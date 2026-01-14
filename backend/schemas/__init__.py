"""
Pydantic schemas for request/response validation.

Defines data models for API requests and responses.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


# ============================================
# USER SCHEMAS
# ============================================

class UserBase(BaseModel):
    """Base user schema with common fields."""
    email: EmailStr
    name: str = Field(..., min_length=1, max_length=255)


class UserCreate(UserBase):
    """Schema for user creation."""
    password: str = Field(..., min_length=8, max_length=100)
    role_id: Optional[int] = None


class UserUpdate(BaseModel):
    """Schema for user update."""
    email: Optional[EmailStr] = None
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    password: Optional[str] = Field(None, min_length=8, max_length=100)
    role_id: Optional[int] = None
    is_active: Optional[bool] = None


class UserResponse(UserBase):
    """Schema for user response."""
    id: int
    is_active: bool
    is_superuser: bool
    role_id: Optional[int]
    created_at: datetime
    updated_at: Optional[datetime]
    last_login: Optional[datetime]
    
    class Config:
        from_attributes = True


# ============================================
# ROLE SCHEMAS
# ============================================

class RoleBase(BaseModel):
    """Base role schema."""
    name: str = Field(..., min_length=1, max_length=50)
    description: Optional[str] = None
    permissions: Optional[str] = None


class RoleCreate(RoleBase):
    """Schema for role creation."""
    pass


class RoleUpdate(BaseModel):
    """Schema for role update."""
    name: Optional[str] = Field(None, min_length=1, max_length=50)
    description: Optional[str] = None
    permissions: Optional[str] = None


class RoleResponse(RoleBase):
    """Schema for role response."""
    id: int
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attributes = True


# ============================================
# AUTH SCHEMAS
# ============================================

class Token(BaseModel):
    """Schema for token response."""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int


class TokenRefresh(BaseModel):
    """Schema for token refresh request."""
    refresh_token: str


class LoginRequest(BaseModel):
    """Schema for login request."""
    username: EmailStr  # Using email as username
    password: str


class RegisterRequest(UserCreate):
    """Schema for registration request."""
    pass
