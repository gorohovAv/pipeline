from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class Pipelines(Base):
    __tablename__ = "pipelines"

    id = Column(primary_key = True)
    pipelime_name = Column(String, index="true")
    pipeline_content = Column(String)
