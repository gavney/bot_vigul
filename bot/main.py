# -*- coding: utf-8 -*-
import json

from vk_api import VkApi
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import keyboard_config
from questions import questions_data

GROUP_ID = "221826865"
GROUP_TOKEN = ""
API_VERSION = "5.120"


def save_data(data):
    print(data)
    json_object = json.dumps(data)
 
    with open("users.json", "w") as outfile:
        outfile.write(json_object)


def open_data():
    with open('users.json') as json_file:
        data = json.load(json_file)
        return data


users = open_data()


def main():
    vk_session = VkApi(token=GROUP_TOKEN, api_version=API_VERSION)
    vk = vk_session.get_api()
    longpoll = VkBotLongPoll(vk_session, group_id=GROUP_ID)

    try:
        for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW and event.from_user:
                    user_id = str(event.obj.message["from_id"])
                    
                    if user_id not in users:
                        vk.messages.send(
                            random_id=get_random_id(),
                            peer_id=user_id,
                            keyboard=keyboard_config.keyboard_create.get_keyboard(),
                            message="Напишите 'начать', чтобы заказать выгул"
                        )
                        users.update({user_id: 0})

                    if event.message.text.lower() == "начать":
                        if users.get(user_id) == 0:
                            users.update({user_id: 1})

                        if users.get(user_id) >= len(questions_data):
                            send_message(vk, user_id, "Анкета сохранена.", keyboard_config.keyboard_restart, step=0)

                        if users.get(user_id) > 2 and users.get(user_id) < len(questions_data):
                            send_message(vk, user_id, "Вы уже проходите.", keyboard_config.keyboard_skip, step=0)

                    if event.message.text.lower() == "заполнить заново":
                        users.update({user_id: 1})

                    if event.message.text.lower() == "использовать сохранённую анкету": 
                        users.update({user_id: 26})                                
                        
                    questions = questions_data.get(users.get(user_id))

                    if questions:
                        send_message(vk, user_id, questions[0], questions[1])  
                                
                elif event.type == VkBotEventType.MESSAGE_EVENT:
                    user_id = str(event.object.user_id)

                    vk.messages.sendMessageEventAnswer(
                        event_id=event.object.event_id,
                        user_id=event.object.user_id,
                        peer_id=event.object.peer_id
                    )

                    if event.object.payload.get("type") == "answer_change_back":    
                        if users.get(user_id) > 1:
                            questions = questions_data.get(users.get(user_id) - 2)

                            if questions:
                                send_message(vk, user_id, questions[0], questions[1], -1)  
                    
                    
                    if event.object.payload.get("type") == "result":    
                        vk.messages.send(
                            random_id=get_random_id(),
                            peer_id=event.object.user_id,
                            keyboard=VkKeyboard.get_empty_keyboard(),
                            message="До скорых прогулок ;)"
                        )
                save_data(users)
    except:
        print("ошибка")



def send_message(vk, peer_id, text, keyboard, step = 1):
    if users.get(peer_id) != 0:
    
        users.update({peer_id: users.get(peer_id) + step})

        vk.messages.send(
            random_id=get_random_id(),
            peer_id=peer_id,
            keyboard=keyboard.get_keyboard(),
            message=text
        )

if __name__ == "__main__":
    main()
