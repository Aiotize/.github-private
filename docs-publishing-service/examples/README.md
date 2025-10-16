# Examples

Practical examples for using the Documentation Publishing Service.

## Directory Structure

```
examples/
├── api/              # API usage examples
├── cli/              # Command-line examples
├── sdk/              # SDK examples for different languages
├── workflows/        # Workflow configuration examples
└── sample-docs/      # Sample documentation
```

## Quick Examples

### Publishing a Document via API

```bash
# Using cURL
curl -X POST https://api.docs-publishing.example.com/v1/publish \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "# My Document\n\nThis is my documentation.",
    "format": "markdown",
    "brand": "example-brand",
    "category": "guides",
    "metadata": {
      "title": "My First Document",
      "author": "John Doe",
      "version": "1.0.0"
    }
  }'
```

### Publishing from a File

```bash
# Publish a markdown file
curl -X POST https://api.docs-publishing.example.com/v1/publish \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "source": "docs/getting-started.md",
  "brand": "example-brand",
  "category": "guides",
  "options": {
    "validate": true,
    "transform": true,
    "publish": true
  }
}
EOF
```

### Validating Before Publishing

```bash
# Validate without publishing
curl -X POST https://api.docs-publishing.example.com/v1/validate \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "# Document Title\n\nContent here...",
    "format": "markdown",
    "brand": "example-brand"
  }'
```

### Transforming Between Formats

```bash
# Convert Markdown to HTML
curl -X POST https://api.docs-publishing.example.com/v1/transform \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "# Hello\n\nThis is **bold**",
    "from": "markdown",
    "to": "html",
    "options": {
      "brand": "example-brand",
      "apply_styles": true
    }
  }'
```

## Language-Specific Examples

### JavaScript/Node.js

```javascript
const axios = require('axios');

const publishDoc = async () => {
  const response = await axios.post(
    'https://api.docs-publishing.example.com/v1/publish',
    {
      content: '# My Document\n\nContent here',
      format: 'markdown',
      brand: 'example-brand',
      category: 'guides',
      metadata: {
        title: 'My Document',
        author: 'Jane Doe'
      }
    },
    {
      headers: {
        'Authorization': `Bearer ${process.env.DOCS_API_KEY}`,
        'Content-Type': 'application/json'
      }
    }
  );
  
  console.log('Published:', response.data);
};

publishDoc();
```

### Python

```python
import requests
import os

def publish_document(content, metadata):
    response = requests.post(
        'https://api.docs-publishing.example.com/v1/publish',
        json={
            'content': content,
            'format': 'markdown',
            'brand': 'example-brand',
            'category': 'guides',
            'metadata': metadata
        },
        headers={
            'Authorization': f'Bearer {os.environ["DOCS_API_KEY"]}',
            'Content-Type': 'application/json'
        }
    )
    
    return response.json()

# Usage
doc_content = """
# Getting Started

This is a sample document.
"""

metadata = {
    'title': 'Getting Started',
    'author': 'Documentation Team',
    'version': '1.0.0'
}

result = publish_document(doc_content, metadata)
print(f"Published: {result['id']}")
```

### Go

```go
package main

import (
    "bytes"
    "encoding/json"
    "fmt"
    "net/http"
    "os"
)

type PublishRequest struct {
    Content  string            `json:"content"`
    Format   string            `json:"format"`
    Brand    string            `json:"brand"`
    Category string            `json:"category"`
    Metadata map[string]string `json:"metadata"`
}

func publishDocument(content string, metadata map[string]string) error {
    req := PublishRequest{
        Content:  content,
        Format:   "markdown",
        Brand:    "example-brand",
        Category: "guides",
        Metadata: metadata,
    }
    
    jsonData, _ := json.Marshal(req)
    
    httpReq, _ := http.NewRequest(
        "POST",
        "https://api.docs-publishing.example.com/v1/publish",
        bytes.NewBuffer(jsonData),
    )
    
    httpReq.Header.Set("Authorization", "Bearer "+os.Getenv("DOCS_API_KEY"))
    httpReq.Header.Set("Content-Type", "application/json")
    
    client := &http.Client{}
    resp, err := client.Do(httpReq)
    if err != nil {
        return err
    }
    defer resp.Body.Close()
    
    fmt.Println("Published successfully")
    return nil
}

func main() {
    content := "# Getting Started\n\nSample documentation"
    metadata := map[string]string{
        "title":  "Getting Started",
        "author": "Dev Team",
    }
    
    publishDocument(content, metadata)
}
```

## Batch Processing

### Publishing Multiple Documents

```bash
#!/bin/bash

# Publish all markdown files in a directory
for file in docs/*.md; do
  echo "Publishing $file"
  
  # Extract title from first heading
  TITLE=$(grep -m 1 "^# " "$file" | sed 's/# //')
  
  curl -X POST https://api.docs-publishing.example.com/v1/publish \
    -H "Authorization: Bearer $DOCS_API_KEY" \
    -H "Content-Type: application/json" \
    -d @- <<EOF
{
  "source": "$file",
  "brand": "example-brand",
  "category": "guides",
  "metadata": {
    "title": "$TITLE"
  }
}
EOF

  echo ""
done
```

## GitHub Actions Integration

See complete examples in the [workflows](./workflows/) directory.

### Minimal Example

```yaml
name: Publish Docs
on:
  push:
    branches: [main]
    paths: ['docs/**']

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Publish documentation
        env:
          DOCS_API_KEY: ${{ secrets.DOCS_API_KEY }}
        run: |
          curl -X POST ${{ vars.DOCS_API_URL }}/publish \
            -H "Authorization: Bearer $DOCS_API_KEY" \
            -H "Content-Type: application/json" \
            -d '{"source": "docs/", "brand": "my-brand"}'
```

## More Examples

- [Complete API Examples](./api/)
- [CLI Usage Examples](./cli/)
- [SDK Examples](./sdk/)
- [Sample Documentation](./sample-docs/)

## Need Help?

- Check the [API Documentation](../api/README.md)
- Review [Configuration Guide](../config/README.md)
- See [Main README](../README.md)
