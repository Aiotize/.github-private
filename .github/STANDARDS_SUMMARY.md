# Standards Summary

**Document Metadata**
- **Author:** Aiotize Organization
- **Version:** 1.0.0
- **Last Updated:** 2025-10-16
- **Purpose:** Quick reference for author credentials, metadata, and formatting standards

---

## Quick Reference

### Author Credentials Format

All files should include author information in the appropriate format:

#### Markdown Files
```markdown
<!--
Author: Aiotize Organization / Team Name / Individual Name
Created: 2025-10-16
Last Modified: 2025-10-16
Version: 1.0.0
-->
```

#### Code Files
```python
# Author: Aiotize Organization / Team Name / Individual Name
# Created: 2025-10-16
# Last Modified: 2025-10-16
# Version: 1.0.0
```

### File Metadata Standards

| Field | Required | Format | Example |
|-------|----------|--------|---------|
| Author | Yes | Text (Org/Team/Name) | Aiotize Organization |
| Created | Yes | YYYY-MM-DD | 2025-10-16 |
| Last Modified | Yes | YYYY-MM-DD | 2025-10-16 |
| Version | Recommended | X.Y.Z | 1.0.0 |
| Purpose | Recommended | 1-2 sentence summary | Brief description of file's role |
| License | For code | SPDX identifier | MIT |

**Notes:**
- **Author**: Can be organization name, team name, or individual. For multiple authors, use "Author1, Author2" or "Team Name"
- **Purpose**: Keep to 1-2 sentences describing what the file does or contains
- **Multiple contributors**: Track via git history; Author field shows primary/initial author

### Standard Text Sizes

| Content Type | Size (Web) | Size (Docs) |
|--------------|------------|-------------|
| H1 Header | 32-36px | 24-28pt |
| H2 Header | 24-28px | 18-20pt |
| H3 Header | 20-24px | 14-16pt |
| Body Text | 14-16px | 11-12pt |
| Code | 13-14px | 10-11pt |
| Small/Caption | 12-14px | 9-10pt |

### Text Intensity & Contrast

| Level | Ratio | Usage |
|-------|-------|-------|
| **Primary Text** | 14.5:1 | Main content (#24292f on white) |
| **Secondary Text** | 7.5:1 | Supporting content (#57606a on white) |
| **WCAG AA Normal** | 4.5:1 | Minimum for body text |
| **WCAG AAA Normal** | 7:1 | Enhanced accessibility |

### Font Weights

| Weight | Value | Usage |
|--------|-------|-------|
| Regular | 400 | Body text, default |
| Medium | 500 | Emphasis, labels |
| Semibold | 600 | Subheadings |
| Bold | 700 | Headers, important info |

### Line Height Standards

- **Body text:** 1.5-1.6 (150-160%)
- **Headers:** 1.2-1.3
- **Code:** 1.4-1.5
- **Lists:** 1.6-1.8

### Accessible Color Palette

#### Text on White Background
```
Primary:   #24292f (gray-900) - Ratio: 14.5:1 ✓
Secondary: #57606a (gray-700) - Ratio: 7.5:1  ✓
Tertiary:  #6e7781 (gray-600) - Ratio: 5.3:1  ✓
```

#### Text on Dark Background
```
Primary:   #ffffff (white)    - Ratio: 21:1   ✓
Secondary: #e6edf3 (gray-100) - Ratio: 16:1   ✓
Tertiary:  #b1bac4 (gray-300) - Ratio: 9:1    ✓
```

### File Naming Conventions

**For standard GitHub files (use uppercase):**
- ✓ `README.md`, `LICENSE`, `CONTRIBUTING.md`, `CODEOWNERS`

**For custom/regular files (use lowercase with hyphens):**
- ✓ Use lowercase: `my-file.md`
- ✓ Use hyphens for spaces: `user-guide.md`
- ✓ Be descriptive: `authentication-guide.md`
- ✗ Avoid: `MyFile.md`, `user_guide.md`, `auth.md`

### Required Repository Files

| File | Purpose | Priority |
|------|---------|----------|
| README.md | Overview | Required |
| LICENSE | Legal | Required |
| .gitignore | Git exclusions | Required |
| CODEOWNERS | Ownership | Recommended |
| CONTRIBUTING.md | Contribution guide | Recommended |
| CODE_OF_CONDUCT.md | Community rules | Recommended |
| SECURITY.md | Security policy | Recommended |

### Commit Message Format

```
type(scope): subject

body

footer
```

**Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

**Example:**
```
docs(readme): add author credentials section

Added comprehensive author information and metadata
standards to the README file.

Closes #123
```

### Markdown Checklist

- [ ] Headers use proper hierarchy (H1 → H2 → H3)
- [ ] Text size follows standards (14-16px for body)
- [ ] Contrast ratios meet WCAG AA (4.5:1 minimum)
- [ ] Author metadata included
- [ ] File metadata complete
- [ ] Links are functional
- [ ] Images have alt text
- [ ] Code blocks have syntax highlighting
- [ ] Lists are properly formatted
- [ ] No spelling/grammar errors

### Accessibility Checklist

- [ ] Text meets minimum contrast ratio (4.5:1)
- [ ] All images have alt text
- [ ] Headings follow semantic order
- [ ] Links have descriptive text
- [ ] Color not used alone to convey meaning
- [ ] Keyboard navigation supported
- [ ] ARIA labels where appropriate
- [ ] Content readable without CSS

### Template Files Created

**Note:** All files listed below are part of this repository and are included in this PR.

This repository includes the following templates:

1. **Bug Report** (`.github/ISSUE_TEMPLATE/bug_report.yml`)
   - Structured form for bug reports
   - Includes all required metadata fields

2. **Feature Request** (`.github/ISSUE_TEMPLATE/feature_request.yml`)
   - Structured form for feature requests
   - Includes priority and use case fields

3. **Pull Request** (`.github/PULL_REQUEST_TEMPLATE.md`)
   - Comprehensive PR template
   - Includes testing and documentation checklists

4. **Style Guide** (`.github/STYLE_GUIDE.md`)
   - Complete formatting standards
   - Typography and accessibility guidelines

5. **CODEOWNERS** (Root directory)
   - Defines code ownership
   - Includes team assignments

### Integration Points

These standards apply to:

- ✓ All Markdown documentation
- ✓ Issue and PR templates
- ✓ Code comments and headers
- ✓ README files
- ✓ Wiki pages
- ✓ Commit messages
- ✓ Review feedback
- ✓ Discussion posts

### Tools and Resources

**Accessibility Testing:**
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [WAVE Browser Extension](https://wave.webaim.org/)

**Markdown Tools:**
- [Markdown Lint](https://github.com/markdownlint/markdownlint)
- [Prettier](https://prettier.io/)

**Git Tools:**
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub CLI](https://cli.github.com/)

---

## Implementation Status

✅ **Completed:**
- Author credentials format defined
- File metadata standards established
- Text size standards documented
- Text intensity/contrast standards defined
- Issue templates created with metadata
- PR template created with metadata
- Style guide comprehensive documentation
- CODEOWNERS file with author info
- All community health files include metadata

📝 **Next Steps:**
- Apply standards across all repositories
- Train team on new standards
- Set up automated linting for standards
- Create review checklist automation

---

**Document Control**
- **Quick Reference:** Yes
- **Printable:** Yes
- **Mobile Friendly:** Yes
- **Last Reviewed:** 2025-10-16

For detailed information, see the complete [Style Guide](STYLE_GUIDE.md).

---

© 2025 Aiotize. All rights reserved.
