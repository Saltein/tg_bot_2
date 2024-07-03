"""text for tg_bot"""


class txt_reg:
    """
    A class representing text for use in bot scripts

    IMPORTANT: The text is mainly before registration.py and during registration.py

    Example of using a class:
    """
    welcome = 'Привет!'
    mistake = "Упс... Ошибочка вышла 🤷‍♂️"


class txt_mistakes:
    fool_use_buttons = "Пожалуйста, используй предложенные кнопки!"
    name_mistake = "Пожалуйста, введи настоящее имя, на русском\nНапример Иван"
    phone_mistake = "Пожалуйста, введи корректный номер телефона\nНапример 88005003030!"
    email_mistake = "Пожалуйста, введи корректный адрес электронной почты\nНапример ivanivanov@gmail.com!"


class txt_main_menu:
    section_main_menu = "Раздел: Главное меню"
    section_profile_menu = "Раздел: Профиль"
    section_my_orders_menu = "Раздел: Мои заказы"


class txt_profile_menu:
    what_to_change = "Что ты хочешь изменить?"

    ask_name = "Отправь свое настоящее имя, на русском\nНапример Иван"
    ask_email = "Отправь свою почту текстом\nНапример ivanivanov@gmail.com"
    ask_phone = "Отправь свой номер телефона текстом\nНапример 88005003030"

    name_confirmation = "Ты уверен, что тебя зовут"
    email_confirmation = ('Ты уверен, что "', '" - твоя почта?')
    phone_confirmation = ('Ты уверен, что "', '" - твой номер телефона?')