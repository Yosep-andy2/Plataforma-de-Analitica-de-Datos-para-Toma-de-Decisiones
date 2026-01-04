# Changelog

Todos los cambios notables del proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

## [Unreleased]

### Planeado
- Módulo de análisis predictivo
- Integración con más fuentes de datos
- Aplicación móvil nativa

---

## [1.0.0] - 2026-01-03

### Added
- ✨ Estructura inicial del proyecto
- 📁 Configuración de directorios para todos los módulos
- 🔧 Backend con FastAPI
  - API REST básica
  - Autenticación JWT
  - Integración con PostgreSQL
  - Cache con Redis
- 🎨 Frontend con React + Vite
  - Configuración inicial
  - Material-UI integrado
  - Recharts para visualizaciones
- 📊 Módulo de Data
  - Jupyter Lab configurado
  - Scripts ETL base
  - Notebooks de análisis
- 🧪 Suite de Testing
  - Pytest para backend
  - Vitest para frontend
  - Playwright para E2E
- 🐳 DevOps
  - Docker Compose completo
  - Dockerfiles para todos los servicios
  - Prometheus + Grafana para monitoreo
- 📚 Documentación
  - README completo
  - Documentación técnica
  - Manual de usuario (estructura)
  - Guía de contribución
- 🎨 Design System
  - Paleta de colores
  - Tipografía
  - Componentes UI base

### Infrastructure
- PostgreSQL 16
- Redis 7
- Node.js 20
- Python 3.11

---

## Tipos de Cambios

- `Added` - Para nuevas funcionalidades
- `Changed` - Para cambios en funcionalidades existentes
- `Deprecated` - Para funcionalidades que serán eliminadas
- `Removed` - Para funcionalidades eliminadas
- `Fixed` - Para corrección de bugs
- `Security` - Para vulnerabilidades de seguridad

---

[Unreleased]: https://github.com/tu-org/analytics-platform/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/tu-org/analytics-platform/releases/tag/v1.0.0
