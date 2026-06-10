import uuid
from sqlalchemy import Column
from sqlalchemy import String
from app.database.connection import Base

class Client(Base):
    __tablename__ = "client"
    client_id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    client_name = Column(
        String(100),
        nullable=False
    )

    client_company = Column(
        String(100),
        nullable = False
    )