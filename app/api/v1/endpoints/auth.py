from fastapi import APIRouter

from app.domain.user.value_objects.Email import Email
from app.domain.user.value_objects.Password import Password

router = APIRouter()


@router.post("/register")
async def register(email: Email, password: Password):
    return {"user_id": 10}
