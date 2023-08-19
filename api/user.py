from fastapi import APIRouter

from db import db

router = APIRouter()

user = db.user


@router.get("")
async def get_user():
    return {"user": "unknown"}


@router.get("/count")
async def count_user():
    return {"cnt": await user.count_documents({})}
