"""Immunity type definitions."""
from typing import Any, Dict, List, Optional, TypedDict
from datetime import datetime


class ImmunityRecord(TypedDict):
    id: str
    name: str
    type: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: Optional[str]


class ImmunityQuery(TypedDict, total=False):
    limit: int
    offset: int
    filter: str
    sort_by: str
    order: str


class ImmunityResponse(TypedDict):
    data: List[ImmunityRecord]
    total: int
    page: int
    has_more: bool
