from aiogram import Bot, Dispatcher, types, executor

TOKEN = '8355754378:AAHYVOfkDk21mEgigVAbqr9Xf_3cXhIRh7s'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Done')

@dp.message_handler(commands='start')
async def starter(message: types.Message):
    await message.answer(text='Добро пожаловать! Я смогу подобрать комплектующие для вашего компьютера.')






if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)