1. Creamos una carpeta de trabajo, por ejemplo, con nombre HELLOWORLD
2. Con VS Code, creamos 2 ficheros: .env y server.py (puedes descargarlos directamente de este repositorio y guardarlos dentro de la carpeta creada HELLOWORLD o con VS crearlos de nuevo y guardarlos en dicha ruta)
3. En VS Code, vamos a Terminal -> Nueva terminal

<kbd>![image](https://user-images.githubusercontent.com/20743678/218127698-7e614fa2-0f26-4917-8572-9ecec8faa70a.png)</kbd>

4. En la parte inferior, cambiamos al directorio HELLOWORLD y ejecutamos:
```shell
python3 -m venv helloworld
```
O asignamos un nombre distinto al entorno:
```shell
python3 -m venv <tu_nombre_del_entorno>
```

Este comando nos creará una estructura de directorios para que las opciones de entorno de nuestro espacio de trabajo queden configurada e independiente de otras áreas de trabajo

<kbd>![image](https://user-images.githubusercontent.com/20743678/218128508-e0544938-6fa7-48a1-bb5a-7deab09d3ff1.png)</kbd>

5. Ejecutamos el comando:
```shell
.\helloworld\Scripts\activate
```
Obtendremos algo similar a esto:

<kbd>![image](https://user-images.githubusercontent.com/20743678/218129298-4f8e8950-4648-4661-82e7-2fe0c6924312.png)</kbd>

6. Instalamos flask con el comando:

```shell
pip3 install flask
```
Si no lo tenemos instalado nos lo instalará, pero si ya lo tenemos instalado nos saldrá algo similar a esto:

<kbd>![image](https://user-images.githubusercontent.com/20743678/218129868-9b07b510-561e-42e9-a11a-4145df7174cf.png)</kbd>

7. Instalamos python-dotenv con el comando:

```shell
pip3 install python-dotenv
```
Si no lo tenemos instalado nos lo instalará, pero si ya lo tenemos instalado nos saldrá algo similar a esto:

<kbd>![image](https://user-images.githubusercontent.com/20743678/218130121-af5655c0-dbf1-45fd-a042-dc1321340e48.png)</kbd>

Esta utilidad permite a flask arrancar (nota 1) con las opciones definidas en el fichero .env (nota 2), en nuestro caso, que corra en el puerto 8000 (nota 3) y que el fichero .py a correr sea server.py (nota 4)

Lanzamos flask con el comando:

```shell
flask run
```

<kbd>![image](https://user-images.githubusercontent.com/20743678/218131616-25bd5903-d174-4465-bbba-95597392b161.png)</kbd>

Y observamos la salida, donde se nos informa de que el servidor está corriendo en la URL http://127.0.0.1:8000 (nota 5)

8. Observamos también el aviso de que "FLASK_ENV" está obsoleto y nos recomeinda usar "FLASK_DEBUG" en su lugar, aunque al no encontrar "FLASK_DEBUG" considera que el entorno de despliegue es con depurador activado:

<kbd>![image](https://user-images.githubusercontent.com/20743678/218132816-e1d1f680-9d4c-4ca3-aa45-fc94d3a52090.png)</kbd>

Como esto duele en los ojos, cambiamos en el fichero .env la variable de entorno "FLASK_ENV" por "FLASK_DEBUG", pudiendo contener 2 opciones, on u off. Si la definimos como FLASK_DEBUG = on , el entorno será con debug activado. Si la definimos como FLASK_DEBUG = off , el entorno será con debug deasctivado.

Paramos el servicio flask con CTRL+C, editamos el fichero .env (nota 1) y lo guardamos y volvemos a lanzar "flask run" (nota 2). Ya nos sale sin los warnings de "deprecated", sólo nos avisa de que estamos en entorno de desarrollo (nota 3):

<kbd>![image](https://user-images.githubusercontent.com/20743678/218141645-24a645cf-3695-4dab-acd0-4ce89a9e387a.png)</kbd>

9. Visitamos la url http://127.0.0.1:8000 o http://localhost:8000 y veremos el esperado "Hello World!!!":

<kbd>![image](https://user-images.githubusercontent.com/20743678/218142914-6bbb6b74-c091-4f4d-8d94-2df68144ee68.png)</kbd>
