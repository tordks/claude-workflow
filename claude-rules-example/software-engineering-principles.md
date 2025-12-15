# Software Engineering Principles

## DRY (Don't Repeat Yourself)

- Each piece of knowledge exists in exactly one place
- Extract repeated logic into functions, classes, or configuration
- Three strikes rule: refactor on third duplication
- Apply to code, data, and documentation

## Orthogonality

- Change one thing without affecting unrelated things
- Decouple components
- Avoid side effects and hidden dependencies
- Test components independently

## YAGNI (You Aren't Gonna Need It)

- Build what's needed now, not what might be needed later
- Add complexity only when requirements demand it
- Delete unused code immediately

## Principle of Least Surprise

- Code behaves as readers expect
- Follow language idioms and conventions
- Use standard patterns over novel solutions
- Name things precisely for their purpose

## Fail Fast

- Detect errors at the earliest possible point
- Validate inputs at system boundaries
- Use type hints and raise specific exceptions
- Never silently ignore errors

## Separation of Concerns

- Business logic separate from presentation
- Configuration separate from code
- Data access separate from domain models
- One responsibility per module/class/function

## Explicit Over Implicit

- Make behavior visible and clear
- Avoid magic: action at a distance, hidden state
- Configuration over convention when clarity matters
- Type annotations reveal intent

## Simplicity Over Complexity

- Choose the straightforward solution over the clever one
- Readable code > premature optimization

## Documentation as Code

- Explain why, not what (code shows what)
- Keep docs adjacent to implementation
- Document constraints, trade-offs, and non-obvious decisions
- Update docs with code changes
