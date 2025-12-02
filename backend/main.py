"""
FastAPI main application file.
Configures the FastAPI app, CORS, and includes routers.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import campaigns

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Campaign Analytics API",
    description="Backend API for Grippi's Campaign Analytics Dashboard",
    version="1.0.0",
)

# Configure CORS
# In production, replace "*" with your Vercel domain
# Example: origins = ["https://your-app.vercel.app"]
origins = [
    "http://localhost:3000",  # Next.js dev server
    "http://localhost:3001",  # Alternative port
    "https://*.vercel.app",   # Vercel preview deployments
    "*",  # Allow all origins (for development - restrict in production)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(campaigns.router)


@app.get("/")
def root():
    """
    Root endpoint - health check.
    """
    return {
        "message": "Campaign Analytics API is running",
        "version": "1.0.0",
        "endpoints": {
            "campaigns": "/campaigns"
        }
    }


@app.get("/health")
def health_check():
    """
    Health check endpoint.
    """
    return {"status": "healthy"}

