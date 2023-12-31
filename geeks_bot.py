from aiogram import Bot, Dispatcher, types, executor
from config import token
from logging import basicConfig, INFO

bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO) #Логгирование телеграм бота

start_keyboards = [
    types.KeyboardButton("О нас"),
    types.KeyboardButton("Курсы"),
    types.KeyboardButton("График работы"),
    types.KeyboardButton("Адрес")
]
start_button = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_keyboards)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}", reply_markup=start_button)
    print(message)

@dp.message_handler(text="О нас")
async def about(message:types.Message):
    await message.answer("""Образовательный центр Geeks (Гикс) был основан Fullstack-разработчиком 
Айдаром Бакировым и Android-разработчиком Нургазы Сулаймановым в 2018-ом году в 
Бишкеке с целью дать возможность каждому человеку, даже без опыта в технологиях, 
гарантированно освоить IT-профессию.

На сегодняшний день более 1200 студентов в возрасте от 12 до 45 лет изучают здесь 
самые популярные и востребованные IT-профессии. 
Филиальная сеть образовательного центра представлена в таких городах, 
как Бишкек, Ош и Кара-Балта.""")

@dp.message_handler(text="График работы")
async def scheduler_time(message:types.Message):
    await message.answer(f"{message.from_user.username} наш график работы\nПН-СБ 10:00-22:00")

@dp.message_handler(text='Адрес')
async def address(message:types.Message):
    await message.answer("Мы находимся по адресу:\nМырзалы Аматова 1Б (БЦ Томирис)")
    await message.answer_location(40.51927293359835, 72.80298008693217)

courses_keyboards = [
    types.KeyboardButton("Backend"),
    types.KeyboardButton("Frontend"),
    types.KeyboardButton("Android"),
    types.KeyboardButton("iOS"),
    types.KeyboardButton("UX/UI"),
    types.KeyboardButton("Главная")
]
courses_button = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*courses_keyboards)

@dp.message_handler(text='Курсы')
async def get_courses(message:types.Message):
    await message.answer("Выберите курсы:", reply_markup=courses_button)

@dp.message_handler(text='Главная')
async def home(message:types.Message):
    await start(message)

@dp.message_handler(text='Backend')
async def backend(message:types.Message):
    await message.answer("""Стань Backend-разработчиком с нуля за 
5 месяцев и получи доступ к стажировке + помощь в трудоустройстве!

Длительность: 5 месяцев""")

@dp.message_handler(text='Frontend')
async def frontend(message:types.Message):
    await message.answer("""Стань Frontend-разработчиком с нуля за 
5 месяцев и получи доступ к стажировке + помощь в трудоустройстве!

Длительность: 5 месяцев""")

@dp.message_handler(text='Android')
async def android(message:types.Message):
    await message.answer("""Стань Android-разработчиком с нуля за 
5 месяцев и получи доступ к стажировке + помощь в трудоустройстве!

Длительность: 5 месяцев""")

@dp.message_handler(text='iOS')
async def ios(message:types.Message):
    await message.answer("""Стань iOS-разработчиком с нуля за 
5 месяцев и получи доступ к стажировке + помощь в трудоустройстве!

Длительность: 5 месяцев""")

@dp.message_handler(text='UX/UI')
async def uxui(message:types.Message):
    await message.answer("""Стань UX/UI-дизайнером с нуля за 
3 месяца и получи доступ к стажировке + помощь в трудоустройстве!

Длительность: 3 месяца""")

executor.start_polling(dp)