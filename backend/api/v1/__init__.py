"""
API v1 package.

Contains all API v1 endpoints.
"""

from fastapi import APIRouter
from .auth import router as auth_router

# Create main API router
api_router = APIRouter(prefix="/api/v1")

# Include sub-routers
api_router.include_router(auth_router, prefix="/auth", tags=["Authentication"])

__all__ = ["api_router"]
