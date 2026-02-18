from core.database import db
from sqlalchemy.inspection import inspect
from datetime import datetime


class BaseModel(db.Model):
    __abstract__ = True

    def to_dict(self):
        result = {}
        for column in inspect(self).mapper.column_attrs:
            value = getattr(self, column.key)

            if isinstance(value, datetime):
                value = value.isoformat()

            result[column.key] = value

        return result
