## help

def sql_connect (user_name='Erfan' , password_user='erfan2325' , db='mafia'):
    from mysql.connector import connect
    return connect(user=user_name , password=password_user , database=db)

def bot_token ():
    return '2WOP8fzYbhTz50TDJHH1LZb7KCBQBvSXaTq6YOWAnk0JsqNSCIjMqJn4Y18eC3tCRLEjtmmJayhEu3x94UpCp_-6xpTgxTVH6FacY8XFB6MUgss1fvtyd-t-OCpV6UUJwsWmyQhnDrILgBfV'

def me_token ():
    return 'X1vMEU95qyK2PG3jRMOFYgqACr6HU5YWqG_ROUzYmQXJwADY4yN_K3qYY5Y'

def table_users ():
    return 'Users'

def table_list_servers ():
    return 'ServerRunning'

def regex_not_persion ():
    return r"[^۱۲۳۴۵۶۷۸۹۰آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی\s]+"

def game_loop_keyboard_init ():
    return[ [{'text' : 'جادو ها' , 'command' : '//magics' } , {'text' : 'خروج از بازی' , 'command' : '//exit_game'}] ]

def main_page_keyboard_init():
    return[ [{'text' : 'شروع بازی'       , 'command' : '//start_game_main_page'} , {'text' : 'تغییر نام'              , 'command' : '//change_name_main_page'}] ,
            [{'text' : 'امتیاز های من'   , 'command' : '//amtiaz_ha_main_page' } , {'text' : 'پاک کردن تمام امتیازات' , 'command' : '//delete_data_main_page'}] ,
            [{'text' : 'بهترین های بازی' , 'command' : '//best_gamer_main_page'} , {'text' : 'روش بازی'               , 'command' : '//help_about_game'      }] ]

def def_keyboard_votes(list_names:list , list_user_id:list): # nc
    pass
