# 🧪 Testing - Pruebas y QA

Suite completa de pruebas para garantizar la calidad del sistema.

## 🏗️ Estructura

```
tests/
├── unit/                # Pruebas unitarias
│   ├── backend/
│   ├── frontend/
│   └── data/
├── integration/         # Pruebas de integración
│   ├── api/
│   └── database/
├── e2e/                 # Pruebas End-to-End
│   ├── user-flows/
│   └── scenarios/
├── performance/         # Pruebas de rendimiento
│   ├── load-tests/
│   └── stress-tests/
└── README.md
```

## 🚀 Ejecutar Pruebas

### Backend (Pytest)

```bash
cd backend

# Todas las pruebas
pytest

# Con cobertura
pytest --cov=. --cov-report=html

# Pruebas específicas
pytest tests/test_auth.py -v

# Pruebas por marca
pytest -m "unit"
pytest -m "integration"
```

### Frontend (Vitest)

```bash
cd frontend

# Todas las pruebas
npm run test

# Con UI
npm run test:ui

# Con cobertura
npm run test -- --coverage

# Watch mode
npm run test -- --watch
```

### E2E (Playwright)

```bash
cd frontend

# Todas las pruebas E2E
npm run test:e2e

# Con UI
npm run test:e2e -- --ui

# Modo debug
npm run test:e2e -- --debug

# Navegador específico
npm run test:e2e -- --project=chromium
```

## 📝 Escribir Pruebas

### Backend - Pruebas Unitarias

```python
# tests/unit/backend/test_user_service.py
import pytest
from services.user_service import UserService

@pytest.fixture
def user_service():
    return UserService()

def test_create_user(user_service):
    """Test de creación de usuario."""
    user_data = {
        "email": "test@example.com",
        "password": "SecurePass123!",
        "name": "Test User"
    }
    
    user = user_service.create_user(user_data)
    
    assert user.email == "test@example.com"
    assert user.name == "Test User"
    assert user.password != "SecurePass123!"  # Debe estar hasheada

def test_create_user_duplicate_email(user_service):
    """Test de validación de email duplicado."""
    user_data = {
        "email": "duplicate@example.com",
        "password": "Pass123!",
        "name": "User 1"
    }
    
    user_service.create_user(user_data)
    
    with pytest.raises(ValueError, match="Email already exists"):
        user_service.create_user(user_data)
```

### Backend - Pruebas de Integración

```python
# tests/integration/api/test_auth_api.py
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_login_success():
    """Test de login exitoso."""
    response = client.post("/api/v1/auth/login", json={
        "username": "admin@example.com",
        "password": "admin123"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_invalid_credentials():
    """Test de login con credenciales inválidas."""
    response = client.post("/api/v1/auth/login", json={
        "username": "admin@example.com",
        "password": "wrongpassword"
    })
    
    assert response.status_code == 401
    assert "Incorrect username or password" in response.json()["detail"]
```

### Frontend - Pruebas Unitarias

```typescript
// tests/unit/frontend/components/Button.test.tsx
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { Button } from '@/components/common/Button';

describe('Button Component', () => {
  it('renders button with text', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByText('Click me')).toBeInTheDocument();
  });

  it('calls onClick handler when clicked', () => {
    const handleClick = vi.fn();
    render(<Button onClick={handleClick}>Click me</Button>);
    
    fireEvent.click(screen.getByText('Click me'));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('is disabled when disabled prop is true', () => {
    render(<Button disabled>Click me</Button>);
    expect(screen.getByText('Click me')).toBeDisabled();
  });
});
```

### Frontend - Pruebas E2E

```typescript
// tests/e2e/user-flows/login.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Login Flow', () => {
  test('successful login redirects to dashboard', async ({ page }) => {
    await page.goto('http://localhost:3000/login');
    
    // Llenar formulario
    await page.fill('input[name="email"]', 'admin@example.com');
    await page.fill('input[name="password"]', 'admin123');
    
    // Hacer clic en login
    await page.click('button[type="submit"]');
    
    // Verificar redirección
    await expect(page).toHaveURL('http://localhost:3000/dashboard');
    
    // Verificar que el dashboard se cargó
    await expect(page.locator('h1')).toContainText('Dashboard');
  });

  test('invalid credentials show error message', async ({ page }) => {
    await page.goto('http://localhost:3000/login');
    
    await page.fill('input[name="email"]', 'admin@example.com');
    await page.fill('input[name="password"]', 'wrongpassword');
    await page.click('button[type="submit"]');
    
    // Verificar mensaje de error
    await expect(page.locator('.error-message')).toContainText(
      'Credenciales inválidas'
    );
  });
});
```

## 🎯 Cobertura de Código

### Objetivos

- **Backend**: Mínimo 80% de cobertura
- **Frontend**: Mínimo 70% de cobertura
- **Funciones críticas**: 100% de cobertura

### Generar Reportes

```bash
# Backend
cd backend
pytest --cov=. --cov-report=html
# Abrir: htmlcov/index.html

# Frontend
cd frontend
npm run test -- --coverage
# Abrir: coverage/index.html
```

## ⚡ Pruebas de Rendimiento

### Load Testing con Locust

```python
# tests/performance/load-tests/locustfile.py
from locust import HttpUser, task, between

class AnalyticsPlatformUser(HttpUser):
    wait_time = between(1, 3)
    
    def on_start(self):
        """Login antes de las pruebas."""
        response = self.client.post("/api/v1/auth/login", json={
            "username": "test@example.com",
            "password": "test123"
        })
        self.token = response.json()["access_token"]
        self.headers = {"Authorization": f"Bearer {self.token}"}
    
    @task(3)
    def view_dashboard(self):
        """Simula visualización de dashboard."""
        self.client.get("/api/v1/dashboards/1", headers=self.headers)
    
    @task(2)
    def list_reports(self):
        """Simula listado de reportes."""
        self.client.get("/api/v1/reports", headers=self.headers)
    
    @task(1)
    def generate_report(self):
        """Simula generación de reporte."""
        self.client.post("/api/v1/reports", json={
            "name": "Test Report",
            "type": "sales",
            "date_from": "2024-01-01",
            "date_to": "2024-01-31"
        }, headers=self.headers)
```

### Ejecutar Load Tests

```bash
# Instalar Locust
pip install locust

# Ejecutar pruebas
cd tests/performance/load-tests
locust -f locustfile.py

# Abrir UI: http://localhost:8089
```

## 🔍 Pruebas de Seguridad

### OWASP ZAP

```bash
# Escaneo de seguridad
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t http://localhost:8000
```

### Bandit (Python Security)

```bash
cd backend
bandit -r . -f json -o security-report.json
```

## 📊 Métricas de Calidad

### SonarQube

```bash
# Análisis de código
sonar-scanner \
  -Dsonar.projectKey=analytics-platform \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://localhost:9000
```

## 🤖 CI/CD Integration

### GitHub Actions

```yaml
# .github/workflows/tests.yml
name: Tests

on: [push, pull_request]

jobs:
  backend-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Backend Tests
        run: |
          cd backend
          pip install -r requirements.txt
          pytest --cov=. --cov-report=xml
      
  frontend-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Frontend Tests
        run: |
          cd frontend
          npm install
          npm run test -- --coverage
      
  e2e-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run E2E Tests
        run: |
          docker-compose up -d
          cd frontend
          npm run test:e2e
```

## 📝 Convenciones

### Naming

```python
# Backend
def test_<function_name>_<scenario>():
    """Test description."""
    pass

# Frontend
describe('ComponentName', () => {
  it('should do something when condition', () => {
    // test
  });
});
```

### Estructura AAA

```python
def test_example():
    # Arrange (Preparar)
    user = create_user()
    
    # Act (Actuar)
    result = user.login()
    
    # Assert (Verificar)
    assert result.success is True
```

## 🛠️ Herramientas

- **Backend**: Pytest, Coverage.py, Faker
- **Frontend**: Vitest, Testing Library, Playwright
- **Performance**: Locust, Apache JMeter
- **Security**: OWASP ZAP, Bandit
- **Quality**: SonarQube, ESLint

## 🤝 Contribución

1. Crear rama desde `testing`
2. Escribir pruebas para nuevas features
3. Asegurar cobertura mínima
4. Ejecutar todas las pruebas
5. Crear Pull Request hacia `testing`
