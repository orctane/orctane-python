# Dict with error code -> error type mapping
from typing import Dict, Any, Union


class AppException(Exception):
    """Base class for all errors raised by Orctane SDK.
    This is the parent class of all exceptions (server side)
    raised by the Orctane SDK. Developers can simply catch
    this class and inspect its `code` to implement more specific
    error handling. Note that for some client-side errors ie:
    some method argument missing, a ValueError would be raised.
    Args:
        code: A string error indicating the HTTP status code
        attributed to that Error.
        message: A human-readable error message string.
        suggested_action: A suggested action path to help the user.
        error_type: Maps to the `type` field from the Orctane API
    """

    def __init__(
            self,
            code: str,
            error_type: str,
            message: str,
            suggested_action: str,
    ):
        Exception.__init__(self, message)
        self.code = code
        self.message = message
        self.suggested_action = suggested_action
        self.error_type = error_type


class ValidationException(AppException):
    """Raised when the Orctane SDK encounters a validation error."""

    def __init__(self, code: str, error_type: str, message: str):
        suggested_action = """Please check the error message for details."""
        super().__init__(
            code=code,
            error_type=error_type,
            message=message,
            suggested_action=suggested_action,
        )


class AuthorizationException(AppException):
    """Raised when the Orctane SDK encounters an authorization error."""

    def __init__(self, code: str, error_type: str, message: str):
        suggested_action = """Please check the error message for details."""
        super().__init__(
            code=code,
            error_type=error_type,
            message=message,
            suggested_action=suggested_action,
        )


class InternalServerException(AppException):
    """Raised when the Orctane SDK encounters an internal server error."""

    def __init__(self, code: str, error_type: str, message: str):
        suggested_action = """Please check the error message for details."""
        super().__init__(
            code=code,
            error_type=error_type,
            message=message,
            suggested_action=suggested_action,
        )


ERRORS: Dict[str, Dict[str, Any]] = {
    "400": {"validation_error": ValidationException},
    "401": {"missing_api_key": AuthorizationException},
    "403": {"invalid_api_key": AuthorizationException},
    "500": {"application_error": InternalServerException},
}


def raise_exception(
        code: Union[str, int], error_type: str, message: str
):
    """Raise an exception based on the error code and error type.
    Args:
        code: A string error indicating the HTTP status code
            attributed to that Error.
        error_type: Maps to the `type` field from the Orctane API
        message: A human-readable error message string.
    """
    error = ERRORS.get(code)
    if error:
        if error_type in error:
            raise error[error_type](code, error_type, message)
        else:
            raise AppException(code, error_type, message, 'Please check the error message for details.')
    else:
        raise AppException(code, error_type, message, 'Please check the error message for details.')
