from bs4 import BeautifulSoup
from requests import get
import re
import mysql.connector

SQL = mysql.connector.connect(
    user='Erfan' ,
    password='erfan2325' ,
    database='learning'
)

# x = input('Enter Car: ')
x = 'audi'
url = 'https://www.truecar.com/used-cars-for-sale/listings/%s/?sort[]=best_match'

reader = get(url % x)

soup = BeautifulSoup(reader.text , 'html.parser')

cars = soup.find_all('div' , {"data-test":"cardContent"})

counter = 0

for car in cars:

    if counter == 20:
        break

    car = car.text
    x = re.findall(r'\$(\d+\,\d\d\d)' , car)
    x = x[0]
    ghimat = int(re.sub(r'\,' , '' , x))

    car = re.sub(r'\$(\d+\,\d\d\d)' , ' ' , car)
    x = re.findall(r'(\d+\,\d\d\d)\s*miles' , car)
    x = x[0]
    karkard = int(re.sub(r'\,' , '' , x))

    query = 'INSERT INTO car_web VALUES (%i , %i)'
    curser = SQL.cursor()
    curser.execute(query % (karkard , ghimat))

    counter += 1


SQL.commit()
SQL.close()
