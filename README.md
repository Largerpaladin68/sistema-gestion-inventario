# Sistema de Gestión de Inventario

Aplicación de consola desarrollada en Python para administrar productos mediante una base de datos SQLite. Permite registrar, consultar, actualizar y eliminar productos, además de realizar búsquedas por identificador.

## Funcionalidades

- **Registrar productos:** guardar nombre, descripción, cantidad, precio y categoría.
- **Consultar inventario:** visualizar los productos almacenados.
- **Actualizar productos:** modificar el precio de un producto existente.
- **Eliminar productos:** borrar registros mediante su identificador.
- **Buscar productos:** consultar un producto por su ID.
- **Persistencia de datos:** almacenar la información localmente mediante SQLite.

## Tecnologías utilizadas

- **Python:** lógica de la aplicación y gestión de las operaciones.
- **SQLite:** almacenamiento y consulta de datos mediante SQL.
- **Colorama:** personalización de mensajes en la consola.

## Estructura del proyecto

```text
sistema-gestion-inventario/
├── main.py       # Menú principal y flujo de la aplicación
├── sql.py        # Conexión a SQLite y operaciones sobre productos
├── .gitignore    # Archivos excluidos del control de versiones
└── README.md     # Documentación del proyecto
```

## Requisitos

- Python 3.10 o superior.
- pip para instalar la dependencia externa.

SQLite se utiliza a través del módulo `sqlite3` de Python, por lo que no requiere una instalación adicional para este proyecto.

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/Largerpaladin68/sistema-gestion-inventario.git
cd sistema-gestion-inventario
```

### 2. Instalar las dependencias

```bash
python -m pip install colorama
```

### 3. Ejecutar la aplicación

```bash
python main.py
```

Al iniciar la aplicación, se crea la tabla de productos si todavía no existe. La base de datos `inventario.db` se genera localmente cuando se establece la conexión.

## Modelo de datos

La tabla `productos` contiene los siguientes campos:

| Campo | Descripción |
|---|---|
| `id` | Identificador único autoincremental |
| `nombre` | Nombre del producto |
| `descripcion` | Descripción opcional |
| `cantidad` | Cantidad disponible |
| `precio` | Precio del producto |
| `categoria` | Categoría del producto |

## Objetivos de aprendizaje

Este proyecto permitió practicar programación en Python, modularización mediante funciones y archivos, consultas SQL, operaciones CRUD y conexión con una base de datos SQLite.

---

Proyecto académico de práctica.
