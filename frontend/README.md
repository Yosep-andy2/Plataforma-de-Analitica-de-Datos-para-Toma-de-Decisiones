# 🎨 Frontend - Dashboards y Visualizaciones

Interfaz de usuario para la Plataforma de Analítica de Datos.

## 🏗️ Arquitectura

```
frontend/
├── public/              # Archivos estáticos
│   ├── favicon.ico
│   └── logo.png
├── src/
│   ├── components/      # Componentes reutilizables
│   │   ├── common/      # Botones, inputs, modales
│   │   ├── charts/      # Gráficos y visualizaciones
│   │   ├── layout/      # Header, Sidebar, Footer
│   │   └── dashboard/   # Componentes de dashboards
│   ├── pages/           # Páginas de la aplicación
│   │   ├── Login.tsx
│   │   ├── Dashboard.tsx
│   │   ├── Reports.tsx
│   │   ├── DataSources.tsx
│   │   └── Settings.tsx
│   ├── services/        # Servicios API
│   │   ├── api.ts
│   │   ├── auth.ts
│   │   ├── dashboards.ts
│   │   └── reports.ts
│   ├── store/           # Estado global (Zustand)
│   │   ├── authStore.ts
│   │   ├── dashboardStore.ts
│   │   └── uiStore.ts
│   ├── styles/          # Estilos globales
│   │   ├── theme.ts
│   │   ├── global.css
│   │   └── variables.css
│   ├── utils/           # Utilidades
│   │   ├── formatters.ts
│   │   ├── validators.ts
│   │   └── constants.ts
│   ├── types/           # TypeScript types
│   │   ├── api.ts
│   │   └── models.ts
│   ├── hooks/           # Custom hooks
│   │   ├── useAuth.ts
│   │   ├── useDashboard.ts
│   │   └── useApi.ts
│   ├── App.tsx          # Componente principal
│   ├── main.tsx         # Punto de entrada
│   └── vite-env.d.ts
├── tests/               # Pruebas
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── .env.example         # Variables de entorno ejemplo
├── package.json
├── tsconfig.json
├── vite.config.ts
└── README.md
```

## 🚀 Instalación

### 1. Instalar dependencias

```bash
npm install
```

### 2. Configurar variables de entorno

```bash
cp .env.example .env
# Editar .env con la URL de tu backend
```

### 3. Ejecutar en modo desarrollo

```bash
npm run dev
```

La aplicación estará disponible en: http://localhost:5173

## 🎨 Componentes Principales

### Layout Components

#### Header
```tsx
import { Header } from '@/components/layout/Header';

<Header 
  user={currentUser} 
  onLogout={handleLogout}
/>
```

#### Sidebar
```tsx
import { Sidebar } from '@/components/layout/Sidebar';

<Sidebar 
  items={menuItems}
  activeItem={activeRoute}
/>
```

### Chart Components

#### LineChart
```tsx
import { LineChart } from '@/components/charts/LineChart';

<LineChart
  data={salesData}
  xKey="date"
  yKey="amount"
  title="Ventas Mensuales"
/>
```

#### BarChart
```tsx
import { BarChart } from '@/components/charts/BarChart';

<BarChart
  data={revenueData}
  xKey="category"
  yKey="revenue"
  color="#3b82f6"
/>
```

### Dashboard Components

#### DashboardGrid
```tsx
import { DashboardGrid } from '@/components/dashboard/DashboardGrid';

<DashboardGrid
  widgets={widgets}
  onWidgetUpdate={handleUpdate}
  editable={true}
/>
```

## 🔐 Autenticación

El sistema utiliza JWT almacenado en localStorage:

```tsx
import { useAuth } from '@/hooks/useAuth';

function MyComponent() {
  const { user, login, logout, isAuthenticated } = useAuth();

  const handleLogin = async (credentials) => {
    await login(credentials);
  };

  return (
    <div>
      {isAuthenticated ? (
        <p>Bienvenido, {user.name}</p>
      ) : (
        <LoginForm onSubmit={handleLogin} />
      )}
    </div>
  );
}
```

## 📊 Gestión de Estado

Utilizamos Zustand para estado global:

```tsx
// store/dashboardStore.ts
import { create } from 'zustand';

interface DashboardStore {
  dashboards: Dashboard[];
  currentDashboard: Dashboard | null;
  setDashboards: (dashboards: Dashboard[]) => void;
  setCurrentDashboard: (dashboard: Dashboard) => void;
}

export const useDashboardStore = create<DashboardStore>((set) => ({
  dashboards: [],
  currentDashboard: null,
  setDashboards: (dashboards) => set({ dashboards }),
  setCurrentDashboard: (dashboard) => set({ currentDashboard: dashboard }),
}));
```

## 🎨 Tema y Estilos

### Material-UI Theme

```tsx
// styles/theme.ts
import { createTheme } from '@mui/material/styles';

export const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
  },
  typography: {
    fontFamily: '"Inter", "Roboto", "Helvetica", "Arial", sans-serif',
  },
});
```

### Uso del tema

```tsx
import { ThemeProvider } from '@mui/material/styles';
import { theme } from '@/styles/theme';

function App() {
  return (
    <ThemeProvider theme={theme}>
      <YourApp />
    </ThemeProvider>
  );
}
```

## 🧪 Testing

### Unit Tests (Vitest)

```bash
# Ejecutar tests
npm run test

# Con UI
npm run test:ui

# Con cobertura
npm run test -- --coverage
```

### E2E Tests (Playwright)

```bash
# Ejecutar tests E2E
npm run test:e2e

# En modo UI
npm run test:e2e -- --ui
```

## 📦 Build para Producción

```bash
# Generar build optimizado
npm run build

# Preview del build
npm run preview
```

Los archivos se generarán en la carpeta `dist/`.

## 🌐 Variables de Entorno

Crear archivo `.env`:

```env
VITE_API_URL=http://localhost:8000/api/v1
VITE_APP_NAME=Plataforma de Analítica
VITE_ENABLE_ANALYTICS=true
```

Uso en código:

```tsx
const apiUrl = import.meta.env.VITE_API_URL;
```

## 📱 Responsive Design

Breakpoints utilizados:

```tsx
const breakpoints = {
  xs: '0px',      // Mobile
  sm: '600px',    // Tablet
  md: '900px',    // Desktop pequeño
  lg: '1200px',   // Desktop
  xl: '1536px',   // Desktop grande
};
```

## 🎯 Páginas Principales

### Dashboard
- Vista general con KPIs principales
- Gráficos interactivos
- Filtros de fecha y categoría

### Reports
- Listado de reportes
- Generación de reportes personalizados
- Exportación (PDF, Excel, CSV)

### Data Sources
- Gestión de fuentes de datos
- Configuración de conexiones
- Sincronización manual/automática

### Settings
- Configuración de perfil
- Preferencias de usuario
- Gestión de notificaciones

## 🛠️ Stack Tecnológico

- **Framework**: React 18 + TypeScript
- **Build Tool**: Vite 5
- **UI Library**: Material-UI 5
- **Charts**: Recharts + D3.js
- **State Management**: Zustand
- **Data Fetching**: TanStack Query (React Query)
- **Forms**: React Hook Form + Zod
- **Routing**: React Router v6
- **HTTP Client**: Axios
- **Animations**: Framer Motion
- **Testing**: Vitest + Playwright

## 📝 Convenciones de Código

### Naming Conventions

```tsx
// Componentes: PascalCase
export const DashboardCard = () => { ... };

// Hooks: camelCase con prefijo 'use'
export const useDashboard = () => { ... };

// Constantes: UPPER_SNAKE_CASE
export const API_BASE_URL = '...';

// Funciones: camelCase
export const formatCurrency = (value: number) => { ... };
```

### File Structure

```tsx
// Cada componente en su propia carpeta
components/
  DashboardCard/
    DashboardCard.tsx
    DashboardCard.test.tsx
    DashboardCard.styles.ts
    index.ts
```

## 🤝 Contribución

1. Crear rama desde `frontend`
2. Implementar cambios con tests
3. Ejecutar linters: `npm run lint:fix`
4. Ejecutar tests: `npm run test`
5. Crear Pull Request hacia `frontend`

## 🔗 Enlaces Útiles

- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)
- [Material-UI](https://mui.com/)
- [Recharts](https://recharts.org/)
- [TanStack Query](https://tanstack.com/query/latest)
