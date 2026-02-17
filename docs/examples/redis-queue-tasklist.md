# Redis Queue Tasklist

## Phase 1: Infrastructure and Configuration

**Goal:** Add Redis infrastructure, RQ dependencies, and configuration settings so the worker and poller can be built in phase 2.

**Deliverable:** Redis running in docker-compose, `rq` and `redis` available as dependencies, configuration settings for Redis URL and poller/timeout thresholds accessible via `settings`.

**Tasks:**

- [ ] [P1.1] Add `rq>=1.16` and `redis>=5.0` to `packages/samui-backend/pyproject.toml` dependencies and run `cd packages/samui-backend && uv sync`
- [ ] [P1.2] Add `redis` service to `docker-compose.yaml` (image: `redis:7-alpine`, port 6379, healthcheck with `redis-cli ping`, named volume `redis_data`)
- [ ] [P1.3] Add configuration fields to `config.py`:
  - `redis_url: str = "redis://localhost:6379"`
  - `poller_interval_seconds: int = 5`
  - `stale_job_timeout_seconds: int = 60`
  - `failed_job_timeout_seconds: int = 120`
- [ ] [P1.4] Add `REDIS_URL`, `POLLER_INTERVAL_SECONDS`, `STALE_JOB_TIMEOUT_SECONDS`, `FAILED_JOB_TIMEOUT_SECONDS` to `.env.example` with dev defaults and comments explaining each
- [ ] [P1.5] Run existing tests to verify no regressions: `cd packages/samui-backend && uv run pytest ../../tests/ -v`

**Checkpoints:**

- [ ] Code quality: `uvx ruff check packages/samui-backend/src/ && uvx ruff format --check packages/samui-backend/src/`
- [ ] Review: Verify Redis service starts with `docker compose up redis -d` and `docker compose exec redis redis-cli ping` returns PONG

**Phase 1 Complete:** Redis infrastructure available, RQ dependency installed, configuration settings accessible via `settings` object. Existing tests pass unchanged.

---

## Phase 2: Poller and Worker

**Goal:** Create the poller module (stale cleanup + job enqueue loop) and worker entry point (load model, start poller thread, run RQ worker).

**Deliverable:** `poller.py` and `worker.py` modules with unit tests. Poller handles stale/failed job cleanup and enqueues QUEUED jobs to RQ using SKIP LOCKED. Worker loads SAM3 model, starts poller as daemon thread, and runs RQ worker loop.

**Tasks:**

- [ ] [P2.1] Create `packages/samui-backend/src/samui_backend/poller.py` with the poller loop function:
  - `fail_expired_jobs(db)` — Set QUEUED or RUNNING jobs with `created_at` older than `FAILED_JOB_TIMEOUT_SECONDS` to FAILED
  - `reset_stale_jobs(db)` — Set RUNNING jobs with `started_at` older than `STALE_JOB_TIMEOUT_SECONDS` back to QUEUED
  - `enqueue_ready_jobs(db, queue)` — `SELECT ... WHERE status='queued' FOR UPDATE SKIP LOCKED`, update to RUNNING with `started_at=now()`, enqueue job_id to RQ queue with `Retry(max=3)`
  - `run_poller(queue)` — Loop: open DB session, call the three functions above in order, sleep `POLLER_INTERVAL_SECONDS`. Catch and log exceptions per cycle (never crash the thread).
- [ ] [P2.2] Create `packages/samui-backend/src/samui_backend/worker.py` as the worker entry point:
  - Load SAM3 model via `get_sam3_service().load_model()`
  - Create Redis connection from `settings.redis_url`
  - Create RQ `Queue` instance
  - Start poller as daemon thread (`threading.Thread(target=run_poller, args=(queue,), daemon=True)`)
  - Create and start RQ `Worker` with the queue
- [ ] [P2.3] Write unit tests for poller functions in `tests/test_poller.py`:
  - `test_fail_expired_jobs_queued` — QUEUED job past failure threshold is set to FAILED
  - `test_fail_expired_jobs_running` — RUNNING job past failure threshold is set to FAILED
  - `test_fail_expired_jobs_ignores_recent` — Recent QUEUED/RUNNING jobs are not affected
  - `test_fail_expired_jobs_ignores_completed` — COMPLETED/FAILED jobs are not affected
  - `test_reset_stale_jobs` — RUNNING job past stale threshold is reset to QUEUED
  - `test_reset_stale_jobs_ignores_recent` — Recently started RUNNING jobs are not affected
  - `test_enqueue_ready_jobs` — QUEUED jobs are set to RUNNING and enqueued (mock RQ queue)
  - `test_enqueue_ready_jobs_empty` — No QUEUED jobs results in no enqueue calls
- [ ] [P2.4] Run new poller tests: `cd packages/samui-backend && uv run pytest ../../tests/test_poller.py -v`
- [ ] [P2.5] Write unit tests for `process_job()` as RQ task in `tests/test_job_processor.py`:
  - Test with mocked SAM3 and storage services
  - Verify job status transitions to COMPLETED after processing
  - Verify job status transitions to FAILED on exception
  - Verify `current_index` updates per image
  - Note: `process_job()` assumes status is already RUNNING and model is already loaded (set by poller/worker respectively)
- [ ] [P2.6] Run all tests: `cd packages/samui-backend && uv run pytest ../../tests/ -v`

**Checkpoints:**

- [ ] Code quality: `uvx ruff check packages/samui-backend/src/ && uvx ruff format --check packages/samui-backend/src/`
- [ ] Review: Verify poller functions handle edge cases (empty result sets, exceptions) and worker entry point is complete

**Phase 2 Complete:** Poller and worker modules created with passing tests. Poller handles three-step cleanup/enqueue cycle. Worker loads model and starts poller thread.

---

## Phase 3: Integration and Cleanup

**Goal:** Rewire the API route to stop using the in-process queue, adapt `process_job()` for RQ execution, remove dead code, add worker to docker-compose, and update tests.

**Deliverable:** End-to-end flow working: API creates DB record, poller enqueues to RQ, worker processes job. All tests pass. Dead in-process queue code removed.

**Tasks:**

- [ ] [P3.1] Modify `process_job()` in `services/job_processor.py`:
  - Remove `job.status = JobStatus.RUNNING` and `job.started_at` assignment (poller already sets these)
  - Remove `sam3.load_model()` and `sam3.unload_model()` calls (model is resident in worker)
  - Keep image processing loop, status=COMPLETED/FAILED, and error handling unchanged
- [ ] [P3.2] Remove from `services/job_processor.py`:
  - `process_job_and_check_queue()` function
  - `start_job_if_none_running()` function
  - `cleanup_stale_jobs()` function
  - `BackgroundTasks` import and TYPE_CHECKING block
  - `get_background_db` import (if no longer used; check if `process_job` still needs it)
- [ ] [P3.3] Update `services/__init__.py`: remove exports for `start_job_if_none_running`, `process_job_and_check_queue`, `cleanup_stale_jobs`
- [ ] [P3.4] Modify `routes/jobs.py`:
  - Remove `BackgroundTasks` parameter from `create_job()`
  - Remove `start_job_if_none_running()` call and its import
  - The route now just creates the DB record and returns (poller handles the rest)
- [ ] [P3.5] Modify `main.py`:
  - Remove `cleanup_stale_jobs` import and the stale job cleanup block from the lifespan function
  - Keep `Base.metadata.create_all()` for DB table creation
- [ ] [P3.6] Add `worker` service to `docker-compose.yaml`:
  - Same build context and image as `backend`
  - Override CMD to run `python -m samui_backend.worker`
  - Include GPU device reservation (`deploy.resources.reservations.devices` with nvidia driver)
  - Environment: same as backend plus `REDIS_URL=redis://redis:6379`
  - Depends on: `postgres` (healthy), `azurite` (started), `redis` (healthy)
  - Mount huggingface cache volume (read-only)
- [ ] [P3.7] Update `docker-compose.yaml` backend service: add `REDIS_URL` env var (even though API doesn't use it directly, keeps config consistent; alternatively omit — decide based on whether config.py loads it unconditionally). If `config.py` has `redis_url` with a default, the backend service can omit it.
- [ ] [P3.8] Update existing tests:
  - `tests/test_api_jobs.py`: Remove `@patch("samui_backend.routes.jobs.start_job_if_none_running")` from `TestCreateJob` tests. The `create_job` route no longer calls this function, so the mock is unnecessary. Verify tests pass without the mock.
  - `tests/test_job_processor.py` `TestCleanupStaleJobs`: Remove or move these tests since `cleanup_stale_jobs` is removed from `job_processor.py`. The equivalent logic is now tested via `test_poller.py`.
- [ ] [P3.9] Run all tests: `cd packages/samui-backend && uv run pytest ../../tests/ -v`

**Checkpoints:**

- [ ] Code quality: `uvx ruff check packages/samui-backend/src/ && uvx ruff format --check packages/samui-backend/src/`
- [ ] Dead code: `uvx vulture packages/samui-backend/src/ --min-confidence 80`
- [ ] Review: Verify complete flow — API creates job, poller would enqueue (manual verification or integration test), dead code fully removed, all tests pass

**Phase 3 Complete:** In-process queue fully replaced by RQ. API server has no job execution responsibility. Worker container configured with GPU access. All tests pass with no dead code remaining.
