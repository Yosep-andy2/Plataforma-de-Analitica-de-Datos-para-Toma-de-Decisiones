"""
Role service for business logic.

Handles role-related operations.
"""

from typing import Optional, List
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from models.role import Role


class RoleService:
    """Service class for role operations."""
    
    @staticmethod
    def get_role_by_id(db: Session, role_id: int) -> Optional[Role]:
        """
        Get role by ID.
        
        Args:
            db: Database session
            role_id: Role ID
            
        Returns:
            Role if found, None otherwise
        """
        return db.query(Role).filter(Role.id == role_id).first()
    
    @staticmethod
    def get_role_by_name(db: Session, name: str) -> Optional[Role]:
        """
        Get role by name.
        
        Args:
            db: Database session
            name: Role name
            
        Returns:
            Role if found, None otherwise
        """
        return db.query(Role).filter(Role.name == name).first()
    
    @staticmethod
    def get_all_roles(db: Session) -> List[Role]:
        """
        Get all roles.
        
        Args:
            db: Database session
            
        Returns:
            List of all roles
        """
        return db.query(Role).all()
    
    @staticmethod
    def create_role(db: Session, name: str, description: str = None, permissions: str = None) -> Role:
        """
        Create a new role.
        
        Args:
            db: Database session
            name: Role name
            description: Role description
            permissions: JSON string of permissions
            
        Returns:
            Created role
            
        Raises:
            HTTPException: If role name already exists
        """
        # Check if role already exists
        existing_role = RoleService.get_role_by_name(db, name)
        if existing_role:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Role name already exists"
            )
        
        # Create role
        role = Role(
            name=name,
            description=description,
            permissions=permissions
        )
        
        db.add(role)
        db.commit()
        db.refresh(role)
        
        return role
    
    @staticmethod
    def update_role(db: Session, role_id: int, name: str = None, description: str = None, permissions: str = None) -> Optional[Role]:
        """
        Update role information.
        
        Args:
            db: Database session
            role_id: Role ID
            name: New role name
            description: New description
            permissions: New permissions
            
        Returns:
            Updated role if found, None otherwise
        """
        role = RoleService.get_role_by_id(db, role_id)
        if not role:
            return None
        
        if name is not None:
            role.name = name
        if description is not None:
            role.description = description
        if permissions is not None:
            role.permissions = permissions
        
        db.commit()
        db.refresh(role)
        
        return role
    
    @staticmethod
    def delete_role(db: Session, role_id: int) -> bool:
        """
        Delete role.
        
        Args:
            db: Database session
            role_id: Role ID
            
        Returns:
            True if deleted, False if not found
        """
        role = RoleService.get_role_by_id(db, role_id)
        if not role:
            return False
        
        db.delete(role)
        db.commit()
        
        return True
