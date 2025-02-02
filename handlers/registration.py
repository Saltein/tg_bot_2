from datetime import datetime
from datetime import time
from datetime import timedelta
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import ts
from loader import bot
from loader import dp
from loader import BASE_URL
from data import *
from states import *
from keyboards import *
from services import *
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import requests
import re


async def startCommand(message: types.Message):
    """
    startCommand function
    """
    global dataAboutUser

    if not Authentication(message.from_user.id):
        await bot.send_message(dataAboutUser[message.from_user.id]["user_tg_id"], f'{txt_reg.mistake}',
                               reply_markup=GeneralKeyboards.single_btn_command_start)
        return


    await bot.send_message(dataAboutUser[message.from_user.id]["user_tg_id"], f'{txt_reg.welcome}',
                           reply_markup=GeneralKeyboards.single_btn_registration)
    await UserState.start_register.set()

async def fio(message: types.Message):
    global dataAboutUser
    if message.text == "Зарегистрироваться":
        await UserState.get_dateAboutUser_fio.set()
        await bot.send_message(message.from_user.id, f'{txt_reg.fio}', reply_markup=ReplyKeyboardRemove())
    else:
        await bot.send_message(message.from_user.id, f'Ипользуйте предложенные кнопки, пожалуйста',
                               reply_markup=GeneralKeyboards.single_btn_command_start)

async def ask_phone(message: types.Message):
    global dataAboutUser
    if re.fullmatch(r'[А-Яа-яЁё\s]+', message.text):
        dataAboutUser[message.from_user.id]["name"] = message.text
        await UserState.get_dateAboutUser_number.set()
        await bot.send_message(message.from_user.id, f'{txt_reg.numb}')
    else:
        await bot.send_message(message.from_user.id, f'Неверный формат имени. Пожалуйста, введите имя, содержащее только кириллицу.')
        await UserState.get_dateAboutUser_fio.set() 

async def ask_mail(message: types.Message):
    global dataAboutUser
    if message.text.startswith('+7') or message.text.startswith('8'):
        dataAboutUser[message.from_user.id]["phone"] = message.text
        await UserState.get_dateAboutUser_mail.set()
        await bot.send_message(message.from_user.id, f'{txt_reg.mail}')
    else:
        await bot.send_message(message.from_user.id, f'Введён неверный формат номера')
        await UserState.get_dateAboutUser_number.set() 

async def go_to_menu(message: types.Message):
    global dataAboutUser
    if "@" in message.text:
        dataAboutUser[message.from_user.id]["mail"] = message.text
        await bot.send_message(message.from_user.id, f'Все прошло успешно')
        # Add func to go to the menu
    else:
        await bot.send_message(message.from_user.id, f'Введён неверный формат почты')
        await UserState.get_dateAboutUser_mail.set()  
        
    
    
    
    #Запрос на POST этих данных
    try:
        userData = requests.post(f'{BASE_URL}/client/registrations',json={'tg_id':dataAboutUser[message.from_user.id]["user_tg_id"],
                                                               'name':dataAboutUser[message.from_user.id]["name"],
                                                              'phone':dataAboutUser[message.from_user.id]["phone"],
                                                              'email':dataAboutUser[message.from_user.id]["mail"]})
    except Exception as e:
        log_error(e)
    



# _ _ _ Packing the registration.py of handlers into functions by groups _ _ _

def startReg(dp=dp):
    dp.register_message_handler(startCommand, commands=["start"], state="*")
    dp.register_message_handler(fio, state=UserState.start_register)
    dp.register_message_handler(ask_phone, state=UserState.get_dateAboutUser_fio)
    dp.register_message_handler(ask_mail, state=UserState.get_dateAboutUser_number)
    dp.register_message_handler(go_to_menu, state=UserState.get_dateAboutUser_mail)
