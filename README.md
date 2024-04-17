# iHouse FastAPI Seeder 

# Requisitos

- [Python (^v3)](https://www.python.org/downloads/)
    - [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
    - [uvicorn](https://www.uvicorn.org)

# Configuración del proyecto

#### 1.- Clonar Repositorio

```bash
git clone https://github.com/Yayo22124/iHouseFastApiSeeder.git
```

#### 2.- Crear entorno virtual (Si no existe previamente)

```bash
virtualenv miEntorno
```

### 3.- Activar entorno virtual

```bash
./miEntorno/Scripts/activate
```

#### 4.- Crear variables de entorno

Este proyecto usa `python-dotenv` para almacenar y usar variables de entorno seguras, es necesario crear un archivo **.env** a nivel raíz del proyecto y colocar dentro las siguientes variables de entorno:

- MONGODB_URL: La url de la base de datos a utilizar (Mongo) puede ser igual al cluster o a su bd local.

#### 5.- Ejecutar Proyecto

```bash
uvicorn app.main:app --reload
```