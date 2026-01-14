# 🚀 Configuración del Backend

## Paso 1: Configurar Variables de Entorno

Copia el archivo `.env.example` a `.env`:

```bash
cp config/.env.example config/.env
```

Luego edita `config/.env` con tus valores. Para desarrollo local, puedes usar:

```env
DATABASE_URL=postgresql://analytics_user:analytics_pass@localhost:5432/analytics_db
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
CORS_ORIGINS=http://localhost:3000,http://localhost:5173
ENVIRONMENT=development
DEBUG=True
```

## Paso 2: Instalar Dependencias

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Paso 3: Crear Base de Datos

Si usas Docker:
```bash
docker-compose up -d postgres
```

O instala PostgreSQL localmente y crea la base de datos:
```sql
CREATE DATABASE analytics_db;
CREATE USER analytics_user WITH PASSWORD 'analytics_pass';
GRANT ALL PRIVILEGES ON DATABASE analytics_db TO analytics_user;
```

## Paso 4: Ejecutar Migraciones

```bash
# Crear migración inicial
alembic revision --autogenerate -m "Initial migration: users and roles tables"

# Aplicar migraciones
alembic upgrade head
```

## Paso 5: Poblar Base de Datos (Seed Data)

```bash
# Crear roles por defecto y usuario admin
python scripts/seed_data.py
```

Esto creará:
- 4 roles: Administrador, Analista, Consultor, Ejecutivo
- Usuario admin: admin@analytics.com / admin123

⚠️ **Importante:** Cambia la contraseña del admin después del primer login.

## Paso 6: Ejecutar Servidor

```bash
uvicorn main:app --reload
```

El servidor estará disponible en:
- API: http://localhost:8000
- Documentación: http://localhost:8000/docs
- Health Check: http://localhost:8000/health

## 🧪 Probar la API

### 1. Registrar un nuevo usuario

```bash
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "test12345",
    "name": "Test User"
  }'
```

### 2. Login

```bash
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin@analytics.com&password=admin123"
```

### 3. Obtener información del usuario actual

```bash
curl -X GET http://localhost:8000/api/v1/auth/me \
  -H "Authorization: Bearer <tu-access-token>"
```
