"""
FastAPI main application file.
Configures the FastAPI app, CORS, and includes routers.
"""

import os
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
# Get allowed origins from environment variable, fallback to defaults
# In Railway/Render, set ALLOWED_ORIGINS environment variable like:
# ALLOWED_ORIGINS=http://localhost:3000,https://your-app.vercel.app,https://*.vercel.app
allowed_origins_env = os.getenv("ALLOWED_ORIGINS", "")

if allowed_origins_env:
    # Split by comma and strip whitespace
    origins = [origin.strip() for origin in allowed_origins_env.split(",")]
else:
    # Default origins for development
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

