import values
import lib
from class_user import user
SQL = values.sql_connect()

class server:

    def __init__ (self , karbar:user):
        ## find server ##
        sang = True

        cursor = SQL.cursor()
        cursor.execute('SELECT * FROM %s' % values.table_list_servers())
        data = cursor.fetchall()

        for har_server in data: # چک کردن برای سرور خالی یا کم عضو
            har_server = har_server[0].strip('\n')
            cursor.execute('SELECT counter_users FROM %s' % har_server)
            last = cursor.fetchall()
            number_of_users = last.pop()[0]
            if number_of_users <= 6:
                lib.writer_DB(har_server , 'ID' , karbar.ID)
                self.server_name = har_server
                sang = False

        if sang: # ساخت سرور جدید بدلیل نبود سرور
            tmp = self.create_room()
            lib.writer_DB(tmp , 'ID', karbar.ID)
            self.server_name = tmp

        ##   finish    ##
        self.start_game = False
        self.me = str() # user karakter
        self.death = False # live or death
        self.close = False
        self.update_values()

    def create_room (self): # ID , karakter
        random_str = lib.random_string()
        cursor = SQL.cursor()
        cursor.execute('CREATE TABLE %s (counter_users int(1) AUTO_INCREMENT KEY , ID varchar(60) , karakter VARCHAR(10) )' % random_str)
        SQL.commit()
        lib.writer_DB(values.table_list_servers() , 'Name' , random_str)
        return random_str

    def close_room (self):
        cursor = SQL.cursor()
        cursor.execute('DROP TABLE %s' % self.server_name) # پاک کردن خود سرور
        cursor.execute('DELETE FROM %s WHERE Name="%s"' %(values.table_list_servers() , self.server_name)) # پاک کردن سرور از لیست
        SQL.commit()
        self.close = True

    def update_values (self):
        self.all = [] # all user_id
        self.any = dict() # all users and karakters
        cursor = SQL.cursor()
        cursor.execute('SELECT * FROM %s' % self.server_name)
        data = cursor.fetchall()
        for har in data:
            self.all.append(har[1])  # all user id
            self.any[har[2]] = har[1]
            last_number = har[0]
        else:
            self.number = last_number
