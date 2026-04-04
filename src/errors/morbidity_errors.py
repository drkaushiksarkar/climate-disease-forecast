"""Morbidity error definitions."""


class MorbidityError(Exception):
    """Base error for morbidity operations."""
    code = "MORBIDITY_ERROR"


class MorbidityNotFoundError(MorbidityError):
    code = "MORBIDITY_NOT_FOUND"


class MorbidityValidationError(MorbidityError):
    code = "MORBIDITY_VALIDATION"


class MorbidityTimeoutError(MorbidityError):
    code = "MORBIDITY_TIMEOUT"


ERROR_CODES = {
    MorbidityError.code: "General morbidity error",
    MorbidityNotFoundError.code: "Morbidity resource not found",
    MorbidityValidationError.code: "Morbidity validation failed",
    MorbidityTimeoutError.code: "Morbidity operation timed out",
}
