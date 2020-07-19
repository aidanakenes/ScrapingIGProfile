import uvicorn
from fastapi import FastAPI, Request, status, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from src.service import *

app = FastAPI()


@app.get('/profile', description='Get profile info')
def get(username: str = Query(..., min_length=1, max_length=30, regex='^[a-z0-9_.]{1,30}$')):
    _user = get_cache(username=username)
    if _user is None:
        try:
            _user = get_user(username=username)
        except ApplicationError as e:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=jsonable_encoder(
                    {
                        'error': {
                            'code': 'APIError',
                            'message': f'Failed to parse page for username: {e.message}'
                        }
                    }
                )
            )
    return JSONResponse(
        content=jsonable_encoder({'data': _user})
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {
                'error': {
                    'code': 'BadRequest',
                    'message': 'Invalid username: username can contain only letters, numbers, '
                               'periods, underscores and be less than 30'
                }
            }
        )
    )


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080, workers=4)
