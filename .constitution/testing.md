# Testing Principles

## Testing Philosophy

- Tests are a tool for confidence, not a goal
- Write minimal tests that maximize impact and coverage of critical paths
- Test core business logic, skip obvious glue code
- Prefer testing behavior over implementation details
- Tests should catch real bugs, not theoretical ones

## What to Test

- Core business logic and algorithms
- Complex conditionals and edge cases
- Error handling and validation logic
- Public APIs and interfaces
- Data transformations and processing
- Critical paths that would break user workflows

## What Not to Test

- Trivial getters/setters and pass-through functions
- Framework code and third-party libraries
- Configuration files and constants
- Code that only calls other tested functions
- Generated code
- Private implementation details that may change

## Test Quality

- Each test should verify one behavior or scenario
- Test names describe what is being tested and expected outcome
- Tests are isolated and can run in any order
- Tests are fast and deterministic (no flaky tests)
- Use clear assertions that explain failures
- Avoid test interdependencies

## Test Organization

- Group related tests by feature or module
- Use clear naming conventions for test files and functions
- Separate unit tests from integration tests
- Keep test data and fixtures close to tests
- Extract common setup into reusable helpers
- Maintain test code with same quality as production code
