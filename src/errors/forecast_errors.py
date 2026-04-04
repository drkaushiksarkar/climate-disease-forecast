"""Forecast error definitions."""


class ForecastError(Exception):
    """Base error for forecast operations."""
    code = "FORECAST_ERROR"


class ForecastNotFoundError(ForecastError):
    code = "FORECAST_NOT_FOUND"


class ForecastValidationError(ForecastError):
    code = "FORECAST_VALIDATION"


class ForecastTimeoutError(ForecastError):
    code = "FORECAST_TIMEOUT"


ERROR_CODES = {
    ForecastError.code: "General forecast error",
    ForecastNotFoundError.code: "Forecast resource not found",
    ForecastValidationError.code: "Forecast validation failed",
    ForecastTimeoutError.code: "Forecast operation timed out",
}
