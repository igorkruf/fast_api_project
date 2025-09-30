from .base import Base
from .type_element import TypeElement
from .status import Status
from typing import List, Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
import uuid
from enum import Enum
from sqlalchemy import Enum as SQLEnum

class StatusElement(Enum):

    PASSED="passed"
    COMPLETED="completed"
    FAILED="failed"
    INCOMPLETE="incomplete"
    BROWSED="browsed"
    NOT_ATTEMPTED="not attempted"

    @property
    def discription(self)->str:
        description={
            StatusElement.PASSED: "Успешное завершение (Пользователь успешно прошел тест)",
            StatusElement.COMPLETED: "Завершено (Пользователь просмотрел курс до последнего слайда)",
            StatusElement.FAILED: "Неуспешное завершение (Пользователь не прошел тест)",
            StatusElement.INCOMPLETE: "Не завершено (Пользователь не просмотрел курс до последнего слайда)",
            StatusElement.BROWSED: "Просмотрено (Если при сборке SCORM не указано обязательное прохождение теста и просмотр всех слайдов)",
            StatusElement.NOT_ATTEMPTED: "Не начато"
        }
        return description[self]


class Element(Base):

    name: Mapped[str] =  mapped_column(String(1000))
    type_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("type_element.id"))
    type: Mapped[TypeElement] =  relationship(back_populates='elements')
    is_grade: Mapped[bool] = mapped_column(default=False)
    status: Mapped[StatusElement] =  mapped_column(
        SQLEnum(StatusElement), 
        default=StatusElement.NOT_ATTEMPTED
        )

    def __str__(self) -> str:
        return f"Element(name={self.name}, status={self.status.discription}"