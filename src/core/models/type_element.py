from .base import Base
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship



class TypeElement(Base):

    name: Mapped[str] =  mapped_column(String(1000))
    is_grade: Mapped[bool] = mapped_column(default=False)

    def __str__(self) -> str:
        return f"TypeElement(name={self.name}, uuid={self.id}"