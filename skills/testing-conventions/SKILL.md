# Testing Conventions

Apply testing philosophy from `.constitution/testing.md`.

## Testing Philosophy

Tests are a tool for confidence, not a goal. Write minimal tests that maximize impact and coverage of critical paths.

### Key Principles

- Test core business logic, skip obvious glue code
- Prefer testing behavior over implementation details
- Tests should catch real bugs, not theoretical ones
- Write tests that maximize confidence with minimal overhead

## What to Test

Focus testing efforts on:
- Core business logic and algorithms
- Complex conditionals and edge cases
- Error handling and validation logic
- Public APIs and interfaces
- Data transformations and processing
- Critical paths that would break user workflows

## What Not to Test

Avoid wasting effort on:
- Trivial getters/setters and pass-through functions
- Framework code and third-party libraries
- Configuration files and constants
- Code that only calls other tested functions
- Generated code
- Private implementation details that may change

## Test Quality

Each test should:
- Verify one behavior or scenario
- Have names that describe what is being tested and expected outcome
- Be isolated and able to run in any order
- Be fast and deterministic (no flaky tests)
- Use clear assertions that explain failures
- Avoid interdependencies with other tests

## Test Organization

- Group related tests by feature or module
- Use clear naming conventions for test files and functions
- Separate unit tests from integration tests
- Keep test data and fixtures close to tests
- Extract common setup into reusable helpers
- Maintain test code with same quality as production code

---

For complete details and examples, read `.constitution/testing.md`.
