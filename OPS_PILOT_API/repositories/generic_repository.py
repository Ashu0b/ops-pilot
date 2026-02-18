import logging
from sqlalchemy import select
from sqlalchemy.orm import Session
from werkzeug.exceptions import InternalServerError
from typing import Any, Generic, List, Optional, Type, TypeVar

T = TypeVar("T")
logger = logging.getLogger(__name__)


class GenericViewRepo(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    def get_all(
        self,
        session: Session,
        columns: Optional[List[str]] = None,
    ) -> List[Any]:
        try:
            stmt = select(*self._get_select_columns(columns))
            results = session.execute(stmt)
            return results.scalars().all() if not columns else results.all()
        except Exception as e:
            logger.error(
                "Get all on model: %s failed due to an error: %s",
                self.model.__name__,
                e,
                exc_info=True,
            )
            raise InternalServerError(
                description=f"failed fetch for {self.model.__name__}")

    def _get_select_columns(self, columns: Optional[List[str]]) -> List[Any]:
        if columns:
            return [getattr(self.model, col) for col in columns if hasattr(self.model, col)]
        return [self.model]


class GenericRepo(GenericViewRepo[T]):
    def create(self, session: Session, instance: T, commit_immediately: bool = False) -> T:
        try:
            session.add(instance)
            session.flush()
            if commit_immediately:
                session.commit()
            return instance
        except Exception as e:
            session.rollback()
            logger.error(f"Create failed for {self.model.__name__}: {e}")
            raise
