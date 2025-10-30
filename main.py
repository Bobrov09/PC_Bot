import time
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram import Bot, Dispatcher, types, executor


TOKEN = '8355754378:AAHYVOfkDk21mEgigVAbqr9Xf_3cXhIRh7s'


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

WorkingOptionalConfig = '''
Процессор: AMD Ryzen 5 7600

Материнская плата: ASUS PRIME B650M-A

Оперативная память: 16 GB DDR5 5200MHz (2×8 GB)

Видеокарта: Интегрированная графика Radeon

SSD накопитель: 1 TB NVMe PCIe 4.0

Блок питания: 650W 80+ Bronze

Корпус: MIDI-Tower с базовой вентиляцией

Кулер процессора: Боксовый кулер 
'''

WorkingHConfig = '''
Процессор: AMD Ryzen 7 7700X

Материнская плата: ASUS TUF GAMING B650-PLUS WIFI

Оперативная память: 32 GB DDR5 5600MHz (2×16 GB)

Видеокарта: NVIDIA GeForce RTX 4060 8GB

SSD накопитель: 1 TB NVMe PCIe 4.0

Блок питания: 750W 80+ Gold

Корпус: MIDI-Tower с сетчатым фронталом

Кулер процессора: Башенный воздушный кулер
'''

Game_low = '''
Процессор: Intel Core i3 / AMD Ryzen 3

Память: 8-16 GB DDR4

Накопитель: SSD 256-512 GB

Видеокарта: Интегрированная (Intel UHD / AMD Radeon Graphics)

Блок питания: 450-550W
'''

Game_average = '''
Процессор: Intel Core i5 / AMD Ryzen 5

Память: 16 GB DDR4

Накопитель: SSD 512 GB NVMe + HDD 1 TB

Видеокарта: NVIDIA GTX 1660 / RTX 3060 / AMD RX 6600

Блок питания: 550-650W

Монитор: 24-27" Full HD IPS
'''

Game_expensive = '''
Процессор: Intel Core i7 / AMD Ryzen 7

Память: 32 GB DDR4/DDR5

Накопитель: SSD 1 TB NVMe + HDD 2 TB

Видеокарта: NVIDIA RTX 4060 / 4070 / AMD RX 7700 XT

Блок питания: 650-750W

Монитор: 27" 2K 144Hz IPS
'''



kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b1 = KeyboardButton('/Working')
b2 = KeyboardButton('/ForMySelf')
kb.add(b1).add(b2)


kb2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
bb1 = KeyboardButton('/low')
bb2 = KeyboardButton('/average')
bb3 = KeyboardButton('/expensive')
kb2.add(bb1).add(bb2).add(bb3)

kb3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
c1 = KeyboardButton('/optimal')
cc2 = KeyboardButton('/high_priced')
kb3.add(c1).add(cc2)

async def on_startup(_):
    print('Done')



@dp.message_handler(commands='start')
async def starter(message: types.Message):
    await message.answer(text='Добро пожаловать! Я помогу подобрать комплектующие для вашего компьютера.')
    time.sleep(2)
    await message.answer(text='С какой целью вы хотите пользоваться ПК?', reply_markup=kb)





@dp.message_handler(commands='Working')
async def starter(message: types.Message):
    await message.answer(text='Для програмирования подойдут средние комплектующие.')
    time.sleep(2)
    await message.answer(text='Но есть работы, в которых необходимы хорошо подобранные компоненты - для них подойдет дорогая ценовая категория.'
                         ,reply_markup=kb3)

@dp.message_handler(commands='ForMySelf')
async def starter(message: types.Message):
    await message.answer(text='Для подбора комплектующих нужно определить ваш бюджет')
    time.sleep(2)
    await message.answer(text='Оптимальные ценовые категории:',
                         reply_markup=kb2)




@dp.message_handler(commands='low')
async def low_price(message: types.Message):
    await message.answer(text='Оптимальные комплектующие для низкой ценовой категории:')
    time.sleep(1)
    await message.answer(text=Game_low)

@dp.message_handler(commands='average')
async def average_price(message: types.Message):
    await message.answer(text='Оптимальные комплектующие для средней ценовой категории:')
    time.sleep(1)
    await message.answer(text=Game_average)

@dp.message_handler(commands='expensive')
async def expensive_price(message: types.Message):
    await message.answer(text='Оптимальные комплектующие для высокой ценовой категории:')
    time.sleep(1)
    await message.answer(text=Game_expensive)





@dp.message_handler(commands='optimal')
async def optimal_price(message: types.Message):
    await message.answer(text='Лучшие комплектующие в этой ценовой категории:')
    time.sleep(1)
    await message.answer(text=WorkingOptionalConfig)

@dp.message_handler(commands='high_priced')
async def high(message: types.Message):
    await message.answer(text='Лучшие комплектующие в этой ценовой категории:')
    time.sleep(1)
    await message.answer(text=WorkingHConfig)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)