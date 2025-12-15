# RFC 2119: Writing Conformant Specifications

Quick reference guide for writing clear, testable specification documents using RFC 2119 keywords.

## What is RFC 2119?

RFC 2119 defines keywords (MUST, SHOULD, MAY, etc.) that create unambiguous requirements in specifications. These keywords distinguish between absolute requirements, recommendations, and optional features.

**Why use it:**

- **Clarity:** No ambiguity about what's required vs. recommended vs. optional
- **Testability:** Requirements can be objectively verified
- **Interoperability:** Universal understanding across implementations

## The Keywords

| Keyword | Meaning | Use When |
|---------|---------|----------|
| **MUST** | Absolute requirement | Critical for correctness, safety, or core functionality |
| **MUST NOT** | Absolute prohibition | Prevents errors, violations, or incompatibility |
| **SHOULD** | Strong recommendation | Best practice, important but not critical |
| **SHOULD NOT** | Strong discouragement | Generally harmful but might have valid edge cases |
| **MAY** | Optional, permitted | Truly optional features or variations |
| **RECOMMENDED** | Equivalent to SHOULD | Alternative phrasing for clarity |
| **REQUIRED** | Equivalent to MUST | Alternative phrasing (less common) |
| **OPTIONAL** | Equivalent to MAY | Alternative phrasing for clarity |
| **SHALL** | Equivalent to MUST | Used in formal specifications (rare in docs) |

**Critical Rules:**

- Keywords MUST be UPPERCASE when used normatively
- Lowercase "must", "should", "may" are NOT RFC 2119 keywords (just regular English)

## When to Use Each Keyword

### MUST / REQUIRED / SHALL

**Use for:**

- Core functionality that cannot be omitted
- Safety or security requirements
- Data format requirements
- Syntax that must be followed

**Examples:**

- "Configuration files MUST include version field"
- "API responses MUST follow JSON schema"
- "Authentication headers MUST be present"

**Test:** Would omitting this break the system or cause errors?

### MUST NOT

**Use for:**

- Explicit prohibitions
- Common mistakes to prevent
- Actions that cause failures

**Examples:**

- "API responses MUST NOT contain sensitive data"
- "Configuration files MUST NOT include hardcoded credentials"
- "Resource identifiers MUST NOT be reused after deletion"

**Test:** Would doing this cause problems or violate the design?

### SHOULD / RECOMMENDED

**Use for:**

- Best practices
- Quality guidelines
- Recommendations that improve outcomes
- Things that can be skipped with good reason

**Examples:**

- "Tasks SHOULD take 5-10 minutes"
- "Design decisions SHOULD include rationale"
- "Checkpoints SHOULD describe system state"

**Test:** Would skipping this reduce quality but not break functionality?

### SHOULD NOT

**Use for:**

- Generally bad practices
- Things to avoid unless necessary
- Patterns that usually cause problems

**Examples:**

- "Checkpoints SHOULD NOT simply list completed tasks"
- "Tasks SHOULD NOT exceed 30 minutes"

**Test:** Is this usually problematic but might have valid exceptions?

### MAY / OPTIONAL

**Use for:**

- Truly optional features
- Enhancements beyond core functionality
- Implementation choices

**Examples:**

- "Tasks MAY include indented sub-details"
- "Implementations MAY add custom sections"
- "Level 1 documents MAY omit optional subsections"

**Test:** Is this completely optional without affecting quality or correctness?

## Normative vs. Informative Content

### Normative Content

Content that defines requirements for conformance. Uses RFC 2119 keywords.

**What qualifies:**

- Requirements (MUST/SHOULD/MAY)
- Prohibitions (MUST NOT/SHOULD NOT)
- Conformance criteria
- Validation rules

**How to write:**

- Use RFC 2119 keywords (UPPERCASE)
- Be specific and testable
- Avoid subjective terms

### Informative Content

Content that provides context, examples, or guidance but isn't required for conformance.

**What qualifies:**

- Examples showing how to meet requirements
- Explanatory notes and rationale
- Educational content
- "Why" explanations
- Historical context

**How to mark:**

- Add "(Informative)" label to examples
- Use "Typical Content (Informative):" for descriptive lists
- Add labels: **Best Practice:**, **Tip:**, **Rationale:**, **Note:**
- Use "Why this X?" style headings with informative labels

**Example:**

```markdown
## Section Requirements

**Conformance Requirements:**
- Section MUST include problem statement
- Section SHOULD include scope definition

**Typical Content (Informative):**
- Problem statement (what user need?)
- Feature purpose (what does it do?)
- Scope (in/out boundaries)

**Example (Informative):**
**Problem:** Users cannot search documentation by keyword
**Purpose:** Add keyword search with TF-IDF ranking
```

## Common Specification Patterns

### Pattern 1: Conformance Levels

```markdown
### Level 1 Requirements (MUST)
- Item X MUST be present
- Format Y MUST be followed

### Level 2 Requirements (SHOULD)
- Content SHOULD be detailed
- Best practices SHOULD be followed

### Level 3 Requirements (MAY)
- Enhanced features MAY be included
```

### Pattern 2: Content Focus

```markdown
### Content Focus (All Levels)
- Documents MUST contain X
- Documents MUST NOT contain Y
- Documents MUST NOT contain Z
```

### Pattern 3: Typical Content + Requirements

```markdown
**Typical Content (Informative):**
- Item 1 description
- Item 2 description

**Conformance Requirements:**
- Level 1: Items 1-2 MUST be present
- Level 2: All items SHOULD be detailed
```

### Pattern 4: Common Mistakes Section

```markdown
## Common Mistakes to Avoid

These practices help create effective documents:

**❌ Problem pattern**
- **Tip:** Don't do X
- **Best Practice:** Do Y instead
- **Rationale:** Because Z

**❌ Another pattern**
- **Best Practice:** Clear guidance
```

## Common Mistakes

### ❌ Lowercase Keywords

**Wrong:** "Tasks must use checkboxes"
**Right:** "Tasks MUST use checkboxes"
**Note:** Lowercase "must" is just English, not RFC 2119

### ❌ Unlabeled Examples

**Wrong:**

```markdown
**Example:**
Code sample here
```

**Right:**

```markdown
**Example (Informative):**
Code sample here
```

### ❌ Ambiguous Normative Status

**Wrong:** "Contains: X, Y, Z" (Are these required or typical?)
**Right:** "Typical Content (Informative): X, Y, Z" + separate "Conformance Requirements:"

### ❌ Mixing Requirements and Guidance

**Wrong:** Section mixes "MUST do X" with "Why X matters" without separation
**Right:** Separate "Conformance Requirements:" from "Rationale (Informative):"

### ❌ Subjective Requirements

**Wrong:** "Documentation MUST be thorough"
**Right:** "Documentation MUST include all five required sections"

### ❌ Using Checkmarks for Requirements

**Wrong:** "✅ Does X" in validation section
**Right:** "Implementation MUST do X"

### ❌ Imperatives Without Keywords

**Wrong:** "Include YAML frontmatter"
**Right:** "Implementations MUST include YAML frontmatter"

## Validation Checklist

When writing or reviewing specifications:

**Keyword Usage:**

- [ ] All normative requirements use RFC 2119 keywords (UPPERCASE)
- [ ] No lowercase "must", "should", "may" in normative contexts
- [ ] Keywords chosen appropriately (MUST for critical, SHOULD for recommended, MAY for optional)
- [ ] Prohibitions use MUST NOT (not just absence of MUST)

**Normative/Informative Separation:**

- [ ] All examples labeled "(Informative)"
- [ ] Descriptive lists labeled "Typical Content (Informative):"
- [ ] Explanatory sections clearly marked (Tip:, Best Practice:, Rationale:, Note:)
- [ ] "Why" explanations separated from requirements

**Clarity:**

- [ ] Requirements are testable (objective, not subjective)
- [ ] No ambiguity about what's required vs. recommended vs. optional
- [ ] Each MUST/SHOULD/MAY has clear verification criteria

**Consistency:**

- [ ] Similar content uses similar keyword levels
- [ ] Conformance levels (1/2/3) use consistent MUST/SHOULD/MAY patterns
- [ ] No conflicting requirements

**Completeness:**

- [ ] Common violations have MUST NOT prohibitions
- [ ] Best practices have SHOULD recommendations
- [ ] Optional features have MAY permissions
- [ ] All imperatives have RFC keywords ("Include X" → "Implementations MUST include X")

## Quick Decision Tree

```text
Is this requirement critical for correctness/safety?
├─ Yes → MUST / MUST NOT
└─ No → Is this strongly recommended?
    ├─ Yes → SHOULD / SHOULD NOT
    └─ No → Is this completely optional?
        └─ Yes → MAY / OPTIONAL
```

## Additional Resources

### Essential Reading

**RFC 2119 - Key Words for Requirements (START HERE)**

- **URL:** <https://www.ietf.org/rfc/rfc2119.txt>
- **Length:** 3 pages - very short and clear
- **Why:** The authoritative source for all keyword definitions

**RFC 8174 - Ambiguity of Uppercase vs Lowercase (IMPORTANT)**

- **URL:** <https://www.rfc-editor.org/rfc/rfc8174.html>
- **Why:** Clarifies that lowercase "must"/"should"/"may" are NOT RFC 2119 keywords
- **Key point:** Only UPPERCASE keywords have normative force

### Style Guides & Best Practices

**IETF RFC Style Guide**

- **URL:** <https://www.rfc-editor.org/rfc/rfc7322.html>
- **Covers:** General RFC writing conventions beyond keywords
- **Relevant:** Requirement levels, terminology, examples

**W3C Manual of Style - RFC 2119 Usage**

- **URL:** <https://www.w3.org/2001/06/manual/#rfc2119>
- **Why:** Shows how W3C applies RFC 2119 in web specifications
- **Good for:** Real-world examples from major standards body

### Real-World Examples

**OpenAPI Specification (Recommended Study)**

- **URL:** <https://spec.openapis.org/oas/latest.html>
- **Why:** Excellent RFC 2119 usage in modern API specs
- **Study:** MUST/SHOULD/MAY patterns, normative/informative separation

**Kubernetes API Conventions**

- **URL:** <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md>
- **Why:** Real-world RFC 2119 in large-scale system design
- **Focus:** Clear requirements, explicit prohibitions

**JSON Schema Specification**

- **URL:** <https://json-schema.org/specification.html>
- **Why:** Clean normative/informative separation in data format specs


### Quick References

Bookmark these for fast lookup:

- RFC 2119: <https://www.ietf.org/rfc/rfc2119.txt>
- RFC 8174: <https://www.rfc-editor.org/rfc/rfc8174.html>

---

**Remember:** RFC 2119 keywords create contracts between specification writers and implementers. Use them precisely to create clear, testable, unambiguous requirements.
