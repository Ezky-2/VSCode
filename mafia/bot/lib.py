import values

def for_loop_game(bot , karbar , server , message , keyboard=None):
    if message['type'] == 'TEXT':
        if message['body'][0:2] == '//': # اجرا کردن دستورات کیبورد
            dastor = message['body']
            if dastor == '//magics':
                bot.magics_game(karbar.ID)
            elif dastor == '//exit_game':
                if bot.exit_game(karbar.ID , karbar.name , server): # اگر خارج شد بازی را متوقف می کند
                    return False
            else:
                return dastor
        else:
            bot.send_group(server.all , karbar.name , message['body'] , keyboard)
    else:
        bot.send_message(karbar.ID , 'در پیام ارسال شده مشکلی وجود دارد لطفا از کیبورد استفاده کنید' , values.main_page_keyboard_init)

def random_string ():
    from string import ascii_letters
    from random import choice
    return ''.join(choice(ascii_letters) for i in range(20))

def jaigozari (vorodi):

    vorodi = str(vorodi)
    x = ''
    number = {
        '0' : '۰',
        '1' : '۱',
        '2' : '۲',
        '3' : '۳',
        '4' : '۴',
        '5' : '۵',
        '6' : '۶',
        '7' : '۷',
        '8' : '۸',
        '9' : '۹',
        '.' : ''}

    for har in vorodi:
        x = x + number[har]

    return x

def writer (text , loc , back_salsh=True , mode='a'):
    with open(loc , mode) as File:
        File.write(text)
        if back_salsh:
            File.write('\n')
        File.close()

def writer_DB (table:str , w_values , values_r , database = values.database_bot()):
    SQL = values.sql_connect(db=database)
    if type(values_r) == type('a'):
        values_r = list([values_r])
    if type(w_values) == type('a'):
        w_values = list([w_values])
    cursor = SQL.cursor()
    cursor.execute('INSERT INTO %s (%s) VALUES ("%s")' % (table , ','.join(w_values) , '\",\"'.join(values_r)))
    SQL.commit()
    SQL.close()

def game_loop (karbar):
    from class_bot import defs
    from class_server import server
    from class_card_info import card_info
    import time

    keyboard_game_loop_init = values.game_loop_keyboard_init()
    bot = defs(values.bot_token())
    server = server(karbar)

    t_k = [ [{'text' : 'خروج از بازی' , 'command' : '//exit_game'}] ] # tmp_keyboard
    bot.send_message(karbar.ID , 'وارد سرور شدید زمانی که تعضا به ۷ نفر برسد بازی شروع می شود' , t_k)
    bot.send_message(karbar.ID , 'درحال پیدا کردن سرور' , t_k)
    while server.number <= 6: # صبر کردن برای رسیدن اعضا به تعداد کافی
        for message in bot.get_message():
            if message['from'] == karbar.ID and message['type'] == 'TEXT':
                if message['body'][0:2] == '//':
                    # اجرا کردن دستورات کیبورد #
                    last_command = message['body']
                    if last_command == '//exit_game':
                        if bot.exit_game(karbar , server):
                            return False
                else:
                    bot.send_group(server.all , karbar.name , message['body'] , t_k)

                server.update_values()
                if server.number >= 6:
                    break

    server.any = bot.random_karakter(server.all)
    for har_fard in server.any:
        t_m = card_info(server.any[har_fard])
        bot.send_message(har_fard , t_m , keyboard_game_loop_init) # توضیح درباره نقش

    start_game = time.time()
    for message in bot.get_message(): # زمان صحبت کردن

        for_loop_game(bot , karbar , server , message , keyboard_game_loop_init)

        if time.time() - start_game > 60: # اتمام ۶۰ ثانیه صحبت
            t_m = 'زمان رای گیری فرا رسیده است به مشکوک ترین فرد رای بدهید'
            bot.send_message(karbar.ID , t_m , keyboard_game_loop_init)
            break

    # اماده کردن کیبورد رای دادن
    keyboard_votes = values.def_keyboard_votes(server.all)

    for message in bot.get_message(): # زمان رای دادن

        message = for_loop_game(bot , karbar , server , message , keyboard_votes)
        if not message:
            break

        if message['body'][0:6] == '//vote_':
            vote = message['body'][6:]





