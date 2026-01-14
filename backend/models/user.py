"""
User model for authentication and authorization.

Manages user accounts with role-based access control.
"""

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from core.database import Base


class User(Base):
    """
    User model for authentication and user management.
    
    Attributes:
        id: Primary key
        email: User email (unique, used for login)
        password_hash: Hashed password
        name: User full name
        is_active: Whether user account is active
        is_superuser: Whether user has superuser privileges
        role_id: Foreign key to Role
        created_at: Timestamp of account creation
        updated_at: Timestamp of last update
        last_login: Timestamp of last login
        role: Relationship to Role model
    """
    
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    last_login = Column(DateTime(timezone=True), nullable=True)
    
    # Relationships
    role = relationship("Role", back_populates="users")
    
    def __repr__(self) -> str:
        return f"<User(id={self.id}, email='{self.email}', name='{self.name}')>"
    
    def to_dict(self, include_password: bool = False) -> dict:
        """
        Convert user to dictionary.
        
        Args:
            include_password: Whether to include password hash (default: False)
            
        Returns:
            Dictionary representation of user
        """
        data = {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "is_active": self.is_active,
            "is_superuser": self.is_superuser,
            "role_id": self.role_id,
            "role": self.role.to_dict() if self.role else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "last_login": self.last_login.isoformat() if self.last_login else None,
        }
        
        if include_password:
            data["password_hash"] = self.password_hash
            
        return data
