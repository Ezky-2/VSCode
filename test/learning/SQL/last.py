import re
import mysql.connector

SQL = mysql.connector.connect(
    user='Erfan',
    password='nohack',
    database='test'
)

counter_wrong = 0

while counter_wrong != 3:

    email = input('Enter your email: ')

    valid = re.findall(r'^\w+\@[a-zA-Z]+\.[a-zA-Z]+$' , email)
    if valid != []:
        password = input('Enter your password: ')

        query = 'INSERT INTO two VALUES ("%s" , "%s")'
        cursor = SQL.cursor()
        cursor.execute(query % (email , password))

        print ('Successfully saved to SQL' , end='\n\n')


    else:
        counter_wrong += 1
        print ('Wrong Email')
        print ('expression@string.string')
        print ('test025@yahoo.com' , end='\n\n')

SQL.commit()
SQL.close()