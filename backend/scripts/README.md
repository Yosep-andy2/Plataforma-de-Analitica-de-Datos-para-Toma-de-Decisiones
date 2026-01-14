# 🌱 Seed Data - Instrucciones

Este script crea los datos iniciales necesarios para el sistema.

## ¿Qué crea?

### Roles por Defecto

1. **Administrador**
   - Acceso completo al sistema
   - Puede gestionar usuarios, configuraciones y todos los módulos

2. **Analista**
   - Puede crear y gestionar dashboards, reportes y análisis de datos
   - No puede gestionar usuarios

3. **Consultor**
   - Puede visualizar dashboards y generar reportes
   - Sin capacidad de edición

4. **Ejecutivo**
   - Acceso de solo lectura a dashboards ejecutivos
   - Puede exportar reportes

### Usuario Administrador

- **Email:** admin@analytics.com
- **Password:** admin123
- **Rol:** Administrador
- **Permisos:** Superusuario

## 🚀 Cómo Ejecutar

### Opción 1: Desde la raíz del backend

```bash
cd backend
python scripts/seed_data.py
```

### Opción 2: Usando Python directamente

```bash
cd backend
python -m scripts.seed_data
```

## ⚠️ Importante

1. **Ejecutar solo una vez**: Este script verifica si los datos ya existen antes de crearlos
2. **Cambiar contraseña**: Después del primer login, cambia la contraseña del admin
3. **Migraciones primero**: Asegúrate de ejecutar las migraciones de Alembic antes:
   ```bash
   alembic upgrade head
   ```

## 📋 Salida Esperada

```
============================================================
SEEDING DATABASE WITH INITIAL DATA
============================================================

1. Creating database tables...
✓ Tables created/verified

2. Creating default roles...
✓ Created role: Administrador
✓ Created role: Analista
✓ Created role: Consultor
✓ Created role: Ejecutivo

3. Creating admin user...
✓ Created admin user: admin@analytics.com
  Default password: admin123
  ⚠️  IMPORTANT: Change this password after first login!

============================================================
DATABASE SEEDING COMPLETED SUCCESSFULLY!
============================================================

📊 Summary:
  - Roles created: 4
  - Admin user: admin@analytics.com

🔐 Login credentials:
  Email: admin@analytics.com
  Password: admin123

⚠️  Remember to change the admin password!
============================================================
```

## 🔄 Re-ejecutar el Script

Si ejecutas el script nuevamente, verás:

```
✓ Role 'Administrador' already exists
✓ Role 'Analista' already exists
✓ Role 'Consultor' already exists
✓ Role 'Ejecutivo' already exists
✓ Admin user already exists: admin@analytics.com
```

El script es **idempotente**: puede ejecutarse múltiples veces sin crear duplicados.
