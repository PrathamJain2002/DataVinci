"""
SQLAlchemy models for the campaigns database.
"""

from sqlalchemy import Column, Integer, String, Float
from database import Base


class Campaign(Base):
    """
    Campaign model representing a campaign in the database.
    """

    __tablename__ = "campaigns"

    # Primary key
    id = Column(Integer, primary_key=True, index=True)

    # Campaign name
    name = Column(String, nullable=False)

    # Campaign status (Active or Paused)
    status = Column(String, nullable=False)

    # Number of clicks
    clicks = Column(Integer, nullable=False, default=0)

    # Cost in dollars (stored as float/real)
    cost = Column(Float, nullable=False, default=0.0)

    # Number of impressions
    impressions = Column(Integer, nullable=False, default=0)

