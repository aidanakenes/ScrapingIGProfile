class ApplicationError(Exception):
    message: str


class RegexError(ApplicationError):
    message: str = 'invalid regex'
