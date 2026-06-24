from datetime import datetime
from typing import Optional

from pydantic import Field, BaseModel, ConfigDict


class CityBase(BaseModel):
    name: str = Field(..., description="City name")
    additional_info: Optional[str] = Field(
        None,
        description="Additional info"
    )


class CityCreate(CityBase):
    pass


class CityUpdate(BaseModel):
    name: Optional[str] = Field(
        default=None, min_length=1,
        max_length=100
    )
    additional_info: Optional[str] = None


class CityResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int


class TemperatureResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    city_id: int
    date_time: datetime
    temperature: float


class TemperatureUpdateResult(BaseModel):
    updated_cities: list[str]
    failed_cities: list[str]
