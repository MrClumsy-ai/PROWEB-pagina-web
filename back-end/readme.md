1.  abrir mysql workbench, y correr el codigo de !basededatos.txt
2.  terminal (bash)
    python -m pip install virtualenv
    virtualenv venv
    source venv/Source/activate
    pip install fastapi sqlalchemy pymysql uvicorn

<!-- correr el servidor -->

uvicorn main:app --reload

<!-- documentacion -->

root/docs
https://www.youtube.com/watch?v=zzOwU41UjTM&t=363s
