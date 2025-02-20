from app.domain.user.models.user import User
from app.infrastructure.database.models.user import UserDBModel

class UserMapper():
    @staticmethod
    def to_domain(orm_model: UserDBModel) -> User:
        return User(
            id=orm_model.id,
            email=orm_model.email,
            hashed_password=orm_model.password,
            salt=orm_model.salt,
            is_active=orm_model.is_active,
            created_at=orm_model.created_at,
            updated_at=orm_model.updated_at
        )

    @staticmethod
    def to_orm(domain_model: User) -> UserDBModel:
        return UserDBModel(
            id=domain_model.id,
            email=domain_model.email.value,
            password=domain_model.password,
            salt=domain_model.salt,
            is_active=domain_model.is_active,
            created_at=domain_model.created_at,
            updated_at=domain_model.updated_at
        )