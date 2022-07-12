from sklearn import tree
import mysql.connector
clf = tree.DecisionTreeClassifier()

def connector_sql ():
    user = input('نام کاربری دی بی را وارد کنید: ')
    password = input('پسورد را وارد کنید: ')
    database = input('دیتابیس را وارد کنید: ')

    SQL = mysql.connector.connect(
        user=user ,
        password=password ,
        database=database)

    try:
        x = SQL.cursor()
        x.execute('SELECT * FROM testsqlmariadb2021erfan')
        print ('تیبل توسط برنامه شناسایی شد')
        SQL = mysql.connector.connect(
            user=user ,
            password=password ,
            database=database)
        return SQL , 'testsqlmariadb2021erfan'

    except:
        table = input('لطفا تیبل را وارد نمایید: ')
    return SQL , table

SQL , table = connector_sql()
print ()
cursor = SQL.cursor()

x = []
y = []

cursor.execute('SELECT * FROM %s;' % table)

for DDR , MHz , model , zarfiat , ghimat in cursor:
    tmp = []
    tmp.append(DDR)
    tmp.append(MHz)
    tmp.append(model)
    tmp.append(zarfiat)

    x.append(tmp)
    y.append(ghimat)

print ('اطلاعات اماده است')

clf = clf.fit(x , y)

print ('اطلاعات توسط ماشین یاد گرفته شد' , end='\n\n')

print ('Example: 3 , 1600 , laptab , 4')

# اولین عدد نسل رم است

# دومین عدد مگاهرتز رم

# سومین مدل دستگاه یا سخت افزار مثل کامپوتر یا لپتاب

# ضرفیعت هر رم

for a in range(1 , 6):
    tmp = []

    vorodi = input('Enter your data: ')
    vorodi = vorodi.split(',')

    tmp.append(int(vorodi[0]))
    tmp.append(int(vorodi[1]))

    if 'computer' in vorodi[2]:
        tmp.append(100)
    elif 'laptab' in vorodi[2]:
        tmp.append(101)
    else:
        print ('اطلاعات وارد شده اشتباه است')

    tmp.append(int(vorodi[3]))

    print ((clf.predict([tmp]))[0])

if table == 'testsqlmariadb2021erfan':
    print ()
    print ('ایا می خواهید تیبل ساخته شده پاک شود؟')

    x = input('y or n: ')

    if x == 'y':
        cursor = SQL.cursor()
        cursor.execute('DROP table testsqlmariadb2021erfan')


