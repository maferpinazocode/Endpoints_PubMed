# Proyecto de Buscador de Papers (Flask + Frontend)

Este proyecto permite buscar artículos científicos desde PubMed usando la API de NCBI, y muestra los títulos de los artículos encontrados en un frontend simple.

## Requisitos

- Python 3.x
- Tener **pip** instalado para instalar dependencias.

## Pasos para correr el proyecto

### 1. Clonar el repositorio

  Si aún no tienes el repositorio, clónalo usando:
  
    git clone <URL_DEL_REPOSITORIO>
    cd nombre-del-repositorio

### 2. Crear y activar un entorno virtual
  Crear el entorno virtual:
  
    python -m venv venv

Activar el entorno virtual:

    venv\Scripts\activate

### 3. Instalar las dependencias
Instala las librerías necesarias con:

    pip install -r requirements.txt
Si no tienes el archivo requirements.txt aún, simplemente instala las siguientes librerías:

    pip install flask flask-cors requests
### 4. Levantar el servidor backend (Flask)
En una terminal, corre el servidor de Flask:

    python app.py
Esto levantará el servidor en http://127.0.0.1:5000, donde estará disponible el backend de la API.

### 5. Levantar el servidor frontend (HTML + JS)
Para servir los archivos del frontend, abre otra terminal y corre:

    python -m http.server 8000
Esto levantará el servidor en http://127.0.0.1:8000, donde podrás acceder a la interfaz web.

### 6. Acceder a la aplicación
Abre tu navegador y ve a:

http://127.0.0.1:8000
Desde allí, podrás escribir términos de búsqueda y ver los título
