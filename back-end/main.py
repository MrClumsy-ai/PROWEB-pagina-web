# terminal (bash):
# py -m pip install mysql-connector-python
# py -m pip install virtualenv
# source venv/Scripts/activate
import mysql.connector

db = mysql.connector.connect(
    user="root", password="piratas02", host="localhost", database="test", port="3306"
)
print(db)

cur = db.cursor()
# cur.execute("")
