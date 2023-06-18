from datetime import datetime

from sqlalchemy import Column, String, DateTime

from typing import Optional

from enum import Enum

from pydantic import BaseModel


class APPBaseModel:
    def class_name(self):
        return self.__class__.__name__


class APPDataBaseModel(APPBaseModel):
    created_at = Column(DateTime, default=datetime.now)
    created_by = Column(String)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    updated_by = Column(String)


class OrderByModel(str, Enum):
    ascending = "ASC"
    descening = "DESC"


class Visualization(BaseModel):
    order_by: Optional[str] = "id"
    order_by_dir: Optional[OrderByModel] = OrderByModel.descening
    quick_filter: Optional[bool] = False
