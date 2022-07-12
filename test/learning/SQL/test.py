import mysql.connector
cnx = mysql.connector.connect(
    user='me',
    password='nohack',
    database='learning'
)
print ('connected to the mysql!')

cursor = cnx.cursor()

query = 'INSERT INTO yek VALUES (%s , %i , %i)'

list_name = ['Erfan' , 'Jadi' , 'Ehsan' , 'Oskol' , 'Shangol']
from random import randint

for name in list_name:
    query = 'INSERT INTO yek VALUES ("%s" , %i , %i)'
    cursor = cnx.cursor()
    cursor.execute(query %(name , randint(40 , 70) , randint(150 , 200)))


cnx.commit()
cnx.close()