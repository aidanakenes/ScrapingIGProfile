from fastapi import FastAPI, Request, status, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from src.parser import IGParser

app = FastAPI()


@app.get(
    '/profile',
    description='Get profile info'
)
def get(username: str = Query(..., min_length=1, max_length=30, regex='^[a-z0-9_.]{1,30}$')):
    parser = IGParser()
    _user = parser.get_user(username=username)
    if _user:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                {
                    'data': _user,
                    'error': None
                }
            )
        )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {
                'data': None,
                'error': {
                    'code': 'BadRequest',
                    'message': 'Invalid username: username can contain only letters, numbers, '
                               'periods, underscores and be less than 30'
                }
            }
        )
    )
