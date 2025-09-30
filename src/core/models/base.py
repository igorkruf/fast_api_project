from core.config import settings 
from sqlalchemy import MetaData, UUID
import uuid
from sqlalchemy.orm import (
                            DeclarativeBase,
                            Mapped,
                            mapped_column,
                            declared_attr
                           ) 
from utils import (
                    camel_case_to_snake_case
                  )


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention=settings.db.naming_convention,
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{camel_case_to_snake_case(cls.__name__)}s"

    id: Mapped[uuid.UUID] = mapped_column(
                                    UUID,
                                    primary_key=True, 
                                    default=uuid.uuid4
                                  )
