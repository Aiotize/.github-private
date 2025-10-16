# Documentation Templates

Standardized templates for creating consistent, brand-endorsed documentation.

## Available Templates

### 1. Standard Documentation Template
General-purpose template for most documentation needs.
- **File:** `standard.md`
- **Use for:** User guides, concept docs, general documentation

### 2. Tutorial Template
Step-by-step guide template with structured learning objectives.
- **File:** `tutorial.md`
- **Use for:** Tutorials, how-to guides, walkthroughs

### 3. API Reference Template
Technical reference documentation for APIs.
- **File:** `api-reference.md`
- **Use for:** API documentation, SDK references

### 4. Troubleshooting Template
Problem-solution format for troubleshooting guides.
- **File:** `troubleshooting.md`
- **Use for:** Error resolution, debugging guides

### 5. Release Notes Template
Structured format for release announcements.
- **File:** `release-notes.md`
- **Use for:** Version releases, changelog entries

### 6. Quick Start Template
Condensed guide for getting started quickly.
- **File:** `quickstart.md`
- **Use for:** Getting started guides, quick references

## Using Templates

### Command Line

```bash
# Copy a template to start a new document
cp templates/standard.md my-new-doc.md

# Or use the publishing service
curl -X POST https://api.docs-publishing.example.com/v1/documents/from-template \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "template": "standard",
    "title": "My New Document",
    "category": "guides"
  }'
```

### GitHub Actions

```yaml
- name: Create document from template
  uses: ./docs-publishing-service/workflows/create-from-template
  with:
    template: standard
    output: docs/my-new-doc.md
```

## Template Structure

All templates follow this basic structure:

1. **Frontmatter** - Metadata in YAML format
2. **Title** - Main document title
3. **Overview** - Brief introduction
4. **Prerequisites** - Required knowledge/setup (if applicable)
5. **Main Content** - Core documentation
6. **Next Steps** - What to do next
7. **Related Resources** - Links to related docs

## Customization

Templates can be customized per brand:

1. Copy the template to `config/brands/{brand}/templates/`
2. Modify as needed
3. The service will use brand-specific templates when available

## Template Variables

Templates support variable substitution:

- `{{title}}` - Document title
- `{{author}}` - Document author
- `{{date}}` - Current date
- `{{version}}` - Document version
- `{{brand}}` - Brand name
- `{{category}}` - Document category

Example:
```markdown
# {{title}}

**Author:** {{author}}  
**Version:** {{version}}  
**Last Updated:** {{date}}
```

## Best Practices

1. **Start with a template** - Don't write from scratch
2. **Keep frontmatter accurate** - Metadata is used for organization
3. **Follow the structure** - Consistency helps readers
4. **Fill in all sections** - Remove sections that don't apply
5. **Use placeholders** - Mark areas that need completion

## Contributing New Templates

To add a new template:

1. Create the template file in `templates/`
2. Follow the standard structure
3. Include comprehensive frontmatter
4. Add documentation to this README
5. Test with the validation service

## Support

For questions about templates, see the main [Documentation Publishing Service README](../README.md).
