from pydantic import BaseModel, ConfigDict
from uuid import UUID, uuid4
from datetime import datetime

from app.domain.mixins.audit_mixin import AuditMixin
from app.domain.user.value_objects import Email


class User(BaseModel, AuditMixin):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    id: UUID = uuid4()
    email: Email
    password: str
    salt: str
    is_active: bool = True

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False
