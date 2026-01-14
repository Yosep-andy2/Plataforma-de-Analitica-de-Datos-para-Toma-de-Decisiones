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

## Paso 5: Ejecutar Servidor

```bash
uvicorn main:app --reload
```

El servidor estará disponible en:
- API: http://localhost:8000
- Documentación: http://localhost:8000/docs
- Health Check: http://localhost:8000/health
