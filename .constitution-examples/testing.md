# Testing Principles

## Philosophy

- Tests are a tool for confidence, not a goal
- Test behavior, not implementation details
- Catch real bugs, not theoretical ones
- Fewer meaningful tests > many granular tests
- Don't test every function and component - test features and behaviors

## What to Test

- Core business logic and algorithms
- Error handling and edge cases
- Public APIs and critical user paths

## What Not to Test

- Trivial code (getters, pass-through functions)
- Framework and third-party library internals
- Private implementation details that may change

## Test Quality

- One behavior per test
- Fast, isolated, deterministic
- Clear names that describe expected outcome
