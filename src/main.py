from typing import Literal
from fastapi.params import Depends
from typing_extensions import Annotated
from fastapi import FastAPI, Request, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI()

# もしCORSの有効化をしたい場合はmiddlewareを使う
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)


@app.get("/")
async def root() -> str:
    # GET (パラメータなし)
    return "Hello World!"


def enforce_single_query_param(request: Request):
    """重複しているパラメータがある場合はHTTP 422エラーを返す"""
    query_params = request.query_params.multi_items()
    keys = [key for key, _ in query_params]
    unique_keys = set(keys)
    duplicated_params = [key for key in unique_keys if keys.count(key) >= 2]
    if len(duplicated_params) > 0:
        raise HTTPException(
            status_code=422,
            detail=[
                {
                    "loc": [param],
                    "msg": "Parameter must appear only once",
                    "type": "value_error",
                }
                for param in duplicated_params
            ],
        )


Animal = Literal["cat", "dog", "bird"]


@app.get("/hello")
async def hello_get(
    animal: Animal,
    number: int = Query(...),
    _=Depends(enforce_single_query_param),
) -> dict:
    """GET (パラメータあり)"""
    # intだけだとboolも受け付けてしまうので、boolを除外する
    if isinstance(number, bool):
        raise HTTPException(
            status_code=422,
            detail=[
                {
                    "loc": ["number"],
                    "msg": "Boolean values not allowed for 'number'",
                    "type": "value_error",
                }
            ],
        )

    return {"animal": animal, "number": number}


# pydanticを使うことで入力パラメータのバリデーションを任せることができる
class PostParams(BaseModel):
    text: str
    number: Annotated[int, Field(strict=True)]  # strict=Trueでboolを除外


@app.post("/hello")
async def hello_post(params: PostParams) -> dict:
    # POST （JSONパラメータ）
    return {"text": params.text, "number": params.number}
