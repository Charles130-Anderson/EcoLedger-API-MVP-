from pydantic import BaseModel

class CreditBase(BaseModel):
    project_name: str
    token_id: str
    location: str
    certification: str
    co2_offset_tonnes: int
    price_per_ton: float
    project_type: str
    impact_summary: str

class CreditCreate(CreditBase):
    pass

class Credit(CreditBase):
    id: int

    class Config:
        from_attributes = True