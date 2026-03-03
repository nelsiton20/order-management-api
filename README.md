# Order Management API

Backend para la gestión de pedidos desarrollado con **FastAPI** siguiendo principios de arquitectura por capas y separación de responsabilidades.

---

## Descripción técnica

API REST profesional que permite:

* **Autenticación con JWT**: Seguridad basada en tokens.
* **Gestión de usuarios**: Roles diferenciados (`admin` / `customer`).
* **Gestión de productos**: Control total del catálogo.
* **Ciclo de pedidos**: Creación, cancelación y reglas de negocio.
* **Manejo de stock**: Validaciones de inventario en tiempo real.
* **Seguridad**: Hashing de contraseñas con **Argon2**.

---

## Arquitectura

El proyecto está organizado en capas para asegurar el desacoplamiento:

```text
app/
├── core/          # Configuración global y utilidades base
├── domain/        # Reglas de negocio y excepciones puras
├── models/        # Definiciones del ORM (Base de Datos)
├── repositories/  # Acceso a datos y persistencia
├── routers/       # Capa de transporte (HTTP/Endpoints)
├── schemas/       # Modelos de Pydantic (Validación y DTOs)
├── security/      # Lógica de JWT y cifrado
├── services/      # Orquestación de lógica de negocio
├── scripts/       # Tareas de mantenimiento y automatización
```

- **Routers** → Capa HTTP
- **Services** → Lógica de negocio
- **Repositories** → Acceso a datos
- **Domain** → Reglas de negocio y excepciones
- **Security** → JWT y hashing
- **Schemas** → Validación de datos y DTOs
- **Core** → Configuración y servicios transversales
- **Scripts** → Tareas de automatización fuera del runtime

---

## Tecnologías utilizadas

- Python
- FastAPI
- PostgreSQL
- Peewee ORM
- JWT
- Argon2
- Pydantic

---

## Requisitos previos

Antes de ejecutar el proyecto debes tener instalado:

- Python 3.10+
- PostgreSQL

---

## Instalación y ejecución

### Clonar el repositorio

```bash
git clone https://github.com/nelsiton20/order-management-api.git
cd order-management-api
```

### Crear entorno virtual
```
python -m venv env
source venv/bin/activate # macOs
env\scripts\activate # Windows
```

### Instalar dependencias
```
pip install -r requirements.txt
```

### Configurar variables de entorno
Crear un archivo .env con las siguientes variables:
```
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
SECRET_KEY=
ALGORITHM=
ACCESS_TOKEN_EXPIRE_DAYS=
ADMIN_USER_EMAIL=
ADMIN_USER_PASSWORD=
```
(Completar con valores correspondientes)

### Crear base de datos en PostgreSQL
Debes ejecutar los siguientes comandos en tu terminal:
```
psql -U postgres # al ejecutar este comando se te pedirá ingresar la contraseña de tu usuario postgres
CREATE DATABASE <nombre de la base de datos> # el nombre debe ser igual al que definiste en la variable de entorno DATABASE_NAME
```

### Crear usuario administrador
El usuario administrador es el único con la capacidad de:
- Crear otros usuarios administradores
- Crear productos
- Modificar el estado de los pedidos

Este es el comando que debes ejecutar para crear el usuario administrador:
```
python -m app/scripts/create_admin.py
```

### Ejecutar el servidor
```
uvicorn main:app
```

La API estará disponible en:
```
http://127.0.0.1:8000
```

---

## Documentación interactiva
FastAPI genera automáticamente documentación Swagger en:
```
http://127.0.0.1:8000/docs
```

---

## Roles disponibles
- Admin
    - Crear productos
    - Ver todos los pedidos

- Customer
    - Crear pedidos
    - Cancelar pedidos propios
    - Ver sus pedidos

---

## Decisiones técnicas importantes
- El precio del producto se almacena en OrderItem para mantener historial.
- Se utilizan transacciones atómicas para evitar inconsistencias.
- Separación clara entre autenticación y entidad de negocio.
- Validaciones centralizadas en capa de dominio.

--- 

## Posibles mejoras futuras
- Tests automatizados
- Dockerización
- Rate limiting
- Sistema de logs estructurados

--- 

## Autor
Nelson Jorge Javier Rojas Camones - Backend Developer