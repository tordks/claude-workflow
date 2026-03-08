# Redis Queue State

## Phase 1: Infrastructure and Configuration

**Goal:** Add Redis infrastructure, RQ dependencies, and configuration settings so the worker and poller can be built in phase 2.

**Deliverable:** Redis running in docker-compose, `rq` and `redis` available as dependencies, configuration settings for Redis URL and poller/timeout thresholds accessible via `settings`.

**Tasks:**

- [ ] [P1.1] **Dependencies** — Add `rq>=1.16` and `redis>=5.0` to `packages/samui-backend/pyproject.toml` and run `cd packages/samui-backend && uv sync`
- [ ] [P1.2] **RedisService** — Add `redis` service to `docker-compose.yaml` (image: `redis:7-alpine`, port 6379, healthcheck with `redis-cli ping`, named volume `redis_data`)
- [ ] [P1.3] **Configuration** — Add `redis_url`, `poller_interval_seconds`, `stale_job_timeout_seconds`, and `failed_job_timeout_seconds` fields to `config.py` with dev defaults
- [ ] [P1.4] **EnvironmentVars** — Add `REDIS_URL`, `POLLER_INTERVAL_SECONDS`, `STALE_JOB_TIMEOUT_SECONDS`, `FAILED_JOB_TIMEOUT_SECONDS` to `.env.example` with dev defaults and comments
- [ ] [P1.5] **RegressionTests** — Run existing tests to verify no regressions: `cd packages/samui-backend && uv run pytest ../../tests/ -v`

**Checkpoints:**

- [ ] Code quality: `uvx ruff check packages/samui-backend/src/ && uvx ruff format --check packages/samui-backend/src/`
- [ ] Code complexity: `uvx ruff check packages/samui-backend/src/ --select C901,PLR0912,PLR0915`
- [ ] Review: Verify Redis service starts with `docker compose up redis -d` and `docker compose exec redis redis-cli ping` returns PONG

**Phase 1 Complete:** Redis infrastructure available, RQ dependency installed, configuration settings accessible via `settings` object. Existing tests pass unchanged.

---

## Phase 2: Poller and Worker

**Goal:** Create the poller module (stale cleanup + job enqueue loop) and worker entry point (load model, start poller thread, run RQ worker).

**Deliverable:** `poller.py` and `worker.py` modules with unit tests. Poller handles stale/failed job cleanup and enqueues QUEUED jobs to RQ using SKIP LOCKED. Worker loads SAM3 model, starts poller as daemon thread, and runs RQ worker loop.

**Tasks:**

- [ ] [P2.1] **Poller** — Create `poller.py` with `fail_expired_jobs`, `reset_stale_jobs`, `enqueue_ready_jobs` (SELECT FOR UPDATE SKIP LOCKED), and `run_poller` loop that calls all three in order each cycle
- [ ] [P2.2] **Worker** — Create `worker.py` entry point: load SAM3 model, create Redis connection and RQ Queue, start poller as daemon thread, start RQ Worker
- [ ] [P2.3] **PollerTests** — Unit tests for poller functions: fail expired (queued/running/ignores recent/ignores completed), reset stale (stale/ignores recent), enqueue ready (queued jobs/empty)
- [ ] [P2.4] **WorkerTests** — Unit tests for `process_job()` as RQ task with mocked SAM3 and storage services: status transitions, `current_index` updates, exception handling

**Checkpoints:**

- [ ] Code quality: `uvx ruff check packages/samui-backend/src/ && uvx ruff format --check packages/samui-backend/src/`
- [ ] Code complexity: `uvx ruff check packages/samui-backend/src/ --select C901,PLR0912,PLR0915`
- [ ] Review: Verify poller functions handle edge cases (empty result sets, exceptions) and worker entry point is complete

**Phase 2 Complete:** Poller and worker modules created with passing tests. Poller handles three-step cleanup/enqueue cycle. Worker loads model and starts poller thread.

---

## Phase 3: Integration and Cleanup

**Goal:** Rewire the API route to stop using the in-process queue, adapt `process_job()` for RQ execution, remove dead code, add worker to docker-compose, and update tests.

**Deliverable:** End-to-end flow working: API creates DB record, poller enqueues to RQ, worker processes job. All tests pass. Dead in-process queue code removed.

**Tasks:**

- [ ] [P3.1] **ProcessJob** — Adapt `process_job()` in `services/job_processor.py`: remove status/started_at assignment (poller sets these), remove `sam3.load_model()`/`unload_model()` calls (model resident in worker)
- [ ] [P3.2] **DeadCodeRemoval** — Remove `process_job_and_check_queue`, `start_job_if_none_running`, `cleanup_stale_jobs` from `job_processor.py` and their exports from `services/__init__.py`
- [ ] [P3.3] **RouteRewire** — Remove `BackgroundTasks` parameter and `start_job_if_none_running()` call from `routes/jobs.py` create_job route
- [ ] [P3.4] **LifespanCleanup** — Remove `cleanup_stale_jobs` import and stale job cleanup block from `main.py` lifespan function
- [ ] [P3.5] **WorkerService** — Add `worker` service to `docker-compose.yaml` with GPU device reservation, same build as backend, CMD `python -m samui_backend.worker`, depends on postgres/azurite/redis
- [ ] [P3.6] **TestUpdates** — Remove `start_job_if_none_running` mock from API job tests, remove/move `TestCleanupStaleJobs` (now covered by poller tests), run full test suite

**Checkpoints:**

- [ ] Code quality: `uvx ruff check packages/samui-backend/src/ && uvx ruff format --check packages/samui-backend/src/`
- [ ] Code complexity: `uvx ruff check packages/samui-backend/src/ --select C901,PLR0912,PLR0915`
- [ ] Dead code: `uvx vulture packages/samui-backend/src/ --min-confidence 80`
- [ ] Review: Verify complete flow — API creates job, poller would enqueue (manual verification or integration test), dead code fully removed, all tests pass

**Phase 3 Complete:** In-process queue fully replaced by RQ. API server has no job execution responsibility. Worker container configured with GPU access. All tests pass with no dead code remaining.
