from bs4 import BeautifulSoup
import re
import mysql.connector
from requests import get

def connector_sql ():
    table = 'testsqlmariadb2021erfan'
    user = 'root'
    password = 'erfan2325'
    database = 'python'
    print ()

    SQL = mysql.connector.connect(
        user=user ,
        password=password ,
        database=database)

    return SQL , table

SQL , table = connector_sql()

curser = SQL.cursor()
query = 'INSERT INTO %s VALUES (%i , %i , %i , %i , %i)'

def jaigozari (vorodi):

    number = {
        '۰' : '0',
        '۱' : '1',
        '۲' : '2',
        '۳' : '3',
        '۴' : '4',
        '۵' : '5',
        '۶' : '6',
        '۷' : '7',
        '۸' : '8',
        '۹' : '9',
        ',' : ''}
    x = ''

    for har in vorodi:
        x = x + number[har]

    return x

print ()
print ('شروع خواندن اطلاعات اس سایت دیجی کالا' , end='\n\n')

for page in range (1,11):
    print('page %s is reading' % str(page))

    counter = 0
    URL = 'https://www.digikala.com/search/category-ram/?page=%s' % str(page)
    vorodi = get(URL)

    soup = BeautifulSoup(vorodi.text , 'html5lib')
    all_ghimat = soup.find_all('div' , {"class" : "d-flex ai-center jc-end gap-1 color-700 color-400 text-h5 grow-1"})
    tree = len(all_ghimat)
    if tree == 0:
        continue
    all_ram = soup.find_all('div' , {"class" : "c-product-box__title"} , limit=tree)

    for har_ram in all_ram:

        har_ghimat = all_ghimat[counter]

        counter += 1

        har_ram = har_ram.text

        if (re.findall(r'رم\s*(دسکتاپ)' , har_ram)) == []:
            if (re.findall(r'رم\s*(کامپیوتر)' , har_ram)) == []: 
                if (re.findall(r'رم\s*(لپ تاپ)' , har_ram)) == []:
                    if (re.findall(r'رم\s*(تاپ لپ)' , har_ram)) == []:
                        continue
                    else:
                        model = 101
                else:
                    model = 101
            else:
                model = 100
        else:
            model = 100

        har_ghimat = re.sub(r'\s' , '' , re.sub(r'‍‍‍,' , '' , re.sub(r'تومان' , '' , har_ghimat.text))).strip()
        if  'ناموجود' in har_ghimat:
            continue
        har_ghimat = int(jaigozari(har_ghimat))

        DDR = re.findall(r'DDR(\d)' , har_ram)
        if DDR == []:
            continue

        zarfiat = re.findall(r'ظرفیت\s*(\d+)' , har_ram)
        if zarfiat == []:
            continue
        else:
            zarfiat = zarfiat[0]
            if len(zarfiat) >= 3:
                zarfiat = zarfiat[1] + zarfiat[2]

        MHz = re.findall(r'(\d+)\s*مگاهرتز' , har_ram)
        if MHz == []:
            MHz = re.findall(r'(\d+)MHz' , har_ram)
            if MHz == []:
                continue

        curser.execute(query % (table , int(DDR[0]) , int(MHz[0]) , int(model) , int(zarfiat) , har_ghimat))

SQL.commit()
SQL.close()

print ()
print ('اطلاعات با موفقیت خوانده و ذخیره شد')
