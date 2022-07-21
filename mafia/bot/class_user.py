import values
from lib import *

class user:

    def __init__ (self , user_id):
        SQL = values.sql_connect()
        cursor = SQL.cursor()
        cursor.execute('SELECT * FROM %s WHERE ID="%s"' %(values.table_users() , user_id))
        data = cursor.fetchall()
        if data == []:
            data = self.create_user(user_id)
        else:
            data = data[0]

        self.ID = data[0]
        self.name = data[1]
        self.amtiaz = data[2]
        self.uadmin = data[3]
        self.tdavat = data[4]
        self.tcoin = data[5]

    def updater (self , column:str , new):
        SQL = values.sql_connect()
        cursor = SQL.cursor()
        if type(new) == type(10):
            cursor.execute('UPDATE %s SET %s=%s WHERE ID="%s"' % (values.table_users() , column , new , self.ID))
        else:
            cursor.execute('UPDATE %s SET %s="%s" WHERE ID="%s"' % (values.table_users() , column , new , self.ID))
        SQL.commit()
        self.update_values()

    def update_values (self):
        SQL = values.sql_connect()
        cursor = SQL.cursor()
        cursor.execute('SELECT * FROM %s WHERE ID="%s"' %(values.table_users() , self.ID))
        data = cursor.fetchall()[0]

        self.ID = data[0]
        self.name = data[1]
        self.amtiaz = data[2]
        self.uadmin = data[3]
        self.tdavat = data[4]
        self.tcoin = data[5]

    def create_user(self , user_id):
        from class_bot import defs
        SQL = values.sql_connect()
        bot = defs(values.bot_token())
        cursor = SQL.cursor()
        name_karbar = None
        tmp_message = 'متاسفانه اسم شما در بازی ثبت نشده است لطفا اسم خود را وارد نمایید'
        tmp_keyboard = [[{'text' : 'اره همینه' , 'command' : '//yes_create_user'} , {'text' : 'نه اشتباهه' , 'command' : '//no_create_user'}]]
        bot.send_message(user_id , tmp_message)

        for message in bot.get_message():

            if message['from'] == user_id:

                body = message['body']
                if body == '//yes_create_user': # change name
                    cursor.execute('INSERT INTO %s (ID , Name) VALUES ("%s" , "%s")' % (values.table_users() , user_id , name_karbar))
                    SQL.commit()

                    t = 'حالا دیگه عضو بازی شدی می تونی وارد بازی بشی و بقیه رو دعوت کنی تا سکه بگیری \nراستی ۵۰ تا سکه هم برای عضو شدنت به حسابت اضافه شد'
                    bot.send_message(user_id , t)

                    cursor.execute('SELECT * FROM %s WHERE ID="%s"' %(values.table_users() , user_id))
                    return cursor.fetchall()[0]

                if not body[0:2] == '//':
                    name_karbar = body
                    tmp_message = 'اسم شما %s هست دیگه نه؟' % name_karbar

                if body == '//no_create_user': # wrong onderstand
                    bot.send_message(user_id , 'ببخشید لطفا دوباره بگید')
                    name_karbar = None
                if name_karbar != None:
                    bot.send_message(user_id , tmp_message , tmp_keyboard)
