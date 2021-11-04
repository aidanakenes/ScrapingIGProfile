import uvicorn

from fastapi import FastAPI, Request, status, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from src.db.cache import Cache
from src.service.parser import IGParser
from src.models.user import User
from src.utils.err_utils import ApplicationError, ValidationError
from src.db.db import DB
from src.utils.conf import LOGGER_CONFIG

app = FastAPI()


@app.get('/profile', description='Get profile info')
async def get(username: str = Query(..., min_length=1, max_length=30, regex='^[a-z0-9_.]{1,30}$')):
    my_redis = Cache()
    _user = my_redis.get_cache(username=username)
    if _user is None:
        try:
            parser = IGParser()
            _user: User = parser.get_user(username=username)
            if _user:
                my_db = DB()
                await my_redis.save_cache(user=_user)
                await my_db.insert_user(user=_user)
        except ApplicationError as e:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=jsonable_encoder({'error': e.__dict__})
            )
    return JSONResponse(
        content=jsonable_encoder({'data': _user})
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({'error': ValidationError().__dict__})
    )


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080, workers=4, log_config=LOGGER_CONFIG)

