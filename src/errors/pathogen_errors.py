"""Pathogen error definitions."""


class PathogenError(Exception):
    """Base error for pathogen operations."""
    code = "PATHOGEN_ERROR"


class PathogenNotFoundError(PathogenError):
    code = "PATHOGEN_NOT_FOUND"


class PathogenValidationError(PathogenError):
    code = "PATHOGEN_VALIDATION"


class PathogenTimeoutError(PathogenError):
    code = "PATHOGEN_TIMEOUT"


ERROR_CODES = {
    PathogenError.code: "General pathogen error",
    PathogenNotFoundError.code: "Pathogen resource not found",
    PathogenValidationError.code: "Pathogen validation failed",
    PathogenTimeoutError.code: "Pathogen operation timed out",
}
