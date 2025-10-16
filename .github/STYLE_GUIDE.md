# Style Guide

**Document Metadata**
- **Author:** Aiotize Organization
- **Maintainer:** Aiotize Standards Team
- **Version:** 1.0.0
- **Last Updated:** 2025-10-16
- **Status:** Active
- **Classification:** Internal Reference
- **Purpose:** Define standard text formatting, metadata, and style guidelines

---

## Document Metadata Standards

### Required File Metadata

All files in Aiotize repositories should include appropriate metadata. The format varies by file type:

#### Markdown Files (.md)

```markdown
<!--
File: filename.md
Author: Author Name or Team
Created: YYYY-MM-DD
Last Modified: YYYY-MM-DD
Version: X.Y.Z
Purpose: Brief description
License: MIT
-->
```

#### Code Files (Python, JavaScript, etc.)

```python
# File: filename.py
# Author: Author Name or Team
# Created: YYYY-MM-DD
# Last Modified: YYYY-MM-DD
# Version: X.Y.Z
# Purpose: Brief description
# License: MIT
```

#### YAML Files (.yml, .yaml)

```yaml
# File: filename.yml
# Author: Author Name or Team
# Created: YYYY-MM-DD
# Last Modified: YYYY-MM-DD
# Version: X.Y.Z
# Purpose: Brief description
```

#### JSON Files (.json)

```json
{
  "_metadata": {
    "file": "filename.json",
    "author": "Author Name or Team",
    "created": "YYYY-MM-DD",
    "lastModified": "YYYY-MM-DD",
    "version": "X.Y.Z",
    "purpose": "Brief description"
  }
}
```

## Text Formatting Standards

### Typography

#### Font Sizes

| Element | Web (px) | Document (pt) | Usage |
|---------|----------|---------------|-------|
| H1 | 32-36 | 24-28 | Page title |
| H2 | 24-28 | 18-20 | Section header |
| H3 | 20-24 | 14-16 | Subsection header |
| H4 | 18-20 | 12-14 | Minor header |
| Body | 14-16 | 11-12 | Main content |
| Small | 12-14 | 9-10 | Captions, notes |
| Code | 13-14 | 10-11 | Code blocks |

#### Line Height

- **Body text:** 1.5-1.6 (150-160% of font size)
- **Headers:** 1.2-1.3
- **Code:** 1.4-1.5
- **Lists:** 1.6-1.8

#### Line Length

- **Optimal:** 50-75 characters per line
- **Maximum:** 80-100 characters per line
- **Code:** 80-120 characters (depends on team standards)

### Text Intensity & Contrast

#### Contrast Ratios (WCAG Compliance)

| Level | Minimum Ratio | Usage |
|-------|---------------|-------|
| AA Normal | 4.5:1 | Body text (14-16px) |
| AA Large | 3:1 | Large text (18px+ or bold 14px+) |
| AAA Normal | 7:1 | Enhanced accessibility |
| AAA Large | 4.5:1 | Large text, enhanced |

#### Color Standards

**Text on White Background:**
- **Primary text:** #24292f (gray-900) - Ratio: 14.5:1
- **Secondary text:** #57606a (gray-700) - Ratio: 7.5:1
- **Tertiary text:** #6e7781 (gray-600) - Ratio: 5.3:1
- **Placeholder text:** #8c959f (gray-500) - Ratio: 3.8:1

**Text on Dark Background:**
- **Primary text:** #ffffff (white) - Ratio: 21:1
- **Secondary text:** #e6edf3 (gray-100) - Ratio: 16:1
- **Tertiary text:** #b1bac4 (gray-300) - Ratio: 9:1

#### Font Weights

- **Regular (400):** Body text, default
- **Medium (500):** Emphasis, labels
- **Semibold (600):** Subheadings, strong emphasis
- **Bold (700):** Headers, critical information

### Markdown Standards

#### Headers

```markdown
# H1: Main Title (Use once per document)

## H2: Major Section

### H3: Subsection

#### H4: Minor Section

##### H5: Rarely Used

###### H6: Avoid if Possible
```

#### Emphasis

```markdown
**Bold text** for strong emphasis
*Italic text* for light emphasis
***Bold and italic*** for critical emphasis
`code` for inline code or technical terms
~~Strikethrough~~ for deprecated content
```

#### Lists

**Unordered Lists:**
```markdown
- Item 1
- Item 2
  - Nested item 2.1
  - Nested item 2.2
- Item 3
```

**Ordered Lists:**
```markdown
1. First item
2. Second item
   1. Nested item 2.1
   2. Nested item 2.2
3. Third item
```

**Task Lists:**
```markdown
- [x] Completed task
- [ ] Pending task
- [ ] Another pending task
```

#### Code Blocks

**Inline Code:**
```markdown
Use `code` for inline code
```

**Code Blocks with Syntax Highlighting:**
````markdown
```python
def hello_world():
    print("Hello, World!")
```

```javascript
function helloWorld() {
    console.log("Hello, World!");
}
```
````

#### Links and References

```markdown
[Link text](https://example.com)
[Link with title](https://example.com "Title text")
[Reference link][ref]

[ref]: https://example.com "Reference title"
```

#### Images

```markdown
![Alt text](image.png)
![Alt text](image.png "Image title")
```

#### Tables

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |
```

#### Blockquotes

```markdown
> This is a blockquote
> It can span multiple lines
>
> And include multiple paragraphs
```

#### Horizontal Rules

```markdown
---
```

## Documentation Standards

### Document Structure

1. **Title** (H1) - Once per document
2. **Metadata** - Author, version, date, etc.
3. **Table of Contents** - For documents >500 words
4. **Introduction/Overview** - Brief summary
5. **Main Content** - Organized with H2/H3 headers
6. **Conclusion/Summary** - Key takeaways
7. **References/Resources** - Links and citations
8. **Footer** - Document control information

### Writing Style

#### General Guidelines

- **Be concise:** Remove unnecessary words
- **Be clear:** Use simple, direct language
- **Be consistent:** Follow established patterns
- **Be inclusive:** Use gender-neutral language
- **Be accurate:** Verify all technical details

#### Voice and Tone

- **Active voice preferred:** "We recommend..." vs "It is recommended..."
- **Second person for instructions:** "You should..." vs "Users should..."
- **Present tense:** "The function returns..." vs "The function will return..."
- **Professional but friendly:** Avoid overly formal language

#### Technical Terms

- **Define acronyms** on first use: "Application Programming Interface (API)"
- **Use code formatting** for technical terms: `function`, `variable`, `class`
- **Link to definitions** for complex concepts
- **Maintain a glossary** for specialized terminology

## File Organization Standards

### Directory Structure

```
project/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   ├── feature_request.yml
│   │   └── config.yml
│   ├── workflows/
│   │   └── *.yml
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── STYLE_GUIDE.md
├── src/
├── tests/
├── docs/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
└── CODEOWNERS
```

### File Naming Conventions

- **Use lowercase:** `my-file.md` not `My-File.md`
- **Use hyphens for spaces:** `user-guide.md` not `user_guide.md`
- **Be descriptive:** `authentication-guide.md` not `auth.md`
- **Use extensions:** `.md`, `.yml`, `.json`, etc.

### Special Files

| File | Purpose | Required |
|------|---------|----------|
| README.md | Project overview | Yes |
| LICENSE | Legal terms | Yes |
| CONTRIBUTING.md | Contribution guide | Recommended |
| CODE_OF_CONDUCT.md | Community guidelines | Recommended |
| SECURITY.md | Security policy | Recommended |
| CODEOWNERS | Code ownership | Optional |
| .gitignore | Git exclusions | Yes |
| CHANGELOG.md | Version history | Recommended |

## Accessibility Standards

### WCAG 2.1 Guidelines

#### Perceivable

- **Text alternatives:** Provide alt text for images
- **Adaptable:** Content can be presented in different ways
- **Distinguishable:** Make it easy to see and hear content

#### Operable

- **Keyboard accessible:** All functionality via keyboard
- **Enough time:** Users have adequate time to read and use content
- **Navigable:** Help users navigate and find content

#### Understandable

- **Readable:** Make text content readable and understandable
- **Predictable:** Web pages appear and operate predictably
- **Input assistance:** Help users avoid and correct mistakes

#### Robust

- **Compatible:** Maximize compatibility with current and future tools

### Best Practices

- Use semantic HTML/Markdown structures
- Maintain proper heading hierarchy
- Provide descriptive link text
- Use sufficient color contrast
- Don't rely on color alone to convey information
- Provide captions for videos
- Make forms accessible with labels

## Version Control Standards

### Commit Messages

```
type(scope): subject

body

footer
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Tests
- `chore`: Maintenance

**Examples:**
```
feat(auth): add OAuth2 support

Implements OAuth2 authentication flow with support for
Google and GitHub providers.

Closes #123
```

### Branch Naming

- `main` or `master`: Production-ready code
- `develop`: Development branch
- `feature/feature-name`: New features
- `bugfix/bug-name`: Bug fixes
- `hotfix/issue-name`: Critical fixes
- `release/version-number`: Release preparation

## Review Process

### Code Review Checklist

- [ ] Metadata present and correct
- [ ] Text formatting follows standards
- [ ] Contrast ratios meet WCAG AA
- [ ] Documentation is clear and complete
- [ ] No spelling or grammatical errors
- [ ] Links are valid and functional
- [ ] Images have alt text
- [ ] Code is properly formatted
- [ ] Tests are included and pass
- [ ] No security vulnerabilities

### Documentation Review

- [ ] Accurate and up-to-date
- [ ] Consistent with style guide
- [ ] Appropriate detail level
- [ ] Examples are helpful and correct
- [ ] Links work correctly
- [ ] Formatting is consistent
- [ ] Metadata is complete

---

**Document Control**
- **Classification:** Internal Reference
- **Review Cycle:** Quarterly
- **Next Review Date:** 2026-01-16
- **Approved By:** Aiotize Standards Team
- **Contact:** standards@aiotize.com

**Revision History**
- 1.0.0 (2025-10-16): Initial version

---

© 2025 Aiotize. All rights reserved.
