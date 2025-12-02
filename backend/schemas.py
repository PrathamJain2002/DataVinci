"""
Pydantic schemas for request/response validation.
"""

from pydantic import BaseModel


class CampaignBase(BaseModel):
    """Base schema for Campaign with common fields."""

    name: str
    status: str
    clicks: int
    cost: float
    impressions: int


class CampaignCreate(CampaignBase):
    """Schema for creating a new campaign."""

    pass


class Campaign(CampaignBase):
    """Schema for Campaign response (includes id)."""

    id: int

    class Config:
        from_attributes = True

