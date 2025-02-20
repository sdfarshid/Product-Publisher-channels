from uuid import UUID
from fastapi import Depends
from pydantic import BaseModel

from app.domain.mixins.pagination import PaginationParams
from app.domain.user.models.user import User
from app.domain.user.value_objects.Email import Email
from app.domain.user.value_objects.Password import Password
from app.infrastructure.mappers.user_mapper import UserMapper
from app.infrastructure.repositories.Interfaces.Iuser_interface import IUserRepository
from app.infrastructure.repositories.user_repository import UserRepository
from app.utils.log import logger
from app.utils.security import generate_salt, generate_password_hash


class UserResponse(BaseModel):
    id: UUID
    email: str
    is_active: bool

    class Config:
        from_attributes = True


class UserService:
    def __init__(self, user_repository: IUserRepository = Depends(UserRepository)):
        self.user_repository = user_repository

    async def list_users(self, pagination: PaginationParams) -> list[UserResponse]:
        all_users = await self.user_repository.get_all_users(pagination)
        logger.debug(f"Error: {type(all_users)}", exc_info=True)
        return [UserResponse.model_validate(user) for user in all_users]

    async def create_user(self, email: Email, password: Password) -> UserResponse:
        salt = generate_salt()
        hashed_password = generate_password_hash(password, salt)
        domain_user = User(
            email=email,
            password=hashed_password,
            salt=salt,
        )
        orm_user = UserMapper.to_orm(domain_user)
        await self.user_repository.add(orm_user)
        return UserResponse.model_validate(orm_user)

    async def get_user(self, user_id: UUID) -> User:
        # Logic to get a user
        pass
