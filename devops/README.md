# 🐳 DevOps - Infraestructura y Despliegue

Configuración de infraestructura, CI/CD, y monitoreo.

## 🏗️ Estructura

```
devops/
├── docker/              # Dockerfiles y configuraciones
│   ├── Dockerfile.backend
│   ├── Dockerfile.frontend
│   ├── Dockerfile.data
│   └── init-db.sql
├── kubernetes/          # Manifiestos K8s (futuro)
│   ├── deployment.yml
│   ├── service.yml
│   └── ingress.yml
├── scripts/             # Scripts de automatización
│   ├── deploy.sh
│   ├── backup.sh
│   └── restore.sh
├── monitoring/          # Configuración de monitoreo
│   ├── prometheus.yml
│   └── grafana-dashboards/
└── ci-cd/               # Pipelines CI/CD
    └── github-actions/
```

## 🚀 Inicio Rápido con Docker

### Levantar todos los servicios

```bash
docker-compose up -d
```

### Servicios disponibles

| Servicio | URL | Descripción |
|----------|-----|-------------|
| Frontend | http://localhost:3000 | Interfaz de usuario |
| Backend API | http://localhost:8000 | API REST |
| API Docs | http://localhost:8000/docs | Documentación Swagger |
| Jupyter Lab | http://localhost:8888 | Análisis de datos |
| PgAdmin | http://localhost:5050 | Gestión de BD |
| Prometheus | http://localhost:9090 | Métricas |
| Grafana | http://localhost:3001 | Dashboards de monitoreo |

### Credenciales por defecto

**PgAdmin**
- Email: admin@analytics.com
- Password: admin

**Grafana**
- User: admin
- Password: admin

**PostgreSQL**
- Database: analytics_db
- User: analytics_user
- Password: analytics_pass

## 🐳 Comandos Docker Útiles

### Ver logs

```bash
# Todos los servicios
docker-compose logs -f

# Servicio específico
docker-compose logs -f backend
docker-compose logs -f frontend
```

### Reiniciar servicios

```bash
# Reiniciar todo
docker-compose restart

# Reiniciar servicio específico
docker-compose restart backend
```

### Detener servicios

```bash
# Detener todo
docker-compose down

# Detener y eliminar volúmenes
docker-compose down -v
```

### Reconstruir imágenes

```bash
# Reconstruir todo
docker-compose build

# Reconstruir servicio específico
docker-compose build backend
```

### Ejecutar comandos en contenedores

```bash
# Backend - Crear migraciones
docker-compose exec backend alembic revision --autogenerate -m "Initial migration"

# Backend - Aplicar migraciones
docker-compose exec backend alembic upgrade head

# PostgreSQL - Acceder a psql
docker-compose exec postgres psql -U analytics_user -d analytics_db

# Frontend - Instalar paquete
docker-compose exec frontend npm install <package-name>
```

## 📊 Monitoreo

### Prometheus

Configuración en `monitoring/prometheus.yml`:

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'backend'
    static_configs:
      - targets: ['backend:8000']
```

### Grafana

Dashboards predefinidos en `monitoring/grafana-dashboards/`:

1. **System Overview**: CPU, memoria, disco
2. **API Metrics**: Requests, latency, errores
3. **Database Metrics**: Conexiones, queries, performance

## 🔄 CI/CD con GitHub Actions

### Workflow de CI

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [ develop, main ]
  pull_request:
    branches: [ develop, main ]

jobs:
  backend-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          cd backend
          pip install -r requirements.txt
      - name: Run tests
        run: |
          cd backend
          pytest --cov=. --cov-report=xml
      - name: Upload coverage
        uses: codecov/codecov-action@v3

  frontend-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Node
        uses: actions/setup-node@v3
        with:
          node-version: '20'
      - name: Install dependencies
        run: |
          cd frontend
          npm install
      - name: Run tests
        run: |
          cd frontend
          npm run test
```

## 🚀 Despliegue

### Producción

```bash
# Build para producción
docker-compose -f docker-compose.prod.yml build

# Deploy
docker-compose -f docker-compose.prod.yml up -d
```

### Variables de Entorno

Crear archivo `.env` en la raíz:

```env
# Environment
ENVIRONMENT=production

# Security
SECRET_KEY=your-super-secret-key-here

# Database
DATABASE_URL=postgresql://user:pass@host:5432/db

# Redis
REDIS_URL=redis://host:6379/0

# CORS
CORS_ORIGINS=https://yourdomain.com
```

## 🔐 Seguridad

### Secrets Management

```bash
# Generar SECRET_KEY
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### SSL/TLS

Configurar certificados en `devops/ssl/`:

```
ssl/
├── cert.pem
└── key.pem
```

## 📦 Backup y Restore

### Backup de Base de Datos

```bash
# Ejecutar script de backup
./devops/scripts/backup.sh

# Manual
docker-compose exec postgres pg_dump -U analytics_user analytics_db > backup.sql
```

### Restore

```bash
# Ejecutar script de restore
./devops/scripts/restore.sh backup.sql

# Manual
docker-compose exec -T postgres psql -U analytics_user analytics_db < backup.sql
```

## 📈 Escalabilidad

### Horizontal Scaling

```yaml
# docker-compose.yml
backend:
  deploy:
    replicas: 3
    resources:
      limits:
        cpus: '0.5'
        memory: 512M
```

### Load Balancer (Nginx)

```nginx
upstream backend {
    server backend1:8000;
    server backend2:8000;
    server backend3:8000;
}

server {
    listen 80;
    location / {
        proxy_pass http://backend;
    }
}
```

## 🛠️ Troubleshooting

### Logs

```bash
# Ver logs de errores
docker-compose logs --tail=100 backend | grep ERROR

# Logs en tiempo real
docker-compose logs -f --tail=50
```

### Health Checks

```bash
# Verificar estado de servicios
docker-compose ps

# Health check manual
curl http://localhost:8000/health
```

### Limpiar sistema

```bash
# Eliminar contenedores detenidos
docker container prune

# Eliminar imágenes no usadas
docker image prune

# Eliminar volúmenes no usados
docker volume prune

# Limpiar todo
docker system prune -a --volumes
```

## 🤝 Contribución

1. Crear rama desde `devops`
2. Modificar configuración
3. Probar localmente con Docker
4. Crear Pull Request hacia `devops`
