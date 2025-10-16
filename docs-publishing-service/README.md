# Documentation Publishing Services

An intermediary service that brings coherence, uniformity, and provides a better managed knowledge base platform for brand-endorsed documentation.

## Overview

The Documentation Publishing Services is a comprehensive system designed to standardize, validate, and publish documentation across multiple brands and platforms. It acts as an intermediary layer that ensures all documentation meets brand standards and maintains consistency.

## Architecture

```
┌─────────────────┐
│  Source Docs    │
│  (Any Format)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Intermediary   │
│    Service      │
│  - Validation   │
│  - Transform    │
│  - Standardize  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Brand-Endorsed  │
│  Documentation  │
│  Knowledge Base │
└─────────────────┘
```

## Features

- **Universal Input Support**: Accept documentation in various formats (Markdown, HTML, reStructuredText, etc.)
- **Standardization**: Automatically apply brand guidelines and formatting standards
- **Validation**: Ensure documentation meets quality and consistency requirements
- **Transformation**: Convert between different documentation formats
- **Publishing Workflow**: Automated pipeline for documentation deployment
- **Version Control**: Track changes and maintain documentation history
- **Multi-Brand Support**: Support different brand guidelines and styling

## Components

### 1. API Service
RESTful API for submitting and managing documentation

### 2. Configuration
Brand-specific configuration and styling rules

### 3. Templates
Standardized templates for different documentation types

### 4. Workflows
Automated GitHub Actions workflows for CI/CD

### 5. Examples
Sample documentation and usage examples

## Quick Start

### Publishing a Document

```bash
# Submit a document for publishing
curl -X POST https://api.docs-publishing.example.com/v1/publish \
  -H "Content-Type: application/json" \
  -d '{
    "source": "path/to/document.md",
    "brand": "your-brand",
    "category": "guides",
    "metadata": {
      "title": "Getting Started Guide",
      "author": "Documentation Team",
      "version": "1.0.0"
    }
  }'
```

### Using GitHub Actions

```yaml
name: Publish Documentation
on:
  push:
    paths:
      - 'docs/**'

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: ./docs-publishing-service/workflows/publish-action
        with:
          brand: your-brand
          source-dir: docs/
```

## Configuration

Brand-specific configurations are stored in `config/brands/`. Each brand has:

- Style guidelines
- Template overrides
- Validation rules
- Publishing destinations

## Directory Structure

```
docs-publishing-service/
├── api/                    # API specifications and schemas
├── config/                 # Configuration files
│   └── brands/            # Brand-specific configs
├── templates/             # Documentation templates
├── workflows/             # GitHub Actions workflows
├── examples/              # Usage examples
└── README.md             # This file
```

## API Reference

See [API Documentation](./api/README.md) for detailed API reference.

## Contributing

1. Submit documentation following the guidelines in `templates/`
2. Ensure all validations pass
3. Follow the brand guidelines in `config/brands/`

## Support

For issues or questions, please open an issue in the repository.

## License

See LICENSE file for details.
