# Vaccine API Reference

## Endpoints

### GET /api/v1/vaccine

Returns all vaccine records.

**Parameters:**
- `limit` (int): Max results (default: 100)
- `offset` (int): Pagination offset
- `filter` (string): Filter expression

### POST /api/v1/vaccine

Create a new vaccine record.

**Request Body:**
```json
{
  "name": "string",
  "type": "string",
  "metadata": {}
}
```

### GET /api/v1/vaccine/{id}

Get vaccine by ID.

### DELETE /api/v1/vaccine/{id}

Delete vaccine record.
