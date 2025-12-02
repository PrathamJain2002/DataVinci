"""
Database seeder script.
Populates the campaigns table with sample data.
"""

from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Campaign

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)


def seed_campaigns():
    """
    Seeds the database with 10 sample campaigns.
    """
    db: Session = SessionLocal()

    try:
        # Check if campaigns already exist
        existing_campaigns = db.query(Campaign).count()
        if existing_campaigns > 0:
            print(f"Database already contains {existing_campaigns} campaigns. Skipping seed.")
            return

        # Sample campaign data
        sample_campaigns = [
            {
                "name": "Summer Sale 2024",
                "status": "Active",
                "clicks": 15234,
                "cost": 3421.50,
                "impressions": 125000,
            },
            {
                "name": "Black Friday Campaign",
                "status": "Active",
                "clicks": 28456,
                "cost": 6789.25,
                "impressions": 245000,
            },
            {
                "name": "Holiday Special",
                "status": "Paused",
                "clicks": 8923,
                "cost": 2100.75,
                "impressions": 98000,
            },
            {
                "name": "New Product Launch",
                "status": "Active",
                "clicks": 12345,
                "cost": 4567.80,
                "impressions": 156000,
            },
            {
                "name": "Spring Collection",
                "status": "Active",
                "clicks": 18765,
                "cost": 5234.90,
                "impressions": 198000,
            },
            {
                "name": "Back to School",
                "status": "Paused",
                "clicks": 6543,
                "cost": 1890.40,
                "impressions": 72000,
            },
            {
                "name": "Winter Clearance",
                "status": "Active",
                "clicks": 22134,
                "cost": 6123.60,
                "impressions": 234000,
            },
            {
                "name": "Valentine's Day",
                "status": "Paused",
                "clicks": 9876,
                "cost": 2345.20,
                "impressions": 89000,
            },
            {
                "name": "Tech Innovation Week",
                "status": "Active",
                "clicks": 15678,
                "cost": 4456.30,
                "impressions": 167000,
            },
            {
                "name": "End of Year Sale",
                "status": "Active",
                "clicks": 31245,
                "cost": 7890.10,
                "impressions": 289000,
            },
        ]

        # Insert campaigns into database
        for campaign_data in sample_campaigns:
            campaign = Campaign(**campaign_data)
            db.add(campaign)

        # Commit all changes
        db.commit()
        print(f"Successfully seeded {len(sample_campaigns)} campaigns!")

    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    print("Starting database seeding...")
    seed_campaigns()
    print("Database seeding completed!")

