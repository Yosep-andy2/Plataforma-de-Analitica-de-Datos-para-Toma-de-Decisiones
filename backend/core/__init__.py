"""
Core module for backend application.

This module contains core functionality including:
- Configuration management
- Database connection
- Security utilities
"""

from .config import settings
from .database import get_db, engine, SessionLocal

__all__ = ["settings", "get_db", "engine", "SessionLocal"]
