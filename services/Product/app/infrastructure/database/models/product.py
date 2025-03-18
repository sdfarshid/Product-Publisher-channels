from sqlalchemy import Column, String, DateTime, Float, Integer, UUID, Enum
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from app.infrastructure.database.session import Base
from datetime import datetime


class ProductDBModel(Base):
    __tablename__ = 'products'
    id = Column(PG_UUID(as_uuid=True), primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    company_id = Column(PG_UUID(as_uuid=True), nullable=False, index=True)
    stock = Column(Integer, nullable=False)
    status = Column(Enum('active', 'inactive', name='product_status'), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    def __str__(self):
        return f"Company(name={self.name}, id={self.id})"