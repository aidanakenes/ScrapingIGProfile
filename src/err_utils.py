from pydantic import BaseModel


class ApplicationError(BaseModel):
    code: str
    message: str


class RegexError(ApplicationError):
    code: str = 'APIError'
    message: str = 'Failed to parse username: invalid regex'
