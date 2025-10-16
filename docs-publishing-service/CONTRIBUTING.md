# Contributing to Documentation Publishing Service

Thank you for your interest in contributing to the Documentation Publishing Service! This guide will help you get started.

## How to Contribute

There are many ways to contribute:

- 📝 Improve documentation
- 🐛 Report bugs
- ✨ Suggest new features
- 🔧 Submit code improvements
- 📋 Add new templates
- 🎨 Enhance brand configurations
- ✅ Add validation rules

## Getting Started

### 1. Fork the Repository

Fork the repository and clone it locally:

```bash
git clone https://github.com/YOUR-USERNAME/.github-private.git
cd .github-private
```

### 2. Create a Branch

Create a branch for your contribution:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
# or
git checkout -b docs/documentation-improvement
```

Branch naming conventions:
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation updates
- `config/` - Configuration changes
- `template/` - New templates

## Making Changes

### Documentation Improvements

When improving documentation:

1. **Use existing templates** from `docs-publishing-service/templates/`
2. **Include frontmatter** with proper metadata
3. **Follow style guidelines** in brand configurations
4. **Add examples** where applicable
5. **Test your changes** by validating the documentation

Example:

```bash
# Validate your documentation
curl -X POST https://api.docs-publishing.example.com/v1/validate \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d @your-doc.md
```

### Adding New Templates

To add a new documentation template:

1. Create the template in `docs-publishing-service/templates/`
2. Follow the existing template structure
3. Include comprehensive frontmatter
4. Add placeholders for customization
5. Document the template in `templates/README.md`

Template structure:
```markdown
---
title: "Template Title"
category: "template-category"
# ... other metadata
---

# Template Content

Use {{placeholders}} for variable content
```

### Adding Brand Configurations

To add a new brand configuration:

1. Create directory: `docs-publishing-service/config/brands/your-brand/`
2. Add required files:
   - `config.yaml` - Brand settings
   - `styles.css` - Brand styling
   - `validation.yaml` - Validation rules
3. Follow the example brand structure
4. Test with sample documentation

### Adding Validation Rules

When adding new validation rules:

1. Add to `config/validation-rules.yaml` for global rules
2. Or add to brand-specific `validation.yaml`
3. Document the rule with:
   - Rule name and description
   - When it applies
   - Example violations
   - How to fix

### Code Contributions

If contributing code (API implementation, validators, etc.):

1. Follow the existing code style
2. Add tests for new functionality
3. Update documentation
4. Ensure all tests pass

## Validation and Testing

Before submitting your contribution:

### 1. Validate Documentation

```bash
# Check your documentation meets standards
validate-docs your-file.md
```

### 2. Test Configurations

```bash
# Test brand configuration
test-config config/brands/your-brand/
```

### 3. Lint Files

```bash
# Lint YAML files
yamllint config/**/*.yaml

# Lint Markdown files
markdownlint **/*.md
```

## Commit Guidelines

### Commit Message Format

Use clear, descriptive commit messages:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples:**

```
docs(templates): add troubleshooting template

Add a comprehensive troubleshooting template with common issue patterns
and resolution steps.

Closes #123
```

```
feat(validation): add spell checking rule

Implement spell checking validation rule with custom dictionary support.
Configurable per brand.

Refs #456
```

### Commit Best Practices

- Keep commits focused and atomic
- Write clear commit messages
- Reference issues when applicable
- Sign commits if possible

## Submitting Changes

### 1. Push Your Changes

```bash
git push origin your-branch-name
```

### 2. Create a Pull Request

1. Go to the repository on GitHub
2. Click "New Pull Request"
3. Select your branch
4. Fill out the PR template:
   - **Title**: Clear, descriptive title
   - **Description**: What changed and why
   - **Related Issues**: Link to issues
   - **Testing**: How you tested
   - **Screenshots**: For UI changes

### 3. PR Review Process

Your PR will be reviewed for:

- Code quality and style
- Documentation completeness
- Test coverage
- Breaking changes
- Security considerations

Reviewers may:
- Request changes
- Ask questions
- Suggest improvements
- Approve and merge

### 4. Address Feedback

If changes are requested:

```bash
# Make changes
git add .
git commit -m "Address review feedback"
git push origin your-branch-name
```

The PR will automatically update.

## Style Guidelines

### Documentation Style

- **Tone**: Professional but friendly
- **Voice**: Active voice preferred
- **Perspective**: Second person ("you")
- **Tense**: Present tense

### Formatting

- Use headings hierarchically (don't skip levels)
- Keep paragraphs short (3-5 sentences)
- Use lists for readability
- Add code examples where helpful
- Include links to related content

### Code Examples

```markdown
# Always specify language
```bash
command-example
```

# Include comments for clarity
```python
# This does something important
code_example()
```

# Show expected output
Expected output:
```
output here
```
```

## Brand Guidelines

When creating content for specific brands:

1. Check brand configuration in `config/brands/[brand]/`
2. Follow brand-specific style rules
3. Use brand colors and fonts
4. Apply brand terminology preferences
5. Validate against brand rules

## Issue Guidelines

### Reporting Bugs

When reporting bugs, include:

- Clear, descriptive title
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment details
- Screenshots if applicable
- Logs or error messages

Use the bug report template:

```markdown
**Description:**
Clear description of the bug

**Steps to Reproduce:**
1. Step one
2. Step two
3. Step three

**Expected Behavior:**
What should happen

**Actual Behavior:**
What actually happens

**Environment:**
- OS: 
- Version: 
- Browser (if applicable):

**Additional Context:**
Any other relevant information
```

### Suggesting Features

For feature requests, include:

- Problem statement
- Proposed solution
- Alternatives considered
- Use cases
- Benefits

### Asking Questions

For questions:

- Check existing documentation
- Search existing issues
- Be specific and clear
- Include context
- Show what you've tried

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome diverse perspectives
- Accept constructive criticism
- Focus on what's best for the community
- Show empathy

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or inflammatory comments
- Personal attacks
- Publishing others' private information
- Unprofessional conduct

## Recognition

Contributors are recognized in:

- Release notes
- Contributors list
- Project documentation

## Getting Help

Need help contributing?

- 📚 [Documentation](./README.md)
- 💬 [Community Forum](https://forum.example.com)
- 📧 [Email](mailto:docs@example.com)
- 💡 [Examples](./examples/README.md)

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

## Questions?

If you have questions about contributing:

1. Check this guide
2. Review existing issues and PRs
3. Ask in discussions
4. Contact maintainers

---

Thank you for contributing! 🎉
