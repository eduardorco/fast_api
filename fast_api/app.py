from http import HTTPStatus


from fastapi import FastAPI
from fast_api.schemas import Message
# from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/",status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Olá Mundo!"}
