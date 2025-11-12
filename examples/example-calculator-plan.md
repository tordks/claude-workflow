# Example Calculator - Plan

## Overview

**Problem:** Users need to perform basic arithmetic calculations from the command line without opening a separate calculator application or Python REPL.

**Purpose:** Add a command-line calculator tool that provides instant arithmetic operations with proper error handling and validation.

**Scope:**
- **IN:** Basic arithmetic operations (add, subtract, multiply, divide), command-line interface, input validation, error handling, unit tests
- **OUT:** Scientific functions (trigonometry, logarithms), graphical interface, history/memory features, multi-step calculations

**Success Criteria:**
- All four operations work correctly
- Division by zero handled gracefully
- Invalid inputs rejected with helpful error messages
- Test coverage >90%
- CLI tool installable and usable

## Architecture & Design

### Component Overview

**Calculator:** Core calculation engine
- Handles arithmetic operations
- Returns results or raises validation errors
- No I/O, pure computation

**InputValidator:** Input validation and parsing
- Validates numeric inputs
- Catches invalid operations
- Returns sanitized values or error messages

**CLI:** Command-line interface
- Uses click framework for argument parsing
- Formats output for terminal display
- Handles user errors gracefully

### Project Structure

```
src/
├── calculator/
│   ├── __init__.py [CREATE]
│   ├── core.py [CREATE]
│   └── validator.py [CREATE]
├── cli/
│   ├── __init__.py [CREATE]
│   └── main.py [CREATE]
└── tests/
    ├── __init__.py [CREATE]
    ├── test_core.py [CREATE]
    ├── test_validator.py [CREATE]
    └── test_cli.py [CREATE]
setup.py [CREATE]
```

### Design Decisions

**Decision:** Use Test-Driven Development (TDD) approach
**Rationale:** Arithmetic operations have clear, testable specifications. Writing tests first ensures correctness and catches edge cases (division by zero, float precision) early. Mathematical operations are ideal for TDD.
**Alternatives Considered:**
- Implementation-first: Faster initially but higher risk of missing edge cases
- Property-based testing only: Overkill for simple arithmetic, adds complexity
**Trade-offs:**
- Pro: High confidence in correctness, catches edge cases, living documentation
- Con: Slightly slower initial development, requires test discipline

**Decision:** Use click framework for CLI
**Rationale:** click provides excellent argument parsing, validation, and help text generation. Well-maintained, Pythonic, and handles common CLI patterns (options, flags, help) out of the box.
**Alternatives Considered:**
- argparse: Standard library but more verbose, less intuitive API
- raw sys.argv parsing: Too low-level, would need to reimplement validation
**Trade-offs:**
- Pro: Clean API, automatic help generation, wide adoption
- Con: External dependency (but stable and lightweight)

**Decision:** Separate validator from core calculator
**Rationale:** Separation of concerns - validation logic (checking types, ranges) is distinct from calculation logic (performing operations). Makes both easier to test and maintain independently.
**Alternatives Considered:**
- Inline validation in calculator: Couples validation with calculation, harder to test
- Validation in CLI only: Allows invalid data to reach calculator, breaks encapsulation
**Trade-offs:**
- Pro: Clear responsibilities, independently testable, reusable validator
- Con: Slightly more code, additional module to maintain

### Data Flow

```
User Input → CLI (click) → InputValidator → Calculator → Result → CLI → Terminal Output
                  ↓                ↓              ↓
              Parse args      Validate types   Compute
              Handle errors   Check ranges     Handle edge cases
```

## Technical Approach

### Dependencies

- **Python 3.10+** - Type hints, match statements
- **click 8.1+** - CLI framework
- **pytest 7.4+** - Testing framework
- **pytest-cov** - Coverage reporting

All dependencies are stable, well-maintained, and commonly used in Python projects.

### Integration Points

- **Standalone module:** No integration with existing systems
- **CLI entry point:** Installed as executable command via setup.py
- **Import API:** Can be imported and used programmatically if needed

### Error Handling

**Division by zero:**
- Validator catches before calculation
- Returns error: "Cannot divide by zero"
- Exit code 1

**Invalid numeric input:**
- Validator catches non-numeric strings
- Returns error: "Invalid number: {input}"
- Exit code 1

**Invalid operation:**
- CLI validates operation in allowed set
- Returns error: "Unknown operation: {op}. Use: add, subtract, multiply, divide"
- Exit code 1

**Overflow/underflow:**
- Python handles naturally with arbitrary precision integers
- Floats may overflow to inf (document in help text)
- No special handling needed for initial version

### Configuration

- No configuration files needed
- All options passed via CLI arguments
- Help text provides usage examples

## Implementation Strategy

### Phase Breakdown

- **Phase 0:** Branch setup (create feat-example-calculator branch)
- **Phase 1:** Core calculator and validator (TDD, core functionality working)
- **Phase 2:** CLI interface (user-facing interface complete)
- **Phase 3:** Testing and packaging (comprehensive tests, installable package)

### Testing Approach

**Unit Tests:**
- Calculator: Test each operation with normal inputs, edge cases, boundaries
- Validator: Test valid/invalid inputs, type checking, range checking
- CLI: Test argument parsing, output formatting, error handling

**Test Cases to Cover:**
- Normal operations: 2 + 2 = 4, 10 - 3 = 7, etc.
- Edge cases: 0 * 100 = 0, 1 / 1 = 1
- Error cases: Division by zero, invalid input, unknown operation
- Float precision: 0.1 + 0.2, decimal representation
- Large numbers: Integer overflow behavior

**Coverage Target:** >90% line coverage

**TDD Workflow:**
1. Write test for operation
2. Implement minimal code to pass
3. Refactor
4. Repeat for next operation

### Deployment Notes

- Package with setup.py for pip installation
- Entry point creates `calc` command
- No database or external services needed
- Can distribute via PyPI or git install

## Risks & Considerations

### Technical Challenges

**Float precision issues**
- Risk: 0.1 + 0.2 ≠ 0.3 in binary floating point
- Mitigation: Document behavior in help text, consider decimal.Decimal for Phase 2
- Impact: Low - expected behavior for floats, users understand

**Input validation edge cases**
- Risk: Unicode numbers, scientific notation, special characters
- Mitigation: Comprehensive test suite, explicit input parsing rules
- Impact: Medium - may require iteration on validator

### Performance Implications

- Performance: Negligible - single operations complete in microseconds
- Memory: Minimal - no state maintained between calculations
- Scale: Not applicable - single-calculation CLI tool

### Security Concerns

**Eval injection**
- Risk: If using eval() to parse expressions
- Mitigation: DON'T use eval(), explicit operation parsing only
- Impact: Critical if violated, none with safe parsing

**Input validation**
- Risk: Unexpected input causing crashes
- Mitigation: Comprehensive validation, no direct eval or exec
- Impact: Low - worst case is error message, no security breach

### Technical Debt

**No calculation history**
- Current: Single calculation per invocation
- Future: Could add --history flag to save/recall previous results
- Reason for deferral: Adds complexity (file I/O, serialization), not in initial scope

**No scientific functions**
- Current: Only basic arithmetic
- Future: Could add math.sin, math.log, etc. in v2
- Reason for deferral: Keeps initial version simple, validates approach first

**No expression parsing**
- Current: Single operation only (calc add 2 3)
- Future: Could parse expressions like "2 + 3 * 4"
- Reason for deferral: Requires parser, increases complexity significantly
