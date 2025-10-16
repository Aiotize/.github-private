# Documentation Publishing API

RESTful API for the Documentation Publishing Service.

## Base URL

```
https://api.docs-publishing.example.com/v1
```

## Authentication

All API requests require authentication using an API key:

```
Authorization: Bearer YOUR_API_KEY
```

## Endpoints

### POST /publish

Submit a document for publishing.

**Request Body:**

```json
{
  "source": "string",           // Path or URL to source document
  "content": "string",          // Alternative: direct content
  "format": "markdown",         // Source format: markdown, html, rst, etc.
  "brand": "string",            // Brand identifier
  "category": "string",         // Documentation category
  "metadata": {
    "title": "string",
    "author": "string",
    "version": "string",
    "tags": ["string"],
    "description": "string"
  },
  "options": {
    "validate": true,          // Run validation before publishing
    "transform": true,         // Apply transformations
    "publish": true            // Publish immediately or draft
  }
}
```

**Response:**

```json
{
  "id": "string",
  "status": "pending|processing|published|failed",
  "url": "string",
  "validations": {
    "passed": boolean,
    "errors": ["string"],
    "warnings": ["string"]
  },
  "published_at": "timestamp",
  "version": "string"
}
```

### GET /documents/{id}

Retrieve a published document.

**Response:**

```json
{
  "id": "string",
  "title": "string",
  "content": "string",
  "format": "string",
  "brand": "string",
  "category": "string",
  "metadata": {},
  "status": "string",
  "created_at": "timestamp",
  "updated_at": "timestamp",
  "published_at": "timestamp",
  "version": "string"
}
```

### PUT /documents/{id}

Update an existing document.

**Request Body:** Same as POST /publish

**Response:** Same as POST /publish

### DELETE /documents/{id}

Delete a published document.

**Response:**

```json
{
  "id": "string",
  "status": "deleted"
}
```

### GET /documents

List all documents with optional filtering.

**Query Parameters:**
- `brand` - Filter by brand
- `category` - Filter by category
- `status` - Filter by status
- `page` - Page number
- `limit` - Items per page

**Response:**

```json
{
  "documents": [
    {
      "id": "string",
      "title": "string",
      "brand": "string",
      "category": "string",
      "status": "string",
      "published_at": "timestamp"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 100,
    "pages": 5
  }
}
```

### POST /validate

Validate a document without publishing.

**Request Body:**

```json
{
  "content": "string",
  "format": "string",
  "brand": "string",
  "rules": ["string"]  // Optional: specific validation rules
}
```

**Response:**

```json
{
  "valid": boolean,
  "errors": [
    {
      "line": number,
      "column": number,
      "message": "string",
      "rule": "string",
      "severity": "error|warning"
    }
  ],
  "warnings": [],
  "score": number  // 0-100 quality score
}
```

### POST /transform

Transform a document from one format to another.

**Request Body:**

```json
{
  "content": "string",
  "from": "markdown",
  "to": "html",
  "options": {
    "brand": "string",
    "apply_styles": true,
    "include_toc": true
  }
}
```

**Response:**

```json
{
  "content": "string",
  "format": "string",
  "metadata": {}
}
```

### GET /brands

List available brands and their configurations.

**Response:**

```json
{
  "brands": [
    {
      "id": "string",
      "name": "string",
      "description": "string",
      "categories": ["string"],
      "formats": ["string"]
    }
  ]
}
```

### GET /brands/{brand}/config

Get configuration for a specific brand.

**Response:**

```json
{
  "brand": "string",
  "styles": {},
  "validation_rules": [],
  "templates": [],
  "categories": []
}
```

## Error Responses

All errors follow this format:

```json
{
  "error": {
    "code": "string",
    "message": "string",
    "details": {}
  }
}
```

**Common Error Codes:**
- `400` - Bad Request
- `401` - Unauthorized
- `403` - Forbidden
- `404` - Not Found
- `422` - Unprocessable Entity (validation failed)
- `500` - Internal Server Error

## Rate Limiting

- 100 requests per minute per API key
- Rate limit headers included in all responses:
  - `X-RateLimit-Limit`
  - `X-RateLimit-Remaining`
  - `X-RateLimit-Reset`

## Webhooks

Subscribe to events:

- `document.published`
- `document.updated`
- `document.deleted`
- `validation.failed`

Configure webhooks in your brand settings.

## SDK Support

Official SDKs available for:
- JavaScript/Node.js
- Python
- Go
- Ruby

See [examples/](../examples/) for usage examples.
