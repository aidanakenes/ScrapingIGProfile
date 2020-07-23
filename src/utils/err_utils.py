class ApplicationError(Exception):
    def __init__(self):
        self.code = 'APIError',
        self.message = f'Failed to parse page for username'


class RegexError(ApplicationError):
    def __init__(self):
        self.code = 'APIError',
        self.message: str = 'Failed to parse regex'


class ValidationError(Exception):
    def __init__(self):
        self.code = 'BadRequest',
        self.message = 'Invalid username: username can contain only letters, numbers, '
        'periods, underscores and be less than 30'
