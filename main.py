from fastapi import FastAPI

from api import user_router

app = FastAPI()

app.include_router(user_router, prefix="/user")


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == '__main__':
    print("Hello")
