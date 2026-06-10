import uuid
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from app.database.connection import Base

class Project(Base):
    __tablename__ = "project"
    project_id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    project_name = Column(
        String(100),
        nullable=False
    )

    client_id = Column(
        String(36),
        ForeignKey("client.client_id"),
        nullable=False
    )