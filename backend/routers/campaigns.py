"""
Campaign router - handles all campaign-related endpoints.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import Campaign
from schemas import Campaign as CampaignSchema

# Create router
router = APIRouter(prefix="/campaigns", tags=["campaigns"])


@router.get("", response_model=List[CampaignSchema])
def get_campaigns(db: Session = Depends(get_db)):
    """
    GET /campaigns
    
    Returns a list of all campaigns from the database.
    
    Returns:
        List[CampaignSchema]: List of all campaigns
    """
    try:
        # Query all campaigns from database
        campaigns = db.query(Campaign).all()
        
        # Return campaigns (empty list if none found)
        return campaigns
    except Exception as e:
        # Handle any database errors
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching campaigns: {str(e)}"
        )

