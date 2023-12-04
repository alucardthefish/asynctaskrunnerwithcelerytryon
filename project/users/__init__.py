from fastapi import APIRouter
from project.database import SessionLocal


users_router = APIRouter(
    prefix="/user",
)
db = SessionLocal()

from . import models, tasks # noqa

@users_router.get("/", status_code=200)
def get_users():
    users = db.query(models.User).all()
    return users

@users_router.post("/")
def create_user(user_name: str, email: str):
    new_user = models.User(user_name, email)
    db.add(new_user)
    db.commit()
    return new_user

@users_router.get("/summup/", status_code=200)
async def get_summation():
    tasks.sumup.delay(32, 49)
    return {"message": "Summation task is executing..."}
