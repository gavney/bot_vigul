# -*- coding: utf-8 -*-
from vk_api.keyboard import VkKeyboard, VkKeyboardColor 

keyboard_create = VkKeyboard(one_time=False, inline=False)

keyboard_create.add_button(
    label="Начать",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "answer_create"},
)


keyboard_restart = VkKeyboard(one_time=False, inline=False)

keyboard_restart.add_button(
    label="Использовать сохранённую анкету",
    color=VkKeyboardColor.POSITIVE,
    payload={"type": "answer_create"},
)

keyboard_restart.add_line()

keyboard_restart.add_button(
    label="Заполнить заново",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "answer_create"},
)


keyboard_answer_4 = VkKeyboard(one_time=False, inline=False)

keyboard_answer_4.add_button(
    label="Мужской",
    color=VkKeyboardColor.POSITIVE,
    payload={"type": "answer_create"},
)

keyboard_answer_4.add_button(
    label="Женский",
    color=VkKeyboardColor.POSITIVE,
    payload={"type": "answer_create"},
)

keyboard_answer_4.add_line()

keyboard_answer_4.add_callback_button(
    label="Назад",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "answer_change_back"},
)


keyboard_change = VkKeyboard(one_time=False, inline=False)

keyboard_change.add_callback_button(
    label="Назад",
    color=VkKeyboardColor.SECONDARY,
    payload={"type": "answer_change_back"},
)



keyboard_answer = VkKeyboard(one_time=False, inline=False)

keyboard_answer.add_button(
    label="Нет",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "answer_NO"},
)

keyboard_answer.add_button(
    label="Да",
    color=VkKeyboardColor.POSITIVE,
    payload={"type": "answer_YES"},
)

keyboard_answer.add_line()

keyboard_answer.add_callback_button(
    label="Назад",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "answer_change_back"},
)



keyboard_answer_12 = VkKeyboard(one_time=False, inline=False)

keyboard_answer_12.add_button(
    label="Нет",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "answer_NO"},
)

keyboard_answer_12.add_button(
    label="Да",
    color=VkKeyboardColor.POSITIVE,
    payload={"type": "answer_YES"},
)

keyboard_answer_12.add_line()

keyboard_answer_12.add_button(
    label="Кусается",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "answer_YES"},
)

keyboard_answer_12.add_line()

keyboard_answer_12.add_callback_button(
    label="Назад",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "answer_change_back"},
)




keyboard_answer_10 = VkKeyboard(one_time=False, inline=False)

keyboard_answer_10.add_button(
    label="Нет",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "answer_NO"},
)

keyboard_answer_10.add_button(
    label="Иногда тянет",
    color=VkKeyboardColor.POSITIVE,
    payload={"type": "answer_YES"},
)

keyboard_answer_10.add_line()

keyboard_answer_10.add_button(
    label="Сильно тянет",
    color=VkKeyboardColor.POSITIVE,
    payload={"type": "answer_YES"},
)

keyboard_answer_10.add_line()

keyboard_answer_10.add_callback_button(
    label="Назад",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "answer_change_back"},
)



keyboard_answer_11 = VkKeyboard(one_time=False, inline=False)

keyboard_answer_11.add_button(
    label="Нет",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "answer_NO"},
)

keyboard_answer_11.add_button(
    label="Иногда подбирает",
    color=VkKeyboardColor.POSITIVE,
    payload={"type": "answer_YES"},
)

keyboard_answer_11.add_line()

keyboard_answer_11.add_button(
    label="Часто подбирает",
    color=VkKeyboardColor.POSITIVE,
    payload={"type": "answer_YES"},
)

keyboard_answer_11.add_line()

keyboard_answer_11.add_callback_button(
    label="Назад",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "answer_change_back"},
)


keyboard_skip = VkKeyboard(one_time=False, inline=False)

keyboard_skip.add_callback_button(
    label="Назад",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "answer_change_back"},
)



keyboard_answer_21 = VkKeyboard(one_time=False, inline=False)

keyboard_answer_21.add_button(
    label="30 минут - 400 рублей",
    color=VkKeyboardColor.POSITIVE,
    payload={"type": "answer_NO"},
)

keyboard_answer_21.add_button(
    label="1 час - 600 рублей",
    color=VkKeyboardColor.POSITIVE,
    payload={"type": "answer_YES"},
)

keyboard_answer_21.add_line()

keyboard_answer_21.add_button(
    label="1,5 часа - 800 рублей",
    color=VkKeyboardColor.POSITIVE,
    payload={"type": "answer_YES"},
)

keyboard_answer_21.add_line()

keyboard_answer_21.add_callback_button(
    label="Назад",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "answer_change_back"},
)




keyboard_answer_23 = VkKeyboard(one_time=False, inline=False)

keyboard_answer_23.add_button(
    label="На первом пробном выгуле",
    color=VkKeyboardColor.POSITIVE,
    payload={"type": "answer_NO"},
)

keyboard_answer_23.add_line()

keyboard_answer_23.add_button(
    label="Хочу связаться до первого выгула",
    color=VkKeyboardColor.POSITIVE,
    payload={"type": "answer_YES"},
)

keyboard_answer_23.add_line()

keyboard_answer_23.add_button(
    label="Знакомство не требуется",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "answer_YES"},
)

keyboard_answer_23.add_line()

keyboard_answer_23.add_callback_button(
    label="Назад",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "answer_change_back"},
)




keyboard_answer_24 = VkKeyboard(one_time=False, inline=False)

keyboard_answer_24.add_button(
    label="Дома встретят",
    color=VkKeyboardColor.SECONDARY,
    payload={"type": "answer_NO"},
)

keyboard_answer_24.add_line()

keyboard_answer_24.add_button(
    label="Ключи будут в тайном месте",
    color=VkKeyboardColor.SECONDARY,
    payload={"type": "answer_YES"},
)

keyboard_answer_24.add_line()

keyboard_answer_24.add_button(
    label="Передам ключи выгульщику",
    color=VkKeyboardColor.SECONDARY,
    payload={"type": "answer_YES"},
)

keyboard_answer_24.add_line()

keyboard_answer_24.add_button(
    label="Ключи уже у вас",
    color=VkKeyboardColor.SECONDARY,
    payload={"type": "answer_YES"},
)

keyboard_answer_24.add_line()

keyboard_answer_24.add_callback_button(
    label="Назад",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "answer_change_back"},
)


keyboard_answer_29 = VkKeyboard(one_time=False, inline=False)

keyboard_answer_29.add_button(
    label="В любое время",
    color=VkKeyboardColor.POSITIVE,
    payload={"type": "answer_NO"},
)

keyboard_answer_29.add_line()

keyboard_answer_29.add_callback_button(
    label="Назад",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "answer_change_back"},
)

keyboard_answer_result = VkKeyboard(one_time=True, inline=False)

keyboard_answer_result.add_callback_button(
    label="Закончить",
    color=VkKeyboardColor.POSITIVE,
    payload={"type": "result"},
)

keyboard_answer_21 = VkKeyboard(one_time=True, inline=False)

keyboard_answer_21.add_button(
    label="Не нужно",
    color=VkKeyboardColor.POSITIVE,
    payload={"type": "result"},
)

keyboard_answer_21.add_line()

keyboard_answer_21.add_callback_button(
    label="Назад",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "answer_change_back"},
)




