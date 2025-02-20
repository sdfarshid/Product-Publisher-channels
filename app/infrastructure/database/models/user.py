from sqlalchemy import Column, String, DateTime, Boolean

from app.infrastructure.database.mixins.audit_mixin import AuditMixin
from app.infrastructure.database.session import Base
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime


class UserDBModel(Base, AuditMixin):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True)
    email = Column(String, unique=True, nullable=True)
    password = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    salt = Column(String, nullable=False)
