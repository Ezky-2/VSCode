from client import Client
import values
from lib import *
from class_user import user
SQL = values.sql_connect()
cursor = SQL.cursor()

class defs:

    def __init__ (self , bot_token):
        self.bot_token = bot_token
        self.client = Client(bot_token)

    def get_message (self):
        messages = self.client.get_messages()
        for message in messages:
            yield message

    def send_message (self , user_id , message , keyboard=None):
        self.client.send_text(user_id , message , self.client.make_keyboard(keyboard))

    def change_keyboard (self , to , keyboard):
        self.client.change_keyboard(to, self.client.make_keyboard(keyboard))

    def send_group (self , list_of_user_id , name_karbar , message , keyboard=None):
        text = '%s : %s'
        for har_fard in list_of_user_id:
            self.send_message(har_fard[0] , text % (name_karbar , message) , keyboard)

    def magics_game (self , karbar):
        pass

    def exit_game (self , karbar:user , server , bot , keyboard=None):
        user_id = karbar
        tmp_keyboard = [[{'text' : 'بله' , 'command' : '//yes_exit'} , {'text' : 'نه' , 'command' : '//no_exit'}]]
        self.send_message(user_id , 'ایا مطمعن به خروج از بازی هستید؟' , tmp_keyboard)
        for message in self.get_message():
            if message['body'][0:2] == '//':
                if message['body'] == '//yes_exit':
                    cursor.execute('DELETE FROM %s WHERE ID="%s"' % (server.server_name , user_id))
                    t_m = 'کاربر %s از بازی خارج شد' % karbar.name # tmp_message
                    bot.send_group(server.all , 'سیستم' , t_m , keyboard)
                    return True

                if message['body'] == '//no_exit':
                    self.send_message(user_id , 'باشه پس به بازی ادامه بده' , keyboard)
                    return False
            else:
                self.send_group(server.server_name , karbar.name , message['body'])

    def reset_rank (self , user_id):
        tmp_message = 'ایا مطمعن به پاک کردن تمام اطلاعات خود شامل امتیاز , نام و  id شما در ربات هستید؟'
        tmp_keyboard = [[{'text' : 'بله' , 'command' : '//yes_reset_rank'} , {'text' : 'نه' , 'command' : '//no_reset_rank'}]]
        self.send_message(user_id , tmp_message , tmp_keyboard)
        for message in self.get_message():
            if message['body'][0:2] == '//':
                if message['body'] == '//yes_reset_rank':
                    cursor.execute('DELETE FROM %s WHERE ID="%s"' %(values.table_users() , user_id))
                    SQL.commit()
                    self.send_message(user_id , 'اطلاعات شما با موفقیت پاک شد')
                    return True
                if message['body'] == '//no_reset_rank':
                    self.send_message(user_id , 'باشه')
                    return False
            else:
                self.send_message(user_id , 'جوون؟ :/')

    def start_game (self , karbar):
        tmp_message = 'ایا مطمعن به شروع بازی هستید؟'
        tmp_keyboard = [ [{'text' : 'بله' , 'command' : '//yes_start_game_main_page'} , {'text' : 'نه' , 'command' : '//no_start_game_main_page'}] ]
        self.send_message(karbar.ID , tmp_message , tmp_keyboard)

        for message in self.get_message():
            if message['from'] == karbar.ID:
                body = message['body']
                if body == '//yes_start_game_main_page':
                    game_loop(karbar)
                    break
                elif body == '//no_start_game_main_page':
                    self.send_message(karbar.ID , 'باشه')
                    break

    def change_name (self , karbar):
        user_id = karbar.ID
        name_karbar = None
        tmp_message_2 = 'لطفا اسم خود را وارد نمایید'
        tmp_keyboard_2 = [ [{'text' : 'منصرف شدم' , 'command' : '//cancel_change_name_main_page'}] ]
        self.send_message(user_id , tmp_message_2 , tmp_keyboard_2)

        for message in self.get_message():

            if message['from'] == user_id:
                body = message['body']
                if message['body'] == '//cancel_change_name_main_page': # cancel
                    self.send_message(user_id , 'باشه')
                    return False
                if body == '//yes_change_name': # change name
                    karbar.updater('Name' , name_karbar)
                    self.send_message(user_id , 'اسم شما با موفقیت تغییر کرد')
                    return True
                if not body[0:2] == '//':
                    name_karbar = body
                if body == '//no_change_name': # wrong onderstand
                    self.send_message(user_id , 'ببخشید لطفا دوباره بگید')
                    name_karbar = None
                if name_karbar != None:
                    tmp_message = 'اسم شما %s هست دیگه نه؟' % name_karbar
                    tmp_keyboard = [[{'text' : 'اره همینه' , 'command' : '//yes_change_name'} , {'text' : 'نه اشتباهه' , 'command' : '//no_change_name'}]]
                    self.send_message(user_id , tmp_message , tmp_keyboard)

    def amtiaz_hai_karbar (self , karbar):
        cursor.execute('SELECT Amtiaz , TDavat , TCoin FROM %s WHERE ID="%s"' %(values.table_users() , karbar.ID))
        data = cursor.fetchall()[0]
        tmp = 'امتیاز شما هست: %i\nتعداد نفرات دعوت شده توسط شما هست: %i\nنعداد سکه های شما هست: %i' % (data[0] , data[1] , data[2])
        self.send_message(karbar.ID , tmp)

    def show_best_gamer (self , karbar , keyboard=None):
        list_name = ['بهترین های این بازی از لحاظ امتیاز برابر است با:\n']
        tmp = ' %s : %s'
        counter = 0
        SQL = values.sql_connect()
        cursor = SQL.cursor()
        cursor.execute('SELECT Amtiaz , Name FROM %s' % values.table_users())
        data = cursor.fetchall()
        data.sort(reverse=True)

        for har_shakhs in data:
            number = jaigozari(har_shakhs[0])

            if counter == 11:
                break
            if counter == 0:
                list_name.append('🥇.' + tmp % (har_shakhs[1] , number))
            elif counter == 1:
                list_name.append('🥈.' + tmp % (har_shakhs[1] , number))
            elif counter == 2:
                list_name.append('🥉.' + tmp % (har_shakhs[1] , number))
            else:
                list_name.append('🌟.' + tmp % (har_shakhs[1] , number))
            counter += 1
        list_name.append('\n\n⭕️' + tmp % (karbar.name , karbar.amtiaz))

        self.send_message(karbar.ID , '\n'.join(list_name) , keyboard)

    def help_about_game (self , karbar , keyboard=None):
        pass

    def random_karakter (self , list_user_id):
        Dict = dict()
        from random import sample

        jon       = ','.join( sample( ['doktor'       , 'badygard' ] , 1))                       # حفاظتی ها
        dideban   = ','.join( sample( ['tizbin'       , 'radgir'   ] , 1))                       # دیدهبان ها
        plus      = ','.join( sample( ['ghebgo'       , 'zerehposh'] , 1))                       # کمکی ها
        mostaghel = ','.join( sample( ['gorgine'      , 'ghatel'  , 'joker'   ] , 1))            # مستقل ها
        sabet     = ','.join( sample( ['pedar_khande' , 'sniper' , 'bazpors' ] , 3))            # ثابت ها
        mafia     = ','.join( sample( ['haker'        , 'noche'   , 'maftesh' , 'shaiad' ] , 1)) # مافیا ها

        List_karakters = (jon + ',' + dideban + ',' + mostaghel + ',' + sabet + ',' + mafia + ',' + plus).split(',')
        List_karakters = sample(List_karakters , len(List_karakters))

        for counter in range(len(List_karakters)):
            Dict[list_user_id[counter]] = List_karakters[counter]

        return Dict
