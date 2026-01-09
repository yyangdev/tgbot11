import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

BOT_TOKEN = "8529391469:AAE-sDSOawB-v4YErjZ1k1y7Y6ILu_G749Q"
ADMIN_IDS = [7529224052, 5556758293]

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command('rules'))
async def rules_cmd(message: types.Message):
    text = '''
<b>Правила предложки новостей</b>

<b>🔍Принимаем материалы по темам:</b>
Игры: релизы, обновления, анонсы, инсайды
Программирование: новые движки, фреймворки, библиотеки, уязвимости
Железо: анонсы GPU/CPU, тесты, утечки, технологии

<b>❌Строго запрещено:</b>
Спам и кликбейтные заголовки
Фейковые новости и недостоверная информация
Материалы для взрослых (18+)
Контент, нарушающий авторские права
Оскорбления, дискриминация, разжигание ненависти

<i>Новость проходит модерацию перед публикацией в канале @PixByteOff.</i>
'''
    await message.answer(text, parse_mode="HTML")

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    text = """
<b>Добро пожаловать в предложку новостей для канала Pixbyte.</b>

Перед отправкой поста ознакомтесь с правилами /rules

Ваша новость будет опубликована в тгк @PixByteOff"""
    await message.answer(text, parse_mode="HTML")

@dp.message(F.text)
async def forward_to_admin(message: types.Message):
    if message.text.startswith('/'):
        return
    
    user_info = f"От: @{message.from_user.username}\nID: {message.from_user.id}\nИмя: {message.from_user.full_name}"
    admin_message = f"📨 Новая новость:\n\n{message.text}\n\n{user_info}"
    
    for admin_id in ADMIN_IDS:
        try:
            await bot.send_message(admin_id, admin_message)
        except:
            pass
    
    await message.answer("✅ Новость отправлена админам на проверку")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main()) 