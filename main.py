import time
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import  InlineKeyboardButton, InlineKeyboardMarkup

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
#SIMPLE KEYBOARD


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




#INLINE KEYBOARD 1 of 5

ikb = InlineKeyboardMarkup(row_width=2)


ikb1 = InlineKeyboardButton(text='Процессор',
                            url='https://market.yandex.ru/category/protsessory-amd-ryzen-5-7600?clid=1601&utm_source_service=web&utm_source=yandex&utm_medium=search&utm_campaign=ymp_dp_cehac_fake_search_newurls_adv_dyb_search_rus&utm_content=cid:701918568%7Cgid:5619853137%7Caid:1881281717801600334%7Cph:205619853137%7Cpt:premium%7Cpn:1%7Csrc:none%7Cst:search%7Crid:205619853137%7Ccgcid:0&yclid=5947855703007559679&baobab_event_id=mhf6pnxpws&wprid=1761935170782041-7977839964650241333-balancer-l7leveler-kubr-yp-vla-171-BAL&src_pof=1601&icookie=gLMvhIxggMi8An21kZFsRzWSxTTgWzsKTybQJvq9Fmq2H6PwpuafDq9NKyWZ8s3aaJ%252FvF1u%252B2w3lhKsTsqpgfpcNTK4%253D')

ikb2 = InlineKeyboardButton(text='Материнская плата',
                            url='https://market.yandex.ru/search?text=ASUS%20PRIME%20B650M-A&rs=eJwzEv7EKMDBKLDwEKsEg0bjcVaNVUdYATpTBfI%2C')

ikb3 = InlineKeyboardButton(text='Оперативная память',
                            url='https://market.yandex.ru/search?text=16%20GB%20DDR5%205200MHz%20(2×8%20GB)&rs=eJwzEv7EKMDBKLDwEKsEg0bjcVaN5908ADqfBf0%2C')

ikb4 = InlineKeyboardButton(text='Видеокарта',
                            url='https://market.yandex.ru/search?text=Интегрированная%20графика%20Radeon%20видеокарпта&rs=eJwz2sfIwSi0gJHL-8KMC3svNl3YemHzxYYLO4B434VNFzZc2AuEGy72K4CFN1xsubDjwq4LGxSCElNS8_MUgEp2XNgC1LQPJApUsR9oxAYhT6oYBjJKYYKfxklGA8YAxk-MIhyMAgsPsUowaDQeZ9V43s2jseoIKwBhhXFD')

ikb5 = InlineKeyboardButton(text='SSD накопитель',
                            url='https://market.yandex.ru/search?text=1%20TB%20NVMe%20PCIe%204.0&rs=eJwzEv_EKMLBKLDwEKsEg0bjcVaNz2dYNRYdYgUAWQ0H3A%2C%2C')

ikb6 = InlineKeyboardButton(text='Блок питания',
                            url='https://market.yandex.ru/search?text=650W%2080%2B%20Bronze&rs=eJwzkv7EKMHBKLDwEKsEg0bjcVaNjUdZNc6eZtV41s0DAHwMCXQ%2C')

ikb7 = InlineKeyboardButton(text='Корпус',
                            url='https://market.yandex.ru/search?text=MIDI-Tower%20с%20базовой%20вентиляцией&rs=eJwzMvjEqMvBKLDwEKsEg0bjcVaNs6dZNZ5382g8A-LVJ1k1fpxi1Xj_6gGzxqojrBobj7ICALidE1M%2C')

ikb8 = InlineKeyboardButton(text='Кулер процессора',
                            url='https://market.yandex.ru/search?text=Боксовый%20кулер&rs=eJwz0v7EqMHBKLDwEKsEg0bjcVaNZ908Gs-BuOcoq8b9I6waZ0-zaiw6xKqx6ggrAE83EBE%2C')

ikb.add(ikb1).add(ikb2).add(ikb3).add(ikb4).add(ikb5).add(ikb6).add(ikb7).add(ikb8)

#INLINE KEYBOARD 2 of 5

ikb_2 = InlineKeyboardMarkup(row_width=2)


ikb_21 = InlineKeyboardButton(text='Процессор',
                              url = 'https://market.yandex.ru/search?text=AMD%20Ryzen%207%207700X&hid=91019&rs=eJwzms-oVMQl6OjrohBUWZWap2CuYG5uYBAhsOn4M0GBY48eMiuxcDAIcINJBiSSGVlEgyEL04gqDlMDQ0sLC2PDKjYzU0MzA-MGxu7jrF2MTBwMVSwcQOYGRoZPjBwcDBIMCkDeX8Z5D4_u62Vq-RJgP5Vpb_AluxVMQGEAUawoxg%2C%2C&rt=11&glfilter=7893318%3A651603&glfilter=37331890%3A50198831')

ikb_22 = InlineKeyboardButton(text='Материнская плата',
                              url = 'https://market.yandex.ru/search?text=ASUS%20TUF%20GAMING%20B650-PLUS%20WIFI&hid=91020&rs=eJwz0qhi4eg5zvqJkYODQYJBAcj8y_jj0dx9vUxMGk72U5nYvsrbr2ACCgMAHiwOKw%2C%2C&rt=9')

ikb_23 = InlineKeyboardButton(text='Оперативная память',
                              url = 'https://market.yandex.ru/search?text=32%20GB%20DDR5%205600MHz%20(2×16%20GB)&hid=191211&rs=eJwz0qhi4Xh9lfsTIwcHgwSDApD5l1Fk8oZ9vUwlHDr2U5kqUpTtVzABhQEncw6F&rt=9')

ikb_24 = InlineKeyboardButton(text='Видеокарта',
                              url = 'https://market.yandex.ru/search?text=NVIDIA%20GeForce%20RTX%204060%208GB&hid=91031&rs=eJwz0qhi4Zh-nPUTIwcHgwSDApD5l5EjZMm-Xqar583tpzIp3VG2X8EEFAYAF_8OSw%2C%2C&rt=9')

ikb_25 = InlineKeyboardButton(text='SSD накопитель',
                              url = 'https://market.yandex.ru/search?text=1%20TB%20NVMe%20PCIe%204.0&hid=16309373&hid=16309374&rs=eJwzMqhi5fi74zH7J0Y-DgYJBgUQW-EfkPjL-OH_gX29TCcZNOynMrn9F7NfwQSSBAALuBXN&rt=9')

ikb_26 = InlineKeyboardButton(text='Блок питания',
                              url = 'https://market.yandex.ru/search?text=750W%2080%2B%20Gold&hid=857707&rs=eJwz0qhi4Xi9xuQTIwcHgwSDApD5l3FD_KN9vUybvETtpzLND-WwX8EEFAYAOacPhQ%2C%2C&rt=9')

ikb_27 = InlineKeyboardButton(text='Корпус',
                              url = 'https://market.yandex.ru/search?text=MIDI-Tower%20с%20сетчатым%20фронталом&hid=91028&rs=eJwz0qhi4ZhynPUTIwcHgwSDApD5l1FC7P2-XiaveB77qUxzu1jsVzABhQEJuA1D&rt=9')

ikb_28 = InlineKeyboardButton(text='Кулер процессора',
                              url = 'https://market.yandex.ru/search?text=Башенный%20воздушный%20кулер&hid=818965&rs=eJwz0qhi4Zj6z_ATIwcHgwSDApD5l5Hv_aJ9vUzG_kb2U5n2H9SyX8EEFAYAL-cPbw%2C%2C&rt=9')

ikb_2.add(ikb_21).add(ikb_22).add(ikb_23).add(ikb_24).add(ikb_25).add(ikb_26).add(ikb_27).add(ikb_28)

#INLINE KEYBOARD 3 OF 5

L_ikb_3 = InlineKeyboardMarkup(row_width=2)

ikb_31 = InlineKeyboardButton(text='Процессор',
                              url = 'https://market.yandex.ru/search?text=Intel%20Core%20i3%20%2F%20AMD%20Ryzen%203&hid=91019&rs=eJwz0qhi4eg-zvqJkYODQYJBAcj8y-g0j2F_L1PPXm77qUz3uJ_ZrWACCgMAETsOLg%2C%2C&rt=9')

ikb_32 = InlineKeyboardButton(text='Память',
                              url = 'https://market.yandex.ru/search?text=8-16%20GB%20DDR4&hid=191211&rs=eJwz0qhi4Xh9lfsTIwcHgwSDApD5l1HtQ8O-XqbFzG72U5nMeSztVzABhQEr_w6F&rt=9')

ikb_33 = InlineKeyboardButton(text='Накопитель',
                              url = 'https://market.yandex.ru/search?text=SSD%20256-512%20GB&hid=16309373&hid=16309374&hid=91033&rs=eJwzcqpi5fi74zH7J0YFDgaBhYdYJRgUQHyFfyBi5nFWDRBPA8T7yzihYfa-XqaD_Xb2U5k2vFe1X8EEkgQA1ewefw%2C%2C&rt=9')

ikb_34 = InlineKeyboardButton(text='Видеокарта',
                              url = 'https://market.yandex.ru/search?text=Интегрированная%20(Intel%20UHD%20%2F%20AMD%20Radeon%20Graphics)&hid=91031&hid=91011&hid=91013&rs=eJwzcqhi4Zh-nPUTowIHg8DCQ6wSDApArkIzELceZ9UAsjVANJD_l3GjlPz-XiYPs-N2U5m-xu2xW8EElAYA0fYXjw%2C%2C&rt=9')

ikb_35 = InlineKeyboardButton(text='Блок питания',
                              url = 'https://market.yandex.ru/search?text=450-550W&hid=857707&rs=eJwz0qhi4Xi9xuQTIwcHgwSDApD5l7FE9f2-XqavrSL2U5l0V_6wW8EEFAYAPWwQag%2C%2C&rt=9')

L_ikb_3.add(ikb_31).add(ikb_32).add(ikb_33).add(ikb_34).add(ikb_35)


#INLINE KEYBOARD 4 OF 5

A_ikb_4 = InlineKeyboardMarkup(row_width=2)

ikb_41 = InlineKeyboardButton(text='Процессор',
                              url = 'https://market.yandex.ru/search?text=Intel%20Core%20i5%20%2F%20AMD%20Ryzen%205&hid=91019&rs=eJwz0qhi4eg-zvqJkYODQYJBAcj8y7hm9dd9vUz1OVz2U5lWnf9vt4IJKAwALMsP4w%2C%2C&rt=9')

ikb_42 = InlineKeyboardButton(text='Память',
                              url = 'https://market.yandex.ru/search?text=16%20GB%20DDR4&hid=191211&rs=eJwz0qhi4Xh9lfsTIwcHgwSDApD5l1FkTs2-XibTaS72U5kOStvar2ACCgMAKpUO2w%2C%2C&rt=9')

ikb_43 = InlineKeyboardButton(text='Накопитель',
                              url = 'https://market.yandex.ru/search?text=SSD%20512%20GB%20NVMe%20%2B%20HDD%201%20TB&hid=16309373&hid=16309374&hid=91033&rs=eJwzMqli5fi74zH7J0YhDgYJBgUQW-EfiJh5nPUv478ylv29TCpz_tlNZXrU_t5uBRNIAQBYqBfs&rt=9')

ikb_44 = InlineKeyboardButton(text='Видеокарта',
                              url = 'https://market.yandex.ru/search?text=NVIDIA%20GTX%201660%20%2F%20RTX%203060%20%2F%20AMD%20RX%206600&hid=91031&rs=eJwz0qhi4Zh-nPUTIwcHgwSDApD5l7G2lGt_L9PNs3_spjIZxdy0W8EEFAYAJGkPUw%2C%2C&rt=9')

ikb_45 = InlineKeyboardButton(text='Блок питания',
                              url = 'https://market.yandex.ru/search?text=550-650W&hid=857707&rs=eJwz0qhi4Xi9xuQTIwcHgwSDApD5l1Fg9Z59vUyxR_TtpzJNniBsv4IJKAwANGEPhA%2C%2C&rt=9')

ikb_46 = InlineKeyboardButton(text='Монитор',
                              url = 'https://market.yandex.ru/search?text=24-27%22%20Full%20HD%20IPS&hid=91052&rs=eJwz0qhi4VhznPUTIwcHgwSDApD5l3GL3v19vUyVp8TspzJdYuOyX8EEFAYAJGgOig%2C%2C&rt=9')

A_ikb_4.add(ikb_41).add(ikb_42).add(ikb_43).add(ikb_44).add(ikb_45).add(ikb_46)


#INLINE KEYBOARD 5 OF 5

E_ikb_5 = InlineKeyboardMarkup(row_width=2)

ikb_51 = InlineKeyboardButton(text='Процессор',
                              url = 'https://market.yandex.ru/search?text=Intel%20Core%20i7%20%2F%20AMD%20Ryzen%207&hid=91019&rs=eJwz0qhi4eg-zvqJkYODQYJBAcj8y8hx7v6-XqZX7JL2U5n4tNjtVzABhQEQjQ0p&rt=9')

ikb_52 = InlineKeyboardButton(text='Память',
                              url = 'https://market.yandex.ru/search?text=32%20GB%20DDR4%2FDDR5&hid=191211&rs=eJwz0qhi4Xh9lfsTIwcHgwSDApD5l_GN7b19vUxHEsTspzL5J3Lbr2ACCgMAPA4Pgw%2C%2C&rt=9')

ikb_53 = InlineKeyboardButton(text='Видеокарта',
                              url = 'https://market.yandex.ru/search?text=NVIDIA%20RTX%204060%20%2F%204070%20%2F%20AMD%20RX%207700%20XT&hid=91031&rs=eJwz0qhi4Zh-nPUTIwcHgwSDApD5l9FLim1_L9MRexb7qUx-4vftVjABhQECRQ0E&rt=9')

ikb_54 = InlineKeyboardButton(text='Накопитель',
                              url = 'https://market.yandex.ru/search?text=SSD%201%20TB%20NVMe%20%2B%20HDD%202%20TB&hid=16309373&hid=16309374&hid=91033&rs=eJwzMqli5fi74zH7J0YhDgYJBgUQW-EfiJh5nPUv4xK-Z_t6mc44i9lPZZq4ltl-BRNIAQBJchZd&rt=9')

ikb_55 = InlineKeyboardButton(text='Блок питания',
                              url = 'https://market.yandex.ru/search?text=650-750W&hid=857707&rs=eJwz0qhi4Xi9xuQTIwcHgwSDApD5l_GE0sF9vUxL96jZT2WapCBhv4IJKAwAOREPgw%2C%2C&rt=9')

ikb_56 = InlineKeyboardButton(text='Монитор',
                              url = 'https://market.yandex.ru/search?text=27%22%202K%20144Hz%20IPS&hid=91052&rs=eJwz0qhi4VhznPUTIwcHgwSDApD5l1Hj3d19vUz_X4rZT2W6pc5tv4IJKAwAMqkPiw%2C%2C&rt=9')

E_ikb_5.add(ikb_51).add(ikb_52).add(ikb_53).add(ikb_54).add(ikb_55).add(ikb_56)


#INLINE KEYBOARD 5 OF 5

M_ikb = InlineKeyboardMarkup(row_width=2)
d_m = InlineKeyboardButton(text='Второй монитор',
                           url='https://market.yandex.ru/search?text=Dell%20P2422H%20(24%22%20IPS%20Full%20HD)&hid=91052&rs=eJwz0qhi4VhznPUTIwcHgwSDApD5l5Fh6819vUwaTQb2U5k2THxtt4IJKAwAIagPIQ%2C%2C&rt=9')
M_ikb.add(d_m)

DM_ikb = InlineKeyboardMarkup(row_width=2)
l_m = InlineKeyboardButton(text='Второй монитор',
                           url='https://market.yandex.ru/search?text=Dell%20U2723QE%20(27%22%204K%20IPS)&hid=91052&rs=eJwz0qhi4VhznPUTIwcHgwSDApD5l3Hawk37epl-_He0n8pUFMdtv4IJKAwAM4QPig%2C%2C&rt=9')
DM_ikb.add(l_m)

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
    await bot.send_message(chat_id=message.from_user.id,
                           text=Game_low,
                           reply_markup=L_ikb_3)

@dp.message_handler(commands='average')
async def average_price(message: types.Message):
    await message.answer(text='Оптимальные комплектующие для средней ценовой категории:')
    time.sleep(1)
    await  bot.send_message(chat_id=message.from_user.id,
                           text=Game_average,
                           reply_markup=A_ikb_4)

@dp.message_handler(commands='expensive')
async def expensive_price(message: types.Message):
    await message.answer(text='Оптимальные комплектующие для высокой ценовой категории:')
    time.sleep(1)
    await bot.send_message(chat_id=message.from_user.id,
                           text=Game_expensive,
                           reply_markup=E_ikb_5)




@dp.message_handler(commands='optimal')
async def optimal_price(message: types.Message):
    await message.answer(text='Лучшие комплектующие в этой ценовой категории:')
    time.sleep(1)
    await bot.send_message(chat_id=message.from_user.id,
                            text=WorkingOptionalConfig,
                           reply_markup=ikb)
    time.sleep(3)
    await bot.send_message(chat_id=message.from_user.id,
                           text='Так же для удобства можно взять второй монитор',
                           reply_markup=M_ikb)

@dp.message_handler(commands='high_priced')
async def high(message: types.Message):
    await message.answer(text='Лучшие комплектующие в этой ценовой категории:')
    time.sleep(1)
    await bot.send_message(chat_id=message.from_user.id,
                            text=WorkingHConfig,
                           reply_markup=ikb_2)
    time.sleep(3)
    await bot.send_message(chat_id=message.from_user.id,
                           text='Так же для удобства можно взять второй монитор',
                           reply_markup=DM_ikb)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)