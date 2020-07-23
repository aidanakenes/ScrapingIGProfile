class ApplicationError(Exception):
    code: str = 'APIError',
    message: str = f'Failed to parse page for username'


class RegexError(ApplicationError):
    message: str = 'Failed to parse regex'


class ValidationError(Exception):
    code: str = 'BadRequest',
    message: str = 'Invalid username: username can contain only letters, numbers, '
    'periods, underscores and be less than 30'
