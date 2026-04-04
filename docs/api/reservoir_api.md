# Reservoir API Reference

## Endpoints

### GET /api/v1/reservoir

Returns all reservoir records.

**Parameters:**
- `limit` (int): Max results (default: 100)
- `offset` (int): Pagination offset
- `filter` (string): Filter expression

### POST /api/v1/reservoir

Create a new reservoir record.

**Request Body:**
```json
{
  "name": "string",
  "type": "string",
  "metadata": {}
}
```

### GET /api/v1/reservoir/{id}

Get reservoir by ID.

### DELETE /api/v1/reservoir/{id}

Delete reservoir record.
