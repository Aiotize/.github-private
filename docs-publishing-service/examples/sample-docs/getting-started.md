---
title: "Getting Started with Documentation Publishing Service"
author: "Documentation Team"
category: "guides"
version: "1.0.0"
date: "2024-01-15"
tags:
  - getting-started
  - beginner
  - introduction
description: "Learn how to use the Documentation Publishing Service to publish brand-endorsed documentation"
status: "published"
---

# Getting Started with Documentation Publishing Service

Welcome! This guide will help you start publishing documentation to your brand's knowledge base using the Documentation Publishing Service.

## Overview

The Documentation Publishing Service is an intermediary platform that standardizes, validates, and publishes documentation across multiple brands. It ensures consistency, quality, and adherence to brand guidelines.

### Key Benefits

- **Consistency**: Automatic application of brand standards
- **Quality**: Built-in validation and quality checks
- **Automation**: CI/CD integration for seamless publishing
- **Multi-format**: Support for various input and output formats
- **Centralized**: Single platform for all documentation

## Prerequisites

Before you begin, ensure you have:

- [ ] An active account on the platform
- [ ] API access key (get one from [dashboard](https://dashboard.example.com))
- [ ] Basic knowledge of Markdown or your preferred documentation format
- [ ] Access to your brand's configuration

## Step 1: Set Up Your Environment

### Get Your API Key

1. Log in to the [dashboard](https://dashboard.example.com)
2. Navigate to Settings > API Keys
3. Click "Generate New Key"
4. Save your API key securely

**Important:** Keep your API key secret and never commit it to version control.

### Configure Environment

Set your API key as an environment variable:

```bash
export DOCS_API_KEY="your_api_key_here"
export DOCS_API_URL="https://api.docs-publishing.example.com/v1"
```

Or create a `.env` file:

```bash
DOCS_API_KEY=your_api_key_here
DOCS_API_URL=https://api.docs-publishing.example.com/v1
```

## Step 2: Create Your First Document

### Choose a Template

Start with a template to ensure proper structure:

```bash
# Copy the standard template
cp docs-publishing-service/templates/standard.md my-first-doc.md
```

### Add Content

Edit `my-first-doc.md` and fill in the sections:

```markdown
---
title: "My First Document"
author: "Your Name"
category: "guides"
version: "1.0.0"
date: "2024-01-15"
tags:
  - example
description: "This is my first published document"
status: "draft"
---

# My First Document

## Overview

This is an example document to demonstrate the publishing process.

## Main Content

Add your content here following the template structure.

### Subsection

Include code examples when needed:

```bash
echo "Hello, Documentation!"
```

## Next Steps

After reading this document, you can:
1. Create more documentation
2. Explore advanced features
3. Share with your team
```

## Step 3: Validate Your Document

Before publishing, validate your document:

```bash
curl -X POST $DOCS_API_URL/validate \
  -H "Authorization: Bearer $DOCS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "'"$(cat my-first-doc.md)"'",
    "format": "markdown",
    "brand": "your-brand"
  }'
```

**Response:**

```json
{
  "valid": true,
  "errors": [],
  "warnings": [
    {
      "line": 10,
      "message": "Consider adding more detail to this section",
      "severity": "warning"
    }
  ],
  "score": 85
}
```

### Fix Validation Issues

If there are errors:

1. Review the error messages
2. Fix the issues in your document
3. Validate again until all errors are resolved

## Step 4: Publish Your Document

Once validation passes, publish your document:

```bash
curl -X POST $DOCS_API_URL/publish \
  -H "Authorization: Bearer $DOCS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "source": "my-first-doc.md",
    "brand": "your-brand",
    "category": "guides",
    "metadata": {
      "title": "My First Document",
      "author": "Your Name",
      "version": "1.0.0"
    },
    "options": {
      "validate": true,
      "transform": true,
      "publish": true
    }
  }'
```

**Success Response:**

```json
{
  "id": "doc_abc123",
  "status": "published",
  "url": "https://docs.your-brand.com/guides/my-first-document",
  "validations": {
    "passed": true,
    "errors": [],
    "warnings": []
  },
  "published_at": "2024-01-15T10:30:00Z",
  "version": "1.0.0"
}
```

## Step 5: Verify Publication

Check that your document is published:

```bash
curl -X GET $DOCS_API_URL/documents/doc_abc123 \
  -H "Authorization: Bearer $DOCS_API_KEY"
```

Visit the URL in the response to see your published document.

## Automating with GitHub Actions

For automatic publishing on every commit:

1. Create `.github/workflows/publish-docs.yml` in your repository

2. Add the workflow configuration:

```yaml
name: Publish Documentation

on:
  push:
    branches: [main]
    paths: ['docs/**']

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Publish to Knowledge Base
        env:
          DOCS_API_KEY: ${{ secrets.DOCS_API_KEY }}
        run: |
          for file in docs/*.md; do
            curl -X POST ${{ vars.DOCS_API_URL }}/publish \
              -H "Authorization: Bearer $DOCS_API_KEY" \
              -H "Content-Type: application/json" \
              -d @- <<EOF
          {
            "source": "$file",
            "brand": "your-brand",
            "category": "guides"
          }
          EOF
          done
```

3. Add your API key as a GitHub secret:
   - Go to repository Settings > Secrets
   - Add `DOCS_API_KEY` with your key

Now documentation publishes automatically on push!

## Best Practices

### Writing Quality Documentation

1. **Use templates** - Start with provided templates
2. **Include examples** - Show, don't just tell
3. **Keep it current** - Update documentation with code changes
4. **Be concise** - Short paragraphs, clear language
5. **Link related docs** - Help readers find more information

### Organization

- **Categorize properly** - Use appropriate categories
- **Version your docs** - Track changes over time
- **Tag effectively** - Make documents discoverable
- **Maintain metadata** - Keep frontmatter up to date

### Validation

- **Validate before publishing** - Catch issues early
- **Fix all errors** - Don't ignore validation errors
- **Address warnings** - Improve quality scores
- **Test links** - Ensure all links work

## Common Tasks

### Update a Document

```bash
# Update existing document
curl -X PUT $DOCS_API_URL/documents/doc_abc123 \
  -H "Authorization: Bearer $DOCS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Updated content here",
    "metadata": {
      "version": "1.1.0"
    }
  }'
```

### List Your Documents

```bash
# Get all your documents
curl -X GET "$DOCS_API_URL/documents?brand=your-brand" \
  -H "Authorization: Bearer $DOCS_API_KEY"
```

### Delete a Document

```bash
# Delete a document
curl -X DELETE $DOCS_API_URL/documents/doc_abc123 \
  -H "Authorization: Bearer $DOCS_API_KEY"
```

## Troubleshooting

### Authentication Errors

**Problem:** Getting 401 Unauthorized errors

**Solution:** 
- Verify your API key is correct
- Check that the key hasn't expired
- Ensure the Authorization header is properly formatted

### Validation Failures

**Problem:** Document fails validation

**Solution:**
- Review error messages carefully
- Check against brand guidelines
- Use templates as reference
- See [validation rules](../config/validation-rules.yaml)

### Publishing Errors

**Problem:** Document won't publish

**Solution:**
- Ensure all validation errors are fixed
- Check brand configuration is correct
- Verify network connectivity
- Check API status at [status page](https://status.example.com)

## Next Steps

Now that you've published your first document, you can:

1. **Explore Templates** - Check out [all templates](../templates/)
2. **Learn Advanced Features** - See [API documentation](../api/README.md)
3. **Set Up Automation** - Configure [workflows](../workflows/)
4. **Join the Community** - Get help at [forum](https://forum.example.com)

## Resources

- **API Reference**: [Complete API docs](../api/README.md)
- **Templates**: [Documentation templates](../templates/)
- **Examples**: [More examples](../examples/)
- **Support**: [Contact support](mailto:docs@example.com)

## Feedback

Have questions or suggestions? [Open an issue](https://github.com/example/issues) or [contact us](mailto:docs@example.com).

---

**Last Updated:** 2024-01-15  
**Version:** 1.0.0

**Ready to publish more?** Continue to [Advanced Publishing Guide](link) for detailed features.
