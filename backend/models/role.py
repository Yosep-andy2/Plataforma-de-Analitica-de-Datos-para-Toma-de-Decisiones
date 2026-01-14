"""
Role model for user authorization.

Defines user roles: Administrador, Analista, Consultor, Ejecutivo.
"""

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from core.database import Base


class Role(Base):
    """
    Role model for role-based access control (RBAC).
    
    Attributes:
        id: Primary key
        name: Role name (unique)
        description: Role description
        permissions: JSON string of permissions
        created_at: Timestamp of creation
        updated_at: Timestamp of last update
        users: Relationship to User model
    """
    
    __tablename__ = "roles"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    permissions = Column(Text, nullable=True)  # JSON string of permissions
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    
    # Relationships
    users = relationship("User", back_populates="role")
    
    def __repr__(self) -> str:
        return f"<Role(id={self.id}, name='{self.name}')>"
    
    def to_dict(self) -> dict:
        """Convert role to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "permissions": self.permissions,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
