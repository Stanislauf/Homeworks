import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = ""

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()



# Обычная клавиатура
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
button_buy = KeyboardButton('Купить')
keyboard.add(button_calculate, button_info, button_buy)

# Inline клавиатура
inline_keyboard = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_keyboard.add(button_calories, button_formulas)

# Inline клавиатура для продуктов
inline_product_keyboard = InlineKeyboardMarkup()
product_buttons = [
    InlineKeyboardButton(text='Product1', callback_data='product_buying1'),
    InlineKeyboardButton(text='Product2', callback_data='product_buying2'),
    InlineKeyboardButton(text='Product3', callback_data='product_buying3'),
    InlineKeyboardButton(text='Product4', callback_data='product_buying4')
]
inline_product_keyboard.add(*product_buttons)


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью. Выберите действие:', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=inline_keyboard)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer(
        'Формула Миффлина-Сан Жеора:\n\n\nЖенщины:\nBMR = 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) - 161\n\n\nМужчины:\nBMR = 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) + 5')
    await call.answer()


@dp.callback_query_handler(lambda call: call.data.startswith('product_buying'))
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler(lambda message: message.text == 'Купить')
async def get_buying_list(message: types.Message):
    product_info = [
        ("Product 1", "Описание 1", 100, "1.jpeg"),
        ("Product 2", "Описание 2", 200, "2.jpeg"),
        ("Product 3", "Описание 3", 300, "3.jpeg"),
        ("Product 4", "Описание 4", 400, "4.jpeg")
    ]

    # Отправляем информацию о каждом продукте и изображение
    for name, description, price, image_path in product_info:
        await message.answer(f'Название: {name} | Описание: {description} | Цена: {price}')

        # Используем with open для открытия локального изображения
        with open(image_path, 'rb') as photo:
            await message.answer_photo(photo=photo)

    await message.answer("Выберите продукт для покупки:", reply_markup=inline_product_keyboard)

@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, "Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)  # Сохраняем возраст
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)  # Сохраняем рост
    await message.answer("Введите свой вес:")
    await UserState.weight.set()  # Устанавливаем состояние для ожидания веса


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)  # Сохраняем вес
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f"Ваша норма калорий: {calories:.2f} ккал.")
    await state.finish()


@dp.message_handler(lambda message: message.text == 'Информация')
async def info_message(message: types.Message):
    await message.answer(
        'Я могу помочь вам рассчитать вашу норму калорий на основе ваших параметров. Нажмите "Рассчитать", чтобы начать.')


@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer('Пожалуйста, нажмите команду /start что бы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)