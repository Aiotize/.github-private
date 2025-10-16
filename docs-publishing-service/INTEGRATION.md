# Integration Guide

Complete guide for integrating the Documentation Publishing Service into your workflow.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Authentication](#authentication)
- [Integration Methods](#integration-methods)
- [CI/CD Integration](#cicd-integration)
- [SDK Integration](#sdk-integration)
- [Webhook Integration](#webhook-integration)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

## Overview

The Documentation Publishing Service can be integrated into your existing workflow in multiple ways:

- **GitHub Actions** - Automated publishing on code changes
- **CI/CD Pipelines** - Jenkins, GitLab CI, Azure DevOps, etc.
- **SDK Integration** - Node.js, Python, Go, Ruby
- **API Integration** - Direct REST API calls
- **Webhooks** - Event-driven updates

## Prerequisites

Before integrating, ensure you have:

1. **Account Access**
   - Active account on the platform
   - Access to your brand's configuration
   - Necessary permissions for publishing

2. **API Credentials**
   - API key from dashboard
   - Appropriate access level (read/write/admin)

3. **Brand Configuration**
   - Brand profile set up
   - Style guidelines configured
   - Validation rules defined

4. **Documentation Repository**
   - Documentation files in supported format
   - Proper directory structure
   - Version control setup

## Quick Start

### 1. Get API Key

```bash
# Visit dashboard and generate API key
https://dashboard.docs-publishing.example.com/settings/api-keys
```

### 2. Test Connection

```bash
export DOCS_API_KEY="your_api_key"
export DOCS_API_URL="https://api.docs-publishing.example.com/v1"

# Test API connection
curl -X GET "$DOCS_API_URL/brands" \
  -H "Authorization: Bearer $DOCS_API_KEY"
```

### 3. Publish Test Document

```bash
# Create a test document
cat > test.md <<EOF
---
title: "Test Document"
author: "Test User"
category: "tests"
---

# Test Document

This is a test.
EOF

# Publish it
curl -X POST "$DOCS_API_URL/publish" \
  -H "Authorization: Bearer $DOCS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "'"$(cat test.md)"'",
    "brand": "your-brand",
    "category": "tests",
    "metadata": {
      "title": "Test Document"
    }
  }'
```

## Authentication

### API Key Authentication

The primary authentication method is API key-based:

```bash
Authorization: Bearer YOUR_API_KEY
```

### Security Best Practices

1. **Never commit API keys to version control**
   ```bash
   # Add to .gitignore
   echo ".env" >> .gitignore
   echo "*.key" >> .gitignore
   ```

2. **Use environment variables**
   ```bash
   # .env file
   DOCS_API_KEY=your_key_here
   DOCS_API_URL=https://api.docs-publishing.example.com/v1
   ```

3. **Rotate keys regularly**
   - Generate new keys every 90 days
   - Revoke old keys after rotation
   - Use different keys for different environments

4. **Limit key permissions**
   - Use read-only keys for listing/viewing
   - Use write keys only where needed
   - Use admin keys sparingly

## Integration Methods

### Method 1: GitHub Actions (Recommended)

Best for: Teams using GitHub for version control

**Setup:**

1. Copy workflow to your repository:
   ```bash
   mkdir -p .github/workflows
   cp docs-publishing-service/workflows/publish-docs.yml .github/workflows/
   ```

2. Add secrets:
   - Go to repository Settings > Secrets and variables > Actions
   - Add `DOCS_API_KEY` secret
   - Optionally add `DOCS_API_URL` variable

3. Configure workflow:
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
         - name: Publish docs
           env:
             DOCS_API_KEY: ${{ secrets.DOCS_API_KEY }}
           run: |
             # Your publishing script
   ```

**Advantages:**
- Automatic publishing on commits
- Built into GitHub interface
- Easy to configure and maintain

### Method 2: GitLab CI/CD

Best for: Teams using GitLab

**Setup (.gitlab-ci.yml):**

```yaml
stages:
  - validate
  - publish

validate-docs:
  stage: validate
  script:
    - |
      for file in docs/**/*.md; do
        curl -X POST "$DOCS_API_URL/validate" \
          -H "Authorization: Bearer $DOCS_API_KEY" \
          -d "@$file"
      done
  only:
    - merge_requests

publish-docs:
  stage: publish
  script:
    - |
      for file in docs/**/*.md; do
        curl -X POST "$DOCS_API_URL/publish" \
          -H "Authorization: Bearer $DOCS_API_KEY" \
          -H "Content-Type: application/json" \
          -d @publish-payload.json
      done
  only:
    - main
```

**Add CI/CD variables:**
- Go to Settings > CI/CD > Variables
- Add `DOCS_API_KEY` (protected, masked)
- Add `DOCS_API_URL`

### Method 3: Jenkins Pipeline

Best for: Teams using Jenkins

**Jenkinsfile:**

```groovy
pipeline {
    agent any
    
    environment {
        DOCS_API_KEY = credentials('docs-api-key')
        DOCS_API_URL = 'https://api.docs-publishing.example.com/v1'
    }
    
    stages {
        stage('Validate') {
            steps {
                script {
                    def files = findFiles(glob: 'docs/**/*.md')
                    files.each { file ->
                        sh """
                            curl -X POST "\${DOCS_API_URL}/validate" \\
                                -H "Authorization: Bearer \${DOCS_API_KEY}" \\
                                -d @${file.path}
                        """
                    }
                }
            }
        }
        
        stage('Publish') {
            when {
                branch 'main'
            }
            steps {
                script {
                    def files = findFiles(glob: 'docs/**/*.md')
                    files.each { file ->
                        sh """
                            curl -X POST "\${DOCS_API_URL}/publish" \\
                                -H "Authorization: Bearer \${DOCS_API_KEY}" \\
                                -H "Content-Type: application/json" \\
                                -d @publish-${file.name}.json
                        """
                    }
                }
            }
        }
    }
    
    post {
        success {
            echo 'Documentation published successfully!'
        }
        failure {
            echo 'Documentation publishing failed!'
        }
    }
}
```

### Method 4: Azure DevOps

Best for: Teams using Azure DevOps

**azure-pipelines.yml:**

```yaml
trigger:
  branches:
    include:
      - main
  paths:
    include:
      - docs/**

variables:
  - group: docs-publishing

stages:
  - stage: Validate
    jobs:
      - job: ValidateDocs
        steps:
          - bash: |
              for file in docs/**/*.md; do
                curl -X POST "$(DOCS_API_URL)/validate" \
                  -H "Authorization: Bearer $(DOCS_API_KEY)" \
                  -d "@$file"
              done
            displayName: 'Validate Documentation'

  - stage: Publish
    dependsOn: Validate
    condition: succeeded()
    jobs:
      - job: PublishDocs
        steps:
          - bash: |
              for file in docs/**/*.md; do
                # Publish each file
                curl -X POST "$(DOCS_API_URL)/publish" \
                  -H "Authorization: Bearer $(DOCS_API_KEY)" \
                  -H "Content-Type: application/json" \
                  -d @payload.json
              done
            displayName: 'Publish Documentation'
```

## SDK Integration

### Node.js

```javascript
const { DocsPublishingClient } = require('./docs-publishing-client');

const client = new DocsPublishingClient({
  apiKey: process.env.DOCS_API_KEY,
  brand: 'your-brand',
});

// Publish a document
await client.publishFile('./docs/guide.md');

// Batch publish
const files = await glob('docs/**/*.md');
await Promise.all(files.map(f => client.publishFile(f)));
```

See [complete Node.js example](./examples/sdk/nodejs-example.js).

### Python

```python
from docs_publishing_client import DocsPublishingClient

client = DocsPublishingClient(
    api_key=os.getenv('DOCS_API_KEY'),
    brand='your-brand'
)

# Publish a document
result = client.publish_file('./docs/guide.md')

# Batch publish
for file in glob.glob('docs/**/*.md', recursive=True):
    client.publish_file(file)
```

See [complete Python example](./examples/sdk/python-example.py).

## Webhook Integration

### Subscribing to Events

Configure webhooks to receive notifications:

```bash
curl -X POST "$DOCS_API_URL/webhooks" \
  -H "Authorization: Bearer $DOCS_API_KEY" \
  -d '{
    "url": "https://your-server.com/webhook",
    "events": ["document.published", "document.updated"],
    "secret": "webhook_secret"
  }'
```

### Webhook Payload

```json
{
  "event": "document.published",
  "timestamp": "2024-01-15T10:30:00Z",
  "data": {
    "id": "doc_123",
    "title": "Document Title",
    "url": "https://docs.example.com/doc",
    "brand": "your-brand"
  },
  "signature": "sha256=..."
}
```

### Webhook Handler Example

```python
from flask import Flask, request
import hmac
import hashlib

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # Verify signature
    signature = request.headers.get('X-Signature')
    payload = request.get_data()
    
    expected = hmac.new(
        WEBHOOK_SECRET.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()
    
    if signature != f"sha256={expected}":
        return 'Invalid signature', 401
    
    # Process event
    event = request.json
    if event['event'] == 'document.published':
        # Handle published document
        notify_team(event['data'])
    
    return 'OK', 200
```

## Best Practices

### 1. Documentation Structure

```
repository/
├── docs/
│   ├── guides/
│   │   ├── getting-started.md
│   │   └── advanced-usage.md
│   ├── api/
│   │   └── reference.md
│   └── tutorials/
│       └── first-steps.md
├── .github/
│   └── workflows/
│       └── publish-docs.yml
└── docs-config.yaml
```

### 2. Validation Before Publishing

Always validate documents before publishing:

```bash
# In CI/CD pipeline
validate_docs() {
  for file in docs/**/*.md; do
    result=$(curl -s -X POST "$DOCS_API_URL/validate" \
      -H "Authorization: Bearer $DOCS_API_KEY" \
      -d "@$file")
    
    valid=$(echo "$result" | jq -r '.valid')
    if [ "$valid" != "true" ]; then
      echo "Validation failed for $file"
      echo "$result" | jq '.errors'
      exit 1
    fi
  done
}
```

### 3. Atomic Publishing

Publish documents atomically to avoid partial deployments:

```bash
# Collect all documents first
docs=()
for file in docs/**/*.md; do
  docs+=("$file")
done

# Validate all
for doc in "${docs[@]}"; do
  validate "$doc" || exit 1
done

# Publish all
for doc in "${docs[@]}"; do
  publish "$doc"
done
```

### 4. Error Handling

Implement robust error handling:

```python
def publish_with_retry(file, max_retries=3):
    for attempt in range(max_retries):
        try:
            return client.publish_file(file)
        except RequestException as e:
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)  # Exponential backoff
```

### 5. Monitoring and Logging

Log all publishing activities:

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def publish_document(file):
    logger.info(f"Publishing {file}")
    try:
        result = client.publish_file(file)
        logger.info(f"Published {file}: {result['id']}")
        return result
    except Exception as e:
        logger.error(f"Failed to publish {file}: {e}")
        raise
```

## Troubleshooting

### Common Issues

#### 1. Authentication Errors

**Problem:** `401 Unauthorized`

**Solutions:**
- Verify API key is correct
- Check key hasn't expired
- Ensure key has write permissions
- Verify Authorization header format

#### 2. Validation Failures

**Problem:** Documents fail validation

**Solutions:**
- Review validation errors
- Check brand guidelines
- Use templates as reference
- Test locally before committing

#### 3. Rate Limiting

**Problem:** `429 Too Many Requests`

**Solutions:**
- Implement exponential backoff
- Batch requests efficiently
- Request rate limit increase
- Cache responses

#### 4. Network Errors

**Problem:** Timeouts or connection errors

**Solutions:**
- Check network connectivity
- Verify API endpoint URL
- Implement retry logic
- Check firewall rules

### Debug Mode

Enable debug logging:

```bash
# Curl with verbose output
curl -v -X POST "$DOCS_API_URL/publish" \
  -H "Authorization: Bearer $DOCS_API_KEY" \
  -d @payload.json

# Node.js
process.env.DEBUG = 'docs-publishing:*'

# Python
logging.basicConfig(level=logging.DEBUG)
```

### Getting Help

If you encounter issues:

1. Check [API documentation](./api/README.md)
2. Review [examples](./examples/)
3. Search [known issues](https://github.com/example/issues)
4. Contact [support](mailto:support@example.com)

## Next Steps

- Review [API Reference](./api/README.md)
- Explore [Examples](./examples/)
- Read [Architecture](./ARCHITECTURE.md)
- Join [Community](https://forum.example.com)

---

Need help with integration? [Contact our team](mailto:support@example.com)
