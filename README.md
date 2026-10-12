# Agenda de Contactos Personal 2 (ES02 - Programación Backend)

Aplicación web desarrollada con **Django** y desplegada en **Vercel** con base de datos de producción en **Supabase (PostgreSQL)**, correspondiente a la Evaluación Sumativa 2 (Caso 3: Agenda de Contactos Personal).

---

##  Características y Requerimientos Cumplidos

### 1. Base de Datos en Producción (No SQLite)
- Conexión configurada a **PostgreSQL en la nube (Supabase)** utilizando `psycopg2-binary`.
- Migraciones ejecutadas y sincronizadas exitosamente en el servidor de base de datos remoto.
- Eliminación total de SQLite en el entorno productivo.

### 2. Personalización de Django Admin & Branding
- **Branding institucional**: Títulos del panel adaptados (`admin.site.site_header`, `admin.site.site_title`, `admin.site.index_title`).
- **Búsqueda**: Búsqueda por `nombre` y `correo`.
- **Filtros personalizados**: Implementación de `ProveedorCorreoFilter` (`SimpleListFilter`) para segmentar contactos por dominios (Gmail, Outlook, INACAP, otros).
- **Acción masiva (Action)**: Exportación de contactos seleccionados a formato **CSV** descargable con codificación UTF-8 / BOM para compatibilidad con Microsoft Excel.

### 3. CRUD Completo con Validación y Feedback al Usuario
- **Listado (Read)**: Vista con tarjetas responsivas y buscador en tiempo real.
- **Paginación**: Paginación integrada con Django `Paginator` (5 contactos por página) manteniendo los parámetros de búsqueda activos.
- **Creación (Create)**: Formulario validado para ingresar nombre, teléfono, correo y dirección.
- **Edición (Update)**: Modificación de contactos existentes con validaciones de campos y manejo de errores.
- **Eliminación (Delete)**: Flujo de borrado seguro con confirmación previa.
- **Mensajes de interfaz (Feedback)**: Alertas visuales (`django.contrib.messages`) con soporte de Bootstrap 5 para avisos de éxito, advertencia y error.

### 4. Variables de Entorno y Seguridad
- Gestión de credenciales confidenciales (`SECRET_KEY`, `DEBUG`, `host`, `port`, `database`, `user`, `password`) a través de `python-dotenv` y archivo `.env`.
- Plantilla pública `.env.example` incluida en el repositorio.
- Exclusión segura de credenciales mediante `.gitignore`.

### 5. Archivos Estáticos y Despliegue
- Configuración de **WhiteNoise** (`whitenoise.middleware.WhiteNoiseMiddleware`) para servir archivos estáticos eficientemente en producción.
- Configuración para despliegue serverless en **Vercel** (`vercel.json`, `agenda/wsgi.py`).

---

##  Estructura del Proyecto

```
ES02_Agenda/
├── agenda/                  # Configuración principal del proyecto Django
│   ├── settings.py         # Configuración (Supabase, WhiteNoise, variables de entorno)
│   ├── urls.py             # Enrutamiento general
│   └── wsgi.py             # Configuración WSGI con alias para Vercel
├── contactos/               # Aplicación de gestión de contactos
│   ├── admin.py            # Personalización de Django Admin y acción CSV
│   ├── forms.py            # Formulario ContactoForm con validaciones
│   ├── models.py           # Modelo Contacto
│   ├── templates/          # Plantillas HTML con Bootstrap 5
│   │   ├── base.html       # Plantilla base con navbar y mensajes de alerta
│   │   └── contactos/
│   │       ├── contacto_list.html            # Listado con paginador y buscador
│   │       ├── contacto_form.html            # Formulario de creación y edición
│   │       └── contacto_confirm_delete.html  # Confirmación de borrado
│   ├── urls.py             # Rutas del CRUD
│   └── views.py            # Vistas del CRUD, paginación y mensajes
├── staticfiles/            # Archivos estáticos recolectados
├── .env.example            # Plantilla de variables de entorno
├── requirements.txt        # Dependencias de Python
└── vercel.json             # Manifiesto de despliegue en Vercel
```

---

##  Instalación y Ejecución Local

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd ti3041-es02-agenda
   ```

2. **Crear y activar entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   # o en Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno:**
   Copia el archivo `.env.example` a `.env` y completa los datos de conexión a Supabase:
   ```bash
   cp .env.example .env
   ```

5. **Ejecutar migraciones y recolectar estáticos:**
   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```

6. **Iniciar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```
   Accede a `http://127.0.0.1:8000/`.

---

##  Acceso al Django Admin

- **Ruta:** `/admin/`
- **Usuario administrador por defecto:** `admin`
- **Contraseña:** `admin1234`
