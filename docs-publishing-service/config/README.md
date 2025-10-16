# Configuration

Configuration files for the Documentation Publishing Service.

## Structure

```
config/
├── brands/              # Brand-specific configurations
│   ├── example-brand/
│   │   ├── config.yaml
│   │   ├── styles.css
│   │   └── validation.yaml
│   └── README.md
├── default.yaml         # Default service configuration
└── validation-rules.yaml # Global validation rules
```

## Brand Configuration

Each brand has its own directory under `brands/` containing:

### config.yaml
Brand metadata and general settings:
- Brand name and identifier
- Supported categories
- Publishing destinations
- Template preferences

### styles.css
Brand-specific styling for documentation:
- Colors and typography
- Layout preferences
- Component styling

### validation.yaml
Brand-specific validation rules:
- Required sections
- Formatting requirements
- Quality standards
- Terminology guidelines

## Default Configuration

The `default.yaml` file contains service-wide defaults that apply when brand-specific settings are not provided.

## Validation Rules

Global validation rules in `validation-rules.yaml` apply to all brands unless overridden in brand-specific configurations.

## Usage

Brands are automatically detected from the directory structure. To add a new brand:

1. Create a new directory under `brands/`
2. Add `config.yaml` with required settings
3. Optionally add `styles.css` and `validation.yaml`
4. The service will automatically recognize the new brand

## Example

See `brands/example-brand/` for a complete example configuration.
