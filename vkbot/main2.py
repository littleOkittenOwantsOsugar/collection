import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


def write_msg(user_id, message, random_id):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.getrandbits(64)})


random_id = random.getrandbits(64)
# API-ключ созданный ранее
token = "vash token"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text
            if request == "привет":
                write_msg(event.user_id, "Хай", random_id)
            elif request == "пока":
                write_msg(event.user_id, "Пока((", random_id)
            else:
                write_msg(event.user_id, "Не понял вашего ответа...", random_id)