# 🎨 Design - UX/UI

Recursos de diseño, wireframes, mockups y guías de estilo.

## 🏗️ Estructura

```
design/
├── wireframes/          # Wireframes de baja fidelidad
│   ├── login.png
│   ├── dashboard.png
│   ├── reports.png
│   └── settings.png
├── mockups/             # Mockups de alta fidelidad
│   ├── desktop/
│   ├── tablet/
│   └── mobile/
├── prototypes/          # Prototipos interactivos
│   └── figma-links.md
├── assets/              # Assets de diseño
│   ├── icons/
│   ├── images/
│   ├── logos/
│   └── fonts/
├── style-guide/         # Guía de estilos
│   ├── colors.md
│   ├── typography.md
│   ├── components.md
│   └── spacing.md
└── README.md
```

## 🎨 Guía de Estilos

### Paleta de Colores

#### Colores Principales

```css
/* Primary - Azul */
--primary-50: #E3F2FD;
--primary-100: #BBDEFB;
--primary-200: #90CAF9;
--primary-300: #64B5F6;
--primary-400: #42A5F5;
--primary-500: #2196F3;  /* Main */
--primary-600: #1E88E5;
--primary-700: #1976D2;
--primary-800: #1565C0;
--primary-900: #0D47A1;

/* Secondary - Verde */
--secondary-50: #E8F5E9;
--secondary-100: #C8E6C9;
--secondary-200: #A5D6A7;
--secondary-300: #81C784;
--secondary-400: #66BB6A;
--secondary-500: #4CAF50;  /* Main */
--secondary-600: #43A047;
--secondary-700: #388E3C;
--secondary-800: #2E7D32;
--secondary-900: #1B5E20;
```

#### Colores de Estado

```css
/* Success */
--success: #4CAF50;
--success-light: #81C784;
--success-dark: #388E3C;

/* Warning */
--warning: #FF9800;
--warning-light: #FFB74D;
--warning-dark: #F57C00;

/* Error */
--error: #F44336;
--error-light: #E57373;
--error-dark: #D32F2F;

/* Info */
--info: #2196F3;
--info-light: #64B5F6;
--info-dark: #1976D2;
```

#### Colores Neutrales

```css
/* Grises */
--gray-50: #FAFAFA;
--gray-100: #F5F5F5;
--gray-200: #EEEEEE;
--gray-300: #E0E0E0;
--gray-400: #BDBDBD;
--gray-500: #9E9E9E;
--gray-600: #757575;
--gray-700: #616161;
--gray-800: #424242;
--gray-900: #212121;

/* Blanco y Negro */
--white: #FFFFFF;
--black: #000000;
```

### Tipografía

#### Fuentes

```css
/* Fuente Principal */
--font-family-primary: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

/* Fuente Monospace (Código) */
--font-family-mono: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
```

#### Tamaños de Fuente

```css
/* Headings */
--font-size-h1: 2.5rem;    /* 40px */
--font-size-h2: 2rem;      /* 32px */
--font-size-h3: 1.75rem;   /* 28px */
--font-size-h4: 1.5rem;    /* 24px */
--font-size-h5: 1.25rem;   /* 20px */
--font-size-h6: 1rem;      /* 16px */

/* Body */
--font-size-base: 1rem;    /* 16px */
--font-size-sm: 0.875rem;  /* 14px */
--font-size-xs: 0.75rem;   /* 12px */

/* Large */
--font-size-lg: 1.125rem;  /* 18px */
--font-size-xl: 1.25rem;   /* 20px */
```

#### Pesos de Fuente

```css
--font-weight-light: 300;
--font-weight-regular: 400;
--font-weight-medium: 500;
--font-weight-semibold: 600;
--font-weight-bold: 700;
```

### Espaciado

```css
/* Spacing Scale (8px base) */
--spacing-xs: 0.25rem;   /* 4px */
--spacing-sm: 0.5rem;    /* 8px */
--spacing-md: 1rem;      /* 16px */
--spacing-lg: 1.5rem;    /* 24px */
--spacing-xl: 2rem;      /* 32px */
--spacing-2xl: 3rem;     /* 48px */
--spacing-3xl: 4rem;     /* 64px */
```

### Bordes y Sombras

#### Border Radius

```css
--radius-sm: 4px;
--radius-md: 8px;
--radius-lg: 12px;
--radius-xl: 16px;
--radius-full: 9999px;
```

#### Shadows

```css
/* Elevaciones */
--shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
--shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
--shadow-2xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
```

## 🖼️ Componentes UI

### Botones

```tsx
// Primary Button
<Button variant="primary" size="md">
  Guardar
</Button>

// Secondary Button
<Button variant="secondary" size="md">
  Cancelar
</Button>

// Outline Button
<Button variant="outline" size="md">
  Editar
</Button>

// Tamaños: xs, sm, md, lg, xl
```

### Cards

```tsx
<Card>
  <CardHeader>
    <CardTitle>Título de la Card</CardTitle>
  </CardHeader>
  <CardContent>
    Contenido de la card
  </CardContent>
  <CardFooter>
    <Button>Acción</Button>
  </CardFooter>
</Card>
```

### Inputs

```tsx
<Input
  label="Email"
  type="email"
  placeholder="tu@email.com"
  error="Email inválido"
/>
```

### Modals

```tsx
<Modal open={isOpen} onClose={handleClose}>
  <ModalHeader>
    <ModalTitle>Título del Modal</ModalTitle>
  </ModalHeader>
  <ModalBody>
    Contenido del modal
  </ModalBody>
  <ModalFooter>
    <Button onClick={handleClose}>Cerrar</Button>
  </ModalFooter>
</Modal>
```

## 📱 Responsive Design

### Breakpoints

```css
/* Mobile First Approach */
--breakpoint-xs: 0px;      /* Mobile */
--breakpoint-sm: 600px;    /* Tablet */
--breakpoint-md: 900px;    /* Desktop pequeño */
--breakpoint-lg: 1200px;   /* Desktop */
--breakpoint-xl: 1536px;   /* Desktop grande */
```

### Media Queries

```css
/* Mobile */
@media (max-width: 599px) {
  /* Estilos mobile */
}

/* Tablet */
@media (min-width: 600px) and (max-width: 899px) {
  /* Estilos tablet */
}

/* Desktop */
@media (min-width: 900px) {
  /* Estilos desktop */
}
```

## 🎯 Iconografía

### Librería de Iconos

Utilizamos **Material Icons** y **Lucide Icons**

```tsx
import { Home, Settings, User, ChartBar } from 'lucide-react';

<Home size={24} color="#2196F3" />
<Settings size={20} />
<User size={16} />
```

### Tamaños de Iconos

```css
--icon-xs: 16px;
--icon-sm: 20px;
--icon-md: 24px;
--icon-lg: 32px;
--icon-xl: 48px;
```

## 🎨 Herramientas de Diseño

### Figma

**Proyecto Principal**: [Figma - Analytics Platform](https://figma.com/file/...)

**Componentes Disponibles**:
- Design System completo
- Wireframes de todas las páginas
- Mockups de alta fidelidad
- Prototipos interactivos

### Adobe XD

**Archivos**:
- `design/adobe-xd/analytics-platform.xd`

## 📐 Wireframes

### Páginas Principales

1. **Login** - `wireframes/login.png`
2. **Dashboard** - `wireframes/dashboard.png`
3. **Reports** - `wireframes/reports.png`
4. **Data Sources** - `wireframes/data-sources.png`
5. **Settings** - `wireframes/settings.png`

## 🖼️ Mockups

### Desktop

- Resolución: 1920x1080
- Archivos en: `mockups/desktop/`

### Tablet

- Resolución: 768x1024
- Archivos en: `mockups/tablet/`

### Mobile

- Resolución: 375x667
- Archivos en: `mockups/mobile/`

## ✨ Animaciones y Transiciones

### Duración

```css
--transition-fast: 150ms;
--transition-base: 200ms;
--transition-slow: 300ms;
--transition-slower: 500ms;
```

### Easing

```css
--ease-in: cubic-bezier(0.4, 0, 1, 1);
--ease-out: cubic-bezier(0, 0, 0.2, 1);
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
```

### Ejemplos

```css
/* Hover en botones */
.button {
  transition: all var(--transition-base) var(--ease-in-out);
}

.button:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

/* Fade in */
.fade-in {
  animation: fadeIn var(--transition-slow) var(--ease-out);
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
```

## 📊 Gráficos y Visualizaciones

### Paleta para Gráficos

```css
/* Colores para charts */
--chart-1: #2196F3;  /* Azul */
--chart-2: #4CAF50;  /* Verde */
--chart-3: #FF9800;  /* Naranja */
--chart-4: #9C27B0;  /* Púrpura */
--chart-5: #F44336;  /* Rojo */
--chart-6: #00BCD4;  /* Cyan */
--chart-7: #FFEB3B;  /* Amarillo */
--chart-8: #795548;  /* Marrón */
```

## 🌙 Dark Mode

### Colores Dark Mode

```css
/* Backgrounds */
--dark-bg-primary: #121212;
--dark-bg-secondary: #1E1E1E;
--dark-bg-tertiary: #2D2D2D;

/* Text */
--dark-text-primary: #FFFFFF;
--dark-text-secondary: #B3B3B3;
--dark-text-disabled: #666666;

/* Borders */
--dark-border: #333333;
```

## 🎓 Mejores Prácticas

### Accesibilidad

- **Contraste**: Mínimo 4.5:1 para texto normal
- **Tamaño de fuente**: Mínimo 16px para body
- **Áreas de clic**: Mínimo 44x44px
- **Alt text**: Siempre en imágenes
- **Navegación por teclado**: Soportada en todos los componentes

### Performance

- Optimizar imágenes (WebP, compresión)
- Lazy loading para imágenes
- Minimizar animaciones pesadas
- Usar SVG para iconos

## 🤝 Contribución

1. Crear rama desde `design`
2. Actualizar diseños en Figma
3. Exportar assets necesarios
4. Documentar cambios en style guide
5. Crear Pull Request hacia `design`

## 📞 Contacto

**Design Lead**: design@analytics-platform.com
**Figma Team**: [Link al equipo](https://figma.com/team/...)
