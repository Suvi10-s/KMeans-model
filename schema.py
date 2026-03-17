from pydantic import BaseModel

class Features(BaseModel):
    age:int
    annual_income:int
    spending_score:int
    gender_female:int
    gender_male:int
    region_East:int
    region_North:int
    region_South:int
    region_West:int