# FastAPI + Python
Manual paso a paso para crear una aplicación web usando FastAPI y Python en Windows

## Entorno del sistema:
* Windows 10
* Visual Studio Code
* Python 3.11

## Primeros pasos:
* Tener instalado Visual Studio Code (VS Code)

https://code.visualstudio.com/

* Instalar la extensión de Python en VS Code
<kbd>![image](https://user-images.githubusercontent.com/20743678/218970281-6e648670-be96-4720-83a4-a3ebada66343.png)</kbd>

* En la propia terminal de VS Code, ejecutamos el siguiente comando para instalar FastAPI:

```powershell
pip install "fastAPI[all])"
```

<kbd>![image](https://user-images.githubusercontent.com/20743678/218970992-dddf638a-e667-4a3f-8d9f-696c604c8291.png)</kbd>

* Creamos una carpeta de trabajo y dentro de ella un fichero .py, en mi caso "main.py", con el siguiente código :

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!!"}
```

Según nuestro ejemplo anterior, hemos creado un fichero llamado main.py, el cual contiene la creación de un onjeto llamado "app". Lanzamos "unicorn" des de la línea de comando con:

```powershell
python -m uvicorn main:app --reload
```

<kbd>![image](https://user-images.githubusercontent.com/20743678/218973884-140e0c55-40b2-403b-91ec-f4e2a82581d0.png)</kbd>

El comando uvicorn main:app se refiere a:

* main: el archivo main.py (el "módulo" de Python) (nota 1)
* app: el objeto creado dentro de main.py con la línea app = FastAPI() (nota 2)
* --reload: hace que el servidor se reinicie cada vez que cambia el código. Úsalo únicamente para desarrollo

Y la salida generada en la terminal:

* URL donde nuestro servidor está escuchando (nota 3), en nuestro caso -> http://127.0.0.1:8000 . Además, nos informe de que para detener el servicio hemos de pulsar CTRL+C
* El @app.get("/") le dice a FastAPI que la función que tiene justo debajo está a cargo de manejar los requests que van al path / usando una operación get. Esto es: cuando hagamos una llamada al path indicado como "/", se ejecutará la función que está justo debajo -> "root()". 

En este ejemplo, definimos 2 funciones y 2 paths, cada uno con su llamada correspondiente:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def funcion_que_se_ejecuta_al_visitar_la_raiz():
    return {"message": "Hello World!! - Desde http://127.0.0.1:8000/"}

@app.get("/prueba")
async def funcion_que_se_ejecuta_al_visitar_la_subcarpeta_prueba():
    return {"message": "Hello World!! - Desde http://127.0.0.1:8000/prueba"}
```

<kbd>![image](https://user-images.githubusercontent.com/20743678/218977848-02dff98d-a5cb-4a02-8be8-8120b13e3bc9.png)</kbd>

<kbd>![image](https://user-images.githubusercontent.com/20743678/218978000-c2b31f08-15bf-48bf-93f8-1b0261f035e9.png)</kbd>


