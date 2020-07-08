from pydantic import BaseModel

class ApplicationError(BaseModel):
    message: str
    status_code: int
