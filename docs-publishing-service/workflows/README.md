# GitHub Actions Workflows

Automated workflows for documentation publishing and management.

## Available Workflows

### 1. Publish Documentation (`publish-docs.yml`)

Automatically validates and publishes documentation when changes are pushed.

**Triggers:**
- Push to `main` branch affecting documentation
- Pull requests affecting documentation
- Manual workflow dispatch

**Features:**
- Validates documentation structure and content
- Checks spelling and grammar
- Publishes to brand-endorsed knowledge base
- Sends notifications on completion

**Usage:**

Place this workflow in your repository's `.github/workflows/` directory:

```bash
cp docs-publishing-service/workflows/publish-docs.yml .github/workflows/
```

**Required Secrets:**
- `DOCS_API_KEY` - API key for documentation publishing service
- `DOCS_API_URL` - (Optional) API endpoint URL

**Manual Trigger:**

You can manually trigger the workflow from GitHub Actions:
1. Go to Actions tab
2. Select "Publish Documentation" workflow
3. Click "Run workflow"
4. Choose brand and options

### 2. Validate Documentation (`validate-docs.yml`)

Runs comprehensive validation on documentation files.

**Usage:**

```yaml
name: Validate Docs
on: [pull_request]

jobs:
  validate:
    uses: ./.github/workflows/validate-docs.yml
```

### 3. Generate Documentation Site (`generate-site.yml`)

Builds a static documentation site from markdown files.

**Usage:**

```yaml
name: Generate Docs Site
on:
  push:
    branches: [main]

jobs:
  build:
    uses: ./.github/workflows/generate-site.yml
```

## Configuration

### Basic Setup

1. **Copy workflow files:**
   ```bash
   mkdir -p .github/workflows
   cp docs-publishing-service/workflows/*.yml .github/workflows/
   ```

2. **Add secrets:**
   - Go to repository Settings > Secrets
   - Add `DOCS_API_KEY`
   - Optionally add `DOCS_API_URL`

3. **Configure brand:**
   - Set brand in workflow file or
   - Use workflow dispatch to specify per run

### Advanced Configuration

#### Custom Validation Rules

Add a `.docsconfig.yml` file to your repository:

```yaml
validation:
  min_words: 150
  max_words: 5000
  strict_mode: true

brand: your-brand-name

categories:
  - guides
  - tutorials
  - reference
```

#### Custom Publishing Destination

Configure publishing destinations in the workflow:

```yaml
env:
  DOCS_API_URL: https://your-api.example.com/v1
  BRAND: your-brand
```

#### Conditional Publishing

Publish only from specific branches:

```yaml
on:
  push:
    branches:
      - main
      - release/**
    paths:
      - 'docs/**'
```

## Workflow Examples

### Example 1: Validate on PR, Publish on Merge

```yaml
name: Documentation Pipeline

on:
  pull_request:
    paths:
      - 'docs/**'
  push:
    branches:
      - main
    paths:
      - 'docs/**'

jobs:
  validate:
    if: github.event_name == 'pull_request'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: ./docs-publishing-service/workflows/validate

  publish:
    if: github.event_name == 'push'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: ./docs-publishing-service/workflows/publish
```

### Example 2: Multi-Brand Publishing

```yaml
name: Publish to Multiple Brands

on:
  push:
    branches: [main]

jobs:
  publish-brand-a:
    uses: ./docs-publishing-service/workflows/publish-docs.yml
    with:
      brand: brand-a
    secrets:
      api_key: ${{ secrets.BRAND_A_API_KEY }}

  publish-brand-b:
    uses: ./docs-publishing-service/workflows/publish-docs.yml
    with:
      brand: brand-b
    secrets:
      api_key: ${{ secrets.BRAND_B_API_KEY }}
```

### Example 3: Scheduled Documentation Updates

```yaml
name: Update Documentation

on:
  schedule:
    - cron: '0 0 * * 0'  # Weekly on Sunday
  workflow_dispatch:

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Update documentation metadata
        run: |
          # Update timestamps, versions, etc.
          find docs -name "*.md" -exec sed -i "s/last_updated:.*/last_updated: $(date -I)/" {} \;
      - name: Commit changes
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@github.com"
          git commit -am "Update documentation metadata" || exit 0
          git push
```

## Integration with CI/CD

### Jenkins

```groovy
pipeline {
    agent any
    stages {
        stage('Validate Docs') {
            steps {
                sh 'curl -X POST -H "Authorization: Bearer $DOCS_API_KEY" $DOCS_API_URL/validate'
            }
        }
        stage('Publish Docs') {
            when { branch 'main' }
            steps {
                sh 'curl -X POST -H "Authorization: Bearer $DOCS_API_KEY" $DOCS_API_URL/publish'
            }
        }
    }
}
```

### GitLab CI

```yaml
validate-docs:
  stage: test
  script:
    - curl -X POST -H "Authorization: Bearer $DOCS_API_KEY" $DOCS_API_URL/validate

publish-docs:
  stage: deploy
  only:
    - main
  script:
    - curl -X POST -H "Authorization: Bearer $DOCS_API_KEY" $DOCS_API_URL/publish
```

## Troubleshooting

### Workflow Not Triggering

- Check file paths in `paths:` filter
- Ensure branch names match
- Verify permissions in repository settings

### API Authentication Failures

- Verify `DOCS_API_KEY` secret is set
- Check API key hasn't expired
- Ensure API key has proper permissions

### Validation Failures

- Review validation rules in brand config
- Check documentation format
- Ensure all required fields are present

## Support

For workflow issues:
1. Check workflow logs in GitHub Actions
2. Review [main documentation](../README.md)
3. Open an issue in the repository
