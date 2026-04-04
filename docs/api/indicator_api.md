# Indicator API Reference

## Endpoints

### GET /api/v1/indicator

Returns all indicator records.

**Parameters:**
- `limit` (int): Max results (default: 100)
- `offset` (int): Pagination offset
- `filter` (string): Filter expression

### POST /api/v1/indicator

Create a new indicator record.

**Request Body:**
```json
{
  "name": "string",
  "type": "string",
  "metadata": {}
}
```

### GET /api/v1/indicator/{id}

Get indicator by ID.

### DELETE /api/v1/indicator/{id}

Delete indicator record.
