import time
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram import Bot, Dispatcher, types, executor

TOKEN = '8355754378:AAHYVOfkDk21mEgigVAbqr9Xf_3cXhIRh7s'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b1 = KeyboardButton('/Working')
b2 = KeyboardButton('/ForYourSelf')
kb.add(b1).add(b2)

async def on_startup(_):
    print('Done')

@dp.message_handler(commands='start')
async def starter(message: types.Message):
    await message.answer(text='Добро пожаловать! Я помогу подобрать комплектующие для вашего компьютера.')
    time.sleep(2)
    await message.answer(text='С какой целью вы хотите пользоваться ПК?', reply_markup=kb)

@dp.message_handler(commands='Working')
async def starter(message: types.Message):
    await message.answer(text='Для работы с программированием требуются минимальные комплектующие.')
    time.sleep(2)
    await message.answer(text='Они подбираются опираясь на бюджет пользователья. Выберите подходящий для себя вариант.')
                        # ,reply_markup=kb)


@dp.message_handler(commands='ForYourSelf')
async def starter(message: types.Message):
    await message.answer(text='Для личного использования (дом, семья, развлечения) вот оптимальные конфигурации ПК:')
                        # reply_markup=kb)




if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)