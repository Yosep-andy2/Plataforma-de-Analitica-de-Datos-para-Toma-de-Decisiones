"""
Seed data script.

Populates database with initial data:
- Default roles (Administrador, Analista, Consultor, Ejecutivo)
- Default admin user
"""

import sys
from pathlib import Path

# Add parent directory to path to import modules
sys.path.append(str(Path(__file__).parent.parent))

from sqlalchemy.orm import Session
from core.database import SessionLocal, engine, Base
from core.security import hash_password
from models.user import User
from models.role import Role


def create_roles(db: Session) -> dict[str, Role]:
    """
    Create default roles.
    
    Returns:
        Dictionary mapping role names to Role objects
    """
    roles_data = [
        {
            "name": "Administrador",
            "description": "Acceso completo al sistema. Puede gestionar usuarios, configuraciones y todos los módulos.",
            "permissions": '["users.create", "users.read", "users.update", "users.delete", "dashboards.create", "dashboards.read", "dashboards.update", "dashboards.delete", "reports.create", "reports.read", "reports.update", "reports.delete", "data_sources.create", "data_sources.read", "data_sources.update", "data_sources.delete", "settings.manage"]'
        },
        {
            "name": "Analista",
            "description": "Puede crear y gestionar dashboards, reportes y análisis de datos.",
            "permissions": '["dashboards.create", "dashboards.read", "dashboards.update", "dashboards.delete", "reports.create", "reports.read", "reports.update", "reports.delete", "data_sources.read"]'
        },
        {
            "name": "Consultor",
            "description": "Puede visualizar dashboards y generar reportes, sin capacidad de edición.",
            "permissions": '["dashboards.read", "reports.create", "reports.read", "reports.export"]'
        },
        {
            "name": "Ejecutivo",
            "description": "Acceso de solo lectura a dashboards ejecutivos y reportes estratégicos.",
            "permissions": '["dashboards.read", "reports.read", "reports.export"]'
        }
    ]
    
    roles = {}
    for role_data in roles_data:
        # Check if role already exists
        existing_role = db.query(Role).filter(Role.name == role_data["name"]).first()
        
        if existing_role:
            print(f"✓ Role '{role_data['name']}' already exists")
            roles[role_data["name"]] = existing_role
        else:
            role = Role(**role_data)
            db.add(role)
            db.commit()
            db.refresh(role)
            roles[role_data["name"]] = role
            print(f"✓ Created role: {role_data['name']}")
    
    return roles


def create_admin_user(db: Session, admin_role: Role) -> User:
    """
    Create default admin user.
    
    Args:
        db: Database session
        admin_role: Admin role object
        
    Returns:
        Created admin user
    """
    admin_email = "admin@analytics.com"
    
    # Check if admin already exists
    existing_admin = db.query(User).filter(User.email == admin_email).first()
    
    if existing_admin:
        print(f"✓ Admin user already exists: {admin_email}")
        return existing_admin
    
    # Create admin user
    admin_user = User(
        email=admin_email,
        name="Administrador del Sistema",
        password_hash=hash_password("admin123"),  # Default password
        role_id=admin_role.id,
        is_active=True,
        is_superuser=True
    )
    
    db.add(admin_user)
    db.commit()
    db.refresh(admin_user)
    
    print(f"✓ Created admin user: {admin_email}")
    print(f"  Default password: admin123")
    print(f"  ⚠️  IMPORTANT: Change this password after first login!")
    
    return admin_user


def seed_database():
    """Main function to seed the database."""
    print("=" * 60)
    print("SEEDING DATABASE WITH INITIAL DATA")
    print("=" * 60)
    
    # Create tables if they don't exist
    print("\n1. Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✓ Tables created/verified")
    
    # Create database session
    db = SessionLocal()
    
    try:
        # Create roles
        print("\n2. Creating default roles...")
        roles = create_roles(db)
        
        # Create admin user
        print("\n3. Creating admin user...")
        admin_user = create_admin_user(db, roles["Administrador"])
        
        print("\n" + "=" * 60)
        print("DATABASE SEEDING COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        print("\n📊 Summary:")
        print(f"  - Roles created: {len(roles)}")
        print(f"  - Admin user: {admin_user.email}")
        print("\n🔐 Login credentials:")
        print(f"  Email: {admin_user.email}")
        print(f"  Password: admin123")
        print("\n⚠️  Remember to change the admin password!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Error seeding database: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
