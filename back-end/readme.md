<!-- abrir mysql workbench, y correr el codigo de !basededatos.txt
terminal (bash)
python -m pip install virtualenv
virtualenv venv
source venv/Source/activate
pip install fastapi sqlalchemy pymysql uvicorn -->

## Instalacion e inicializacion del servidor

1.  instalar mysql, poner la contrasena de root como 'root'
2.  correr mysql, correr el codigo de !basededatos.txt
3.  abrir la terminal (bash), correr los siguientes comandos:

```bash
    # instalar los modulos necesarios para el servidor
    python -m pip install virtualenv fastapi sqlalchemy pymysql uvicorn
    # ir a la carpeta de back-end
    cd back-end`
    # crear un virtual environment, llamarlo venv, asegurarse que este creado dentro de la carpeta back-end
    python -m virutalenv venv
    # activar el virtual environment
    source venv/Source/activate
    # volver a instalar los modulos necesarios para el servidor dentro del virtual environment
    pip install virtualenv fastapi sqlalchemy pymysql uvicorn
    # iniciar el servidor
    uvicorn main:app --reload
```

## Documentacion de la api

una vez iniciado el servidor, ir a la ruta:
/docs

tutorial de back-end
https://www.youtube.com/watch?v=zzOwU41UjTM

```

```
