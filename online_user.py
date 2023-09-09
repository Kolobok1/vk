import time
import telebot

from headers import session
from online_friends import Online_friends
from user_id import user_id


class Get_online():
        
    # написать смс
    def sms_teleg():

        token='token telegram бота'
        bot=telebot.TeleBot(token)
        bot.send_message(chat_id='id чата куда отправлять sms' , text="Нужный человек online")

    # проверить онлайн
    def check_online(num,wel):
        inf = session.method('users.get', {
            'user_ids': user_id, 
            'fields': 'online',
            'name_case': None,
        })
        
        if inf[0]['online'] == True:
            print('Online')
            
            wel = Online_friends.check_online_friends(wel)
            time.sleep(1)
            if num == False:
                num = Get_online.sms_teleg() # написать смс в телеграмм
                num = True
                
        elif inf[0]['online'] == False:
            print('Offline')
            num = False
        
        return num, wel