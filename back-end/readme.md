terminal (bash)
python -m pip install virtualenv
source venv/Source/activate

<!-- dentro de venv -->

pip install fastapi sqlalchemy pymysql uvicorn

<!-- correr el servidor -->

uvicorn main:app --reload
