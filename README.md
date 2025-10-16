# .github-private

## Documentation Publishing Services

This repository contains the **Documentation Publishing Services** - an intermediary service system that brings coherence, uniformity, and provides a better managed knowledge base platform for brand-endorsed documentation.

### Features

- 📝 **Universal Documentation Publishing** - Publish documentation from any format to brand-endorsed platforms
- ✅ **Validation & Quality Assurance** - Automated validation ensuring documentation meets brand standards
- 🔄 **Format Transformation** - Convert between multiple documentation formats seamlessly
- 🎨 **Brand Consistency** - Apply brand-specific styling and guidelines automatically
- 🤖 **Automation Ready** - GitHub Actions workflows for CI/CD integration
- 📊 **Multi-Brand Support** - Manage documentation for multiple brands from one system

### Quick Start

See the [Documentation Publishing Service README](./docs-publishing-service/README.md) for complete documentation.

#### Publishing a Document

```bash
curl -X POST https://api.docs-publishing.example.com/v1/publish \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "source": "path/to/document.md",
    "brand": "your-brand",
    "category": "guides"
  }'
```

#### Using GitHub Actions

```yaml
name: Publish Documentation
on:
  push:
    paths: ['docs/**']

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: ./docs-publishing-service/workflows/publish-action
```

### Documentation

- 📖 [Main Documentation](./docs-publishing-service/README.md)
- 🏗️ [Architecture Overview](./docs-publishing-service/ARCHITECTURE.md)
- 🔌 [API Reference](./docs-publishing-service/api/README.md)
- ⚙️ [Configuration Guide](./docs-publishing-service/config/README.md)
- 📋 [Templates](./docs-publishing-service/templates/README.md)
- 🔄 [Workflows](./docs-publishing-service/workflows/README.md)
- 💡 [Examples](./docs-publishing-service/examples/README.md)

### Repository Structure

```
.github-private/
├── docs-publishing-service/
│   ├── api/                    # API specifications
│   ├── config/                 # Configuration files
│   │   └── brands/            # Brand-specific configs
│   ├── templates/             # Documentation templates
│   ├── workflows/             # GitHub Actions workflows
│   ├── examples/              # Usage examples
│   ├── README.md              # Service documentation
│   └── ARCHITECTURE.md        # Architecture details
├── README.md                  # This file
└── LICENSE