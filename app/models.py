from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Credit(Base):
    __tablename__ = "credits"

    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String, nullable=False)
    token_id = Column(String, unique=True, index=True, nullable=False)
    location = Column(String, nullable=False)
    certification = Column(String, nullable=False)
    co2_offset_tonnes = Column(Integer, nullable=False)
    price_per_ton = Column(Float, nullable=False)
    project_type = Column(String, nullable=False)
    impact_summary = Column(String, nullable=False)
