class ApplicationError(Exception):
    message: str


class RegexError(ApplicationError):
    message: str = 'Failed to parse regex'
