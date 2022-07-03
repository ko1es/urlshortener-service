from enum import IntEnum


class ErrorCode(IntEnum):
    NOT_FOUND = 0
    BAD_PARAMS = 1
    ALREADY_EXISTS = 2


class UrlShortCodeServiceException(Exception):
    error_code: ErrorCode

    def __init__(self, code: ErrorCode = ErrorCode.NOT_FOUND, message: str = 'Unknown error') -> None:
        super().__init__(message)
        self.error_code = code
        self.message = message


class ShortCodeNotFound(UrlShortCodeServiceException):
    def __init__(self, message: str = 'Not found') -> None:
        super().__init__(ErrorCode.NOT_FOUND, message)


class InvalidParamException(UrlShortCodeServiceException):
    def __init__(self, message: str = 'Unknown invalid param error') -> None:
        super().__init__(ErrorCode.BAD_PARAMS, message)


class AlreadyExistsInRepositoryException(UrlShortCodeServiceException):
    def __init__(self, message: str = 'Parameter already exists error') -> None:
        super().__init__(ErrorCode.ALREADY_EXISTS, message)
