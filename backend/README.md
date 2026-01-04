# 🔧 Backend - API REST

API REST para la Plataforma de Analítica de Datos.

## 🏗️ Arquitectura

```
backend/
├── api/              # Endpoints REST
│   ├── v1/           # Versión 1 de la API
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── dashboards.py
│   │   ├── reports.py
│   │   └── data_sources.py
│   └── dependencies.py
├── auth/             # Autenticación y autorización
│   ├── jwt.py
│   ├── oauth2.py
│   └── permissions.py
├── core/             # Configuración central
│   ├── config.py
│   ├── database.py
│   ├── security.py
│   └── logging.py
├── integrations/     # Conectores a fuentes de datos
│   ├── sql_connector.py
│   ├── csv_connector.py
│   ├── api_connector.py
│   └── excel_connector.py
├── models/           # Modelos de datos (ORM)
│   ├── user.py
│   ├── dashboard.py
│   ├── report.py
│   └── data_source.py
├── services/         # Lógica de negocio
│   ├── user_service.py
│   ├── dashboard_service.py
│   ├── report_service.py
│   └── analytics_service.py
├── utils/            # Utilidades compartidas
│   ├── validators.py
│   ├── formatters.py
│   └── helpers.py
├── tests/            # Pruebas del backend
│   ├── test_auth.py
│   ├── test_api.py
│   └── test_services.py
├── config/           # Archivos de configuración
│   ├── .env.example
│   └── settings.py
├── main.py           # Punto de entrada de la aplicación
└── requirements.txt  # Dependencias Python
```

## 🚀 Instalación

### 1. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar variables de entorno

```bash
cp config/.env.example config/.env
# Editar config/.env con tus credenciales
```

### 4. Inicializar base de datos

```bash
alembic upgrade head
```

### 5. Ejecutar servidor de desarrollo

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 📚 Documentación API

Una vez iniciado el servidor, accede a:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## 🧪 Testing

```bash
# Ejecutar todas las pruebas
pytest

# Con cobertura
pytest --cov=. --cov-report=html

# Pruebas específicas
pytest tests/test_auth.py -v
```

## 🔐 Autenticación

El sistema utiliza JWT (JSON Web Tokens) para autenticación:

```python
# Ejemplo de login
POST /api/v1/auth/login
{
  "username": "usuario@empresa.com",
  "password": "contraseña"
}

# Respuesta
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer",
  "expires_in": 3600
}
```

## 📊 Endpoints Principales

### Autenticación
- `POST /api/v1/auth/login` - Iniciar sesión
- `POST /api/v1/auth/register` - Registrar usuario
- `POST /api/v1/auth/refresh` - Refrescar token
- `POST /api/v1/auth/logout` - Cerrar sesión

### Usuarios
- `GET /api/v1/users/me` - Obtener perfil actual
- `GET /api/v1/users` - Listar usuarios (Admin)
- `PUT /api/v1/users/{id}` - Actualizar usuario
- `DELETE /api/v1/users/{id}` - Eliminar usuario

### Dashboards
- `GET /api/v1/dashboards` - Listar dashboards
- `POST /api/v1/dashboards` - Crear dashboard
- `GET /api/v1/dashboards/{id}` - Obtener dashboard
- `PUT /api/v1/dashboards/{id}` - Actualizar dashboard
- `DELETE /api/v1/dashboards/{id}` - Eliminar dashboard

### Reportes
- `GET /api/v1/reports` - Listar reportes
- `POST /api/v1/reports` - Generar reporte
- `GET /api/v1/reports/{id}` - Obtener reporte
- `GET /api/v1/reports/{id}/export` - Exportar reporte (PDF/Excel)

### Fuentes de Datos
- `GET /api/v1/data-sources` - Listar fuentes
- `POST /api/v1/data-sources` - Conectar fuente
- `GET /api/v1/data-sources/{id}/test` - Probar conexión
- `POST /api/v1/data-sources/{id}/sync` - Sincronizar datos

## 🗄️ Base de Datos

### Modelos Principales

- **User**: Usuarios del sistema
- **Role**: Roles y permisos
- **Dashboard**: Dashboards personalizados
- **Report**: Reportes generados
- **DataSource**: Fuentes de datos conectadas
- **Widget**: Widgets de visualización
- **Alert**: Alertas configuradas

### Migraciones

```bash
# Crear nueva migración
alembic revision --autogenerate -m "Descripción del cambio"

# Aplicar migraciones
alembic upgrade head

# Revertir última migración
alembic downgrade -1
```

## 🔧 Configuración

Variables de entorno en `config/.env`:

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/analytics_db

# Redis
REDIS_URL=redis://localhost:6379/0

# Security
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
CORS_ORIGINS=http://localhost:3000,http://localhost:5173

# Environment
ENVIRONMENT=development
DEBUG=True
```

## 📈 Monitoreo

Métricas de Prometheus disponibles en:
- http://localhost:8000/metrics

## 🛠️ Stack Tecnológico

- **Framework**: FastAPI 0.109
- **ORM**: SQLAlchemy 2.0
- **Database**: PostgreSQL 14+
- **Cache**: Redis 7+
- **Authentication**: JWT (python-jose)
- **Validation**: Pydantic v2
- **Testing**: Pytest
- **Documentation**: OpenAPI 3.0

## 📝 Convenciones de Código

- **Estilo**: PEP 8 (enforced by Black)
- **Type Hints**: Obligatorio en todas las funciones
- **Docstrings**: Google Style
- **Imports**: Organizados con isort

```python
# Ejemplo de función bien documentada
async def get_user_by_id(user_id: int, db: Session) -> User:
    """
    Obtiene un usuario por su ID.

    Args:
        user_id: ID del usuario a buscar
        db: Sesión de base de datos

    Returns:
        Usuario encontrado

    Raises:
        HTTPException: Si el usuario no existe
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user
```

## 🤝 Contribución

1. Crear rama desde `backend`
2. Implementar cambios con tests
3. Ejecutar linters: `black . && flake8 && mypy .`
4. Ejecutar tests: `pytest`
5. Crear Pull Request hacia `backend`
