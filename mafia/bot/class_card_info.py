import values
SQL = values.sql_connect()

class card_info:

    def __init__ (self , card_id:str):
        cursor = SQL.cursor()
        cursor.execute('SELECT card_about FROM card_info WHERE card_id="%s"' % card_id)
        data = cursor.fetchall()[0]
        self.card_id = card_id
        self.card_about = data[1]
        self.card_name = data[2]
        self.noe_card= data[3]
