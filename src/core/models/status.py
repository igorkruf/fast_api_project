from .base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Status(Base):

    name: Mapped[str] =  mapped_column(String(1000))
    

    def __str__(self) -> str:
        return f"Статус(name={self.name}, uuid={self.id}"