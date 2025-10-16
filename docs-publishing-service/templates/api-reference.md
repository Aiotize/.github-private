---
title: "API Reference: [API Name]"
author: "API Team"
category: "api-reference"
version: "1.0.0"
date: "YYYY-MM-DD"
tags:
  - api
  - reference
api_version: "v1"
description: "Complete API reference for [API Name]"
status: "draft"
---

# API Reference: [API Name]

## Overview

Brief description of what this API does and its primary use cases.

**Base URL:** `https://api.example.com/v1`

**Authentication:** Bearer token required for all endpoints

## Authentication

All API requests must include an authentication token in the header:

```http
Authorization: Bearer YOUR_API_TOKEN
```

### Getting an API Token

```bash
curl -X POST https://api.example.com/v1/auth/token \
  -H "Content-Type: application/json" \
  -d '{
    "client_id": "your_client_id",
    "client_secret": "your_client_secret"
  }'
```

## Rate Limits

- **Rate Limit:** 1000 requests per hour
- **Burst Limit:** 100 requests per minute

Rate limit information is returned in response headers:

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1234567890
```

## Endpoints

### [Resource Name]

#### List [Resources]

Retrieve a list of all [resources].

```
GET /resources
```

**Query Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `page` | integer | No | Page number for pagination (default: 1) |
| `per_page` | integer | No | Items per page (default: 20, max: 100) |
| `sort` | string | No | Sort field (default: `created_at`) |
| `order` | string | No | Sort order: `asc` or `desc` (default: `desc`) |
| `filter` | string | No | Filter by field values |

**Example Request:**

```bash
curl -X GET "https://api.example.com/v1/resources?page=1&per_page=20" \
  -H "Authorization: Bearer YOUR_API_TOKEN"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "res_123",
      "name": "Resource 1",
      "status": "active",
      "created_at": "2023-01-01T00:00:00Z",
      "updated_at": "2023-01-01T00:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total": 100,
    "total_pages": 5
  }
}
```

**Response Codes:**

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Bad Request |
| 401 | Unauthorized |
| 429 | Rate Limit Exceeded |

---

#### Get [Resource]

Retrieve a specific [resource] by ID.

```
GET /resources/{id}
```

**Path Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | The unique identifier of the resource |

**Example Request:**

```bash
curl -X GET "https://api.example.com/v1/resources/res_123" \
  -H "Authorization: Bearer YOUR_API_TOKEN"
```

**Example Response:**

```json
{
  "id": "res_123",
  "name": "Resource 1",
  "description": "A detailed description",
  "status": "active",
  "metadata": {
    "key": "value"
  },
  "created_at": "2023-01-01T00:00:00Z",
  "updated_at": "2023-01-01T00:00:00Z"
}
```

**Response Codes:**

| Code | Description |
|------|-------------|
| 200 | Success |
| 404 | Resource not found |
| 401 | Unauthorized |

---

#### Create [Resource]

Create a new [resource].

```
POST /resources
```

**Request Body:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Name of the resource |
| `description` | string | No | Description of the resource |
| `metadata` | object | No | Additional metadata |

**Example Request:**

```bash
curl -X POST "https://api.example.com/v1/resources" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "New Resource",
    "description": "A new resource",
    "metadata": {
      "key": "value"
    }
  }'
```

**Example Response:**

```json
{
  "id": "res_124",
  "name": "New Resource",
  "description": "A new resource",
  "status": "active",
  "metadata": {
    "key": "value"
  },
  "created_at": "2023-01-02T00:00:00Z",
  "updated_at": "2023-01-02T00:00:00Z"
}
```

**Response Codes:**

| Code | Description |
|------|-------------|
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 422 | Unprocessable Entity |

---

#### Update [Resource]

Update an existing [resource].

```
PUT /resources/{id}
```

**Path Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | The unique identifier of the resource |

**Request Body:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | No | Name of the resource |
| `description` | string | No | Description of the resource |
| `status` | string | No | Status: `active`, `inactive` |
| `metadata` | object | No | Additional metadata |

**Example Request:**

```bash
curl -X PUT "https://api.example.com/v1/resources/res_123" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Resource",
    "status": "inactive"
  }'
```

**Example Response:**

```json
{
  "id": "res_123",
  "name": "Updated Resource",
  "status": "inactive",
  "updated_at": "2023-01-03T00:00:00Z"
}
```

**Response Codes:**

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Bad Request |
| 404 | Not Found |
| 401 | Unauthorized |

---

#### Delete [Resource]

Delete a [resource].

```
DELETE /resources/{id}
```

**Path Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | The unique identifier of the resource |

**Example Request:**

```bash
curl -X DELETE "https://api.example.com/v1/resources/res_123" \
  -H "Authorization: Bearer YOUR_API_TOKEN"
```

**Example Response:**

```json
{
  "id": "res_123",
  "deleted": true
}
```

**Response Codes:**

| Code | Description |
|------|-------------|
| 200 | Success |
| 404 | Not Found |
| 401 | Unauthorized |

---

## Data Models

### Resource

```typescript
interface Resource {
  id: string;              // Unique identifier
  name: string;            // Resource name
  description?: string;    // Optional description
  status: 'active' | 'inactive';
  metadata?: object;       // Additional metadata
  created_at: string;      // ISO 8601 timestamp
  updated_at: string;      // ISO 8601 timestamp
}
```

### Error Response

```typescript
interface ErrorResponse {
  error: {
    code: string;          // Error code
    message: string;       // Human-readable message
    details?: object;      // Additional error details
  }
}
```

## Error Codes

| Code | Description |
|------|-------------|
| `invalid_request` | The request is malformed |
| `authentication_failed` | Authentication credentials are invalid |
| `authorization_failed` | Insufficient permissions |
| `resource_not_found` | The requested resource doesn't exist |
| `rate_limit_exceeded` | Too many requests |
| `validation_failed` | Request validation failed |
| `internal_error` | An internal server error occurred |

## Webhooks

Subscribe to events to receive notifications when resources change.

### Event Types

- `resource.created`
- `resource.updated`
- `resource.deleted`

### Webhook Payload

```json
{
  "event": "resource.created",
  "timestamp": "2023-01-01T00:00:00Z",
  "data": {
    "id": "res_123",
    "name": "New Resource"
  }
}
```

## SDKs and Libraries

Official SDKs are available for:

- **JavaScript/TypeScript:** `npm install @example/api-client`
- **Python:** `pip install example-api-client`
- **Go:** `go get github.com/example/api-client-go`
- **Ruby:** `gem install example-api-client`

## Support

- **Documentation:** https://docs.example.com
- **Support:** support@example.com
- **Status Page:** https://status.example.com

## Changelog

### v1.0.0 (YYYY-MM-DD)

- Initial release

---

**Last Updated:** YYYY-MM-DD  
**API Version:** v1
