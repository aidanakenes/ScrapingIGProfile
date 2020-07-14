from fastapi import FastAPI, Request, status, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import redis
import json, ast
from src.parser import IGParser
from src.err_utils import *

app = FastAPI()


@app.get(
    '/profile',
    description='Get profile info'
)
def get(username: str = Query(..., min_length=1, max_length=30, regex='^[a-z0-9_.]{1,30}$')):
    my_redis = redis.Redis(host='127.0.0.1', port=6379)
    cached = my_redis.get(username)
    if cached:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder({'data': json.loads(cached.decode('utf-8'))})
        )
    else:
        parser = IGParser()
        try:
            _user = parser.get_user(username=username)
            my_redis.setex(name=username, time=3600,
                           value=json.dumps(_user.dict(), indent=4, sort_keys=True, ensure_ascii=False))
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=jsonable_encoder({'data': _user})
            )

        except ApplicationError or redis.AuthenticationError as e:
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
