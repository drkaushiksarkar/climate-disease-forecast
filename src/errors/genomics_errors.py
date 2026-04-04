"""Genomics error definitions."""


class GenomicsError(Exception):
    """Base error for genomics operations."""
    code = "GENOMICS_ERROR"


class GenomicsNotFoundError(GenomicsError):
    code = "GENOMICS_NOT_FOUND"


class GenomicsValidationError(GenomicsError):
    code = "GENOMICS_VALIDATION"


class GenomicsTimeoutError(GenomicsError):
    code = "GENOMICS_TIMEOUT"


ERROR_CODES = {
    GenomicsError.code: "General genomics error",
    GenomicsNotFoundError.code: "Genomics resource not found",
    GenomicsValidationError.code: "Genomics validation failed",
    GenomicsTimeoutError.code: "Genomics operation timed out",
}
