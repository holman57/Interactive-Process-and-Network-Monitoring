import mysql.connector
from secrete.Secretes import Dorp_Points

mydb = mysql.connector.connect(
    host=Dorp_Points.host,
    user=Dorp_Points.user,
    port=Dorp_Points.port,
    password=Dorp_Points.password,
    database=Dorp_Points.database
)

mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM Nodes')
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
