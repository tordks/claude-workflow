# Example Calculator - Tasklist

> **Using This Tasklist**
> - Each task is designed to take 15-30 minutes
> - Complete all tasks in a phase before moving to the next
> - Code must be runnable after each phase
> - Refer to `example-calculator-plan.md` for architectural context

## Phase 0: Branch Setup

**Goal:** Create feature branch

**Deliverable:** New git branch ready for commits

**Tasks:**
- [ ] [P0.1] Create branch using: `git checkout -b feat-example-calculator`

**Phase 0 Checkpoint:** Feature branch created, ready for implementation

## Phase 1: Core Calculator and Validator

**Goal:** Implement core calculation engine and input validation with TDD

**Deliverable:** Working calculator with validated operations passing all tests

**Tasks:**
- [ ] [P1.1] Create src/calculator/ directory and __init__.py
- [ ] [P1.2] Create src/calculator/core.py with Calculator class stub
- [ ] [P1.3] Create src/tests/ directory, __init__.py, and test_core.py
- [ ] [P1.4] Write tests for Calculator.add() method with normal and edge cases
- [ ] [P1.5] Implement Calculator.add() to pass tests
- [ ] [P1.6] Write tests for Calculator.subtract() method
- [ ] [P1.7] Implement Calculator.subtract() to pass tests
- [ ] [P1.8] Write tests for Calculator.multiply() method including zero cases
- [ ] [P1.9] Implement Calculator.multiply() to pass tests
- [ ] [P1.10] Write tests for Calculator.divide() including division by zero
- [ ] [P1.11] Implement Calculator.divide() with error handling
- [ ] [P1.12] Create src/calculator/validator.py with InputValidator class
- [ ] [P1.13] Write tests in test_validator.py for numeric validation
- [ ] [P1.14] Implement InputValidator.validate_number() method
- [ ] [P1.15] Write tests for InputValidator.validate_operation()
- [ ] [P1.16] Implement InputValidator.validate_operation() method
- [ ] [P1.17] Run pytest to verify all tests pass: `pytest src/tests/ -v`

**Phase 1 Checkpoint:** Core calculator operations work correctly with comprehensive test coverage. Input validation prevents invalid operations and inputs. All tests passing.

## Phase 2: CLI Interface

**Goal:** Build command-line interface using click framework

**Deliverable:** Functional CLI tool with proper argument parsing and error handling

**Tasks:**
- [ ] [P2.1] Create src/cli/ directory and __init__.py
- [ ] [P2.2] Create src/cli/main.py with click boilerplate and calc command stub
- [ ] [P2.3] Add click arguments for operation and two numbers
- [ ] [P2.4] Integrate InputValidator to validate CLI arguments
- [ ] [P2.5] Integrate Calculator to perform validated operations
- [ ] [P2.6] Add formatted output for successful calculations
- [ ] [P2.7] Add error handling and user-friendly error messages
- [ ] [P2.8] Add help text and usage examples to CLI
- [ ] [P2.9] Create test_cli.py with tests for CLI argument parsing
- [ ] [P2.10] Test CLI manually: `python -m src.cli.main add 5 3`
- [ ] [P2.11] Test CLI error cases: division by zero, invalid input
- [ ] [P2.12] Verify all CLI tests pass: `pytest src/tests/test_cli.py -v`

**Phase 2 Checkpoint:** CLI interface complete and functional. Users can perform calculations from command line with helpful error messages. All integration points working.

## Phase 3: Testing and Packaging

**Goal:** Achieve comprehensive test coverage and create installable package

**Deliverable:** Package ready for installation with >90% test coverage

**Tasks:**
- [ ] [P3.1] Run pytest with coverage: `pytest --cov=src --cov-report=term-missing`
- [ ] [P3.2] Add missing tests to reach >90% coverage
- [ ] [P3.3] Create setup.py with package metadata and dependencies
- [ ] [P3.4] Add console_scripts entry point for 'calc' command
- [ ] [P3.5] Test installation in development mode: `pip install -e .`
- [ ] [P3.6] Test installed CLI: `calc add 10 5`, `calc divide 20 4`
- [ ] [P3.7] Test all error cases with installed CLI
- [ ] [P3.8] Create README.md with usage instructions and examples
- [ ] [P3.9] Run full test suite one final time: `pytest -v --cov=src`
- [ ] [P3.10] Verify coverage report shows >90% coverage

**Phase 3 Checkpoint:** Calculator packaged and installable. All tests passing with >90% coverage. CLI tool works as expected. Documentation complete. Ready for distribution.
