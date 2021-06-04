token = "a0db382ab07c3a8889a08b0629590cb6965f0ad09bacc222a7bce06891f594c9ce992cdf5cff1a500f2cc"
GROUP_ID = 200769441

import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType

from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id


class VkBot:
    def write_msg(self, user_id, message):
        random_id = random.getrandbits(64) 
        self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id})


    def __init__(self, token):
        self.vk = vk_api.VkApi(token=token)
        self.longpoll = VkLongPoll(self.vk,mode=vk_api.longpoll.VkLongpollMode.GET_EXTENDED)
        

    def start(self):
        # Основной цикл
        for event in self.longpoll.listen():
            print(event.type)
            # Если пришло новое сообщение
            if event.type == VkEventType.MESSAGE_NEW:
            
                # Если оно имеет метку для меня( то есть бота)
                if event.to_me:
                    self.processor(event)


    #При вступлении в группу нового пользователя
    def sign_in(self,event):


        self.write_msg(event.user_id, "О, ты пришел к нам на помощь?\n Напиши мне свой ник:")

        #нужно будет добавить ник  в какой-то список(?) где он будет ханиться

        self.write_msg(event.user_id, "Привет, *челик_нейм*! Я рад что ты теперь с нами!")
        
    #При выходе из группы 
    #def sign_out(self):

        #Удалить всю инфу по этому пользователю
        # Ну и пафосное сообщение что мы тип скучать будем




    def processor(self, event):
        # Сообщение от пользователя
        request = event.text.lower()
        if request == "клин" or request =="1":
            self.write_msg(event.user_id, "Клинер")
        elif request == "тайп" or request =="2":
            self.write_msg(event.user_id, "Тайпер")
        elif request == "перевод" or request =="3":
            self.write_msg(event.user_id, "Переводчик")
        elif request == "редакт" or request =="4":
            self.write_msg(event.user_id, "Редактор")
        elif request == "эдит" or request =="5":
            self.write_msg(event.user_id, "Эдитор")
        else:
            self.write_msg(event.user_id, "Не поняла вашего ответа...")




                   
bot = VkBot(token)
bot.start()
