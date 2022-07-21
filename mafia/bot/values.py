# changable

def database_bot ():
    return 'mafia'

def table_users ():
    return 'Users'

def me_token ():
    return 'X1vMEU95qyK2PG3jRMOFYgqACr6HU5YWqG_ROUzYmQXJwADY4yN_K3qYY5Y'

def bot_token ():
    return 'yIB5iKxaP8wAunOi7GhS5PYSteIa_gQHspgJcbjq9MRn_0yp0cZ5uXEjp4Q4o8OUvtUdHpLCzVcCMdlQ4Gt_CsDsqKAyX6xXUwpnGLVOTy3Ot4j9JNT9th3nTpCzydIOeIQu2vZqvDg4GNUC'

def table_list_servers ():
    return 'ServerRunning'

def database_user_name ():
    return 'Erfan'

def database_password_user ():
    return 'erfan2325'

#data or defs

def sql_connect (user_name=database_user_name() , password_user=database_password_user() , db=database_bot()):
    from mysql.connector import connect
    return connect(user=user_name , password=password_user , database=db)

def regex_not_persion ():
    return r"[^۱۲۳۴۵۶۷۸۹۰آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی\s]+"

# keyboards

def game_loop_keyboard_init ():
    return[ [{'text' : 'جادو ها' , 'command' : '//magics' } , {'text' : 'خروج از بازی' , 'command' : '//exit_game'}] ]

def main_page_keyboard_init():
    return[ [{'text' : 'شروع بازی'       , 'command' : '//start_game_main_page'} , {'text' : 'تغییر نام'              , 'command' : '//change_name_main_page'}] ,
            [{'text' : 'امتیاز های من'   , 'command' : '//amtiaz_ha_main_page' } , {'text' : 'پاک کردن تمام امتیازات' , 'command' : '//delete_data_main_page'}] ,
            [{'text' : 'بهترین های بازی' , 'command' : '//best_gamer_main_page'} , {'text' : 'روش بازی'               , 'command' : '//help_about_game'      }] ]

def def_keyboard_votes(list_names:list , list_user_id:list): # nc
    pass
