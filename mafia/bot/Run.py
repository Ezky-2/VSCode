from class_bot import defs
from class_user import user
from lib import *
import values

def main_page (karbar:user):
    
    bot = defs(values.bot_token())
    main_page_keyboard_init = values.main_page_keyboard_init()
    init_message = 'سلام %s عزیز\n لطفا بین گزینه ها انتخاب کن تا من جواب بدم' % karbar.name

    for message in bot.get_message():
        if message['from'] == karbar.ID:
            init_message = 'سلام %s عزیز\n لطفا بین گزینه ها انتخاب کن تا من جواب بدم' % karbar.name

            if message['type'] == 'TEXT':
                txt = message['body']
                if txt == '//start_game_main_page':
                    bot.start_game(karbar)
                elif txt == '//change_name_main_page':
                    if bot.change_name(karbar):
                        karbar.update_values()
                elif txt == '//amtiaz_ha_main_page':
                    bot.amtiaz_hai_karbar(karbar)
                elif txt == '//delete_data_main_page':
                    if bot.reset_rank(karbar.ID):
                        karbar = user(karbar.ID)
                elif txt == '//best_gamer_main_page':
                    bot.show_best_gamer(karbar , main_page_keyboard_init)
                elif txt == '//help_about_game':
                    bot.help_about_game(karbar , main_page_keyboard_init)
                bot.change_keyboard(karbar.ID , main_page_keyboard_init)

            else:
                bot.send_message(karbar.ID , 'در پیام ارسال شده مشکلی وجود دارد لطفا از کیبورد استفاده کنید' , main_page_keyboard_init)

            bot.send_message(karbar.ID , init_message , main_page_keyboard_init)

main_page(user(values.me_token()))
