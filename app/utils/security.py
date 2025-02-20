import base64
import os
from passlib.context import CryptContext
from app.domain.user.value_objects.Password import Password
from app.utils.log import logger

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def generate_salt() -> str:
    return base64.b64encode(os.urandom(16)).decode("utf-8")


def generate_password_hash(password: Password, salt: str) -> str:
    salted_password = salt + password.value

    return pwd_context.hash(salted_password)


def verify_password(plain_password: str, hashed_password: str, salt: str) -> bool:
    salted_password = salt + plain_password
    return pwd_context.verify(salted_password, hashed_password)
