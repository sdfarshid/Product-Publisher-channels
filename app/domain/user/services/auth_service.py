from uuid import UUID
from fastapi import Depends
from app.domain.user.models.user import User
from app.domain.user.value_objects.Email import Email
from app.domain.user.value_objects.Password import Password
from app.infrastructure.repositories.user_repository import user_repository
from app.utils.security import generate_salt, generate_password_hash


class AuthService:
    pass