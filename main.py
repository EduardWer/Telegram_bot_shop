from aiogram import Bot, Dispatcher, executor, types
import logging
import config
import marcups
import db_class
import datetime
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class ButtonState(StatesGroup):
    Cassa_button = State()
    Dolg_my_add = State()
    Dolg_my_delate = State()
    Dolg_add = State()
    Dolg_delate = State()


bot = Bot(config.token)
db = db_class.database()
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)


Admin = True

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    admin = False
    await bot.send_message(message.chat.id,"Добро пожаловать в наш бот!\n"
                                                "Войдите в аккаунт для продолжения действий")
    await bot.send_message(message.chat.id, "Введите данные в виде /login Login:Password")

@dp.message_handler(commands=["login"])
async def Loging(message: types.Message):
    info_adm = db.select_admin()
    message_text = message.text.replace('/login ','')
    info_job = db.select_jobs()
    if message_text in info_adm:
        Admin = True
        await bot.send_message(message.chat.id,"Вы зашли как админ",reply_markup=marcups.Admin_keybord)
    elif message_text in info_job:

        await message.reply('Вы зашли как работник', reply_markup=marcups.keyboard)
    else:
        await bot.send_message(message.chat.id, "Ошиблись паролем!")


@dp.message_handler(commands=['new_admin'])
async def add_new_admin(message: types.Message):
    if Admin == True:
        message_text = message.text.replace('/new_admin ', '')
        db.Add_admin(message_text)
        await bot.send_message(message.chat.id,f"Вы успешно создали админа {message_text} ")
    else:
        await bot.send_message(message.chat.id,"Снанала войдите как Admin")


@dp.message_handler(commands=['new_worker'])
async def add_worker(message: types.Message):
    if Admin == True:
        message_text = message.text.replace('/new_worker ', '')
        db.Add_worker(message_text)
        await bot.send_message(message.chat.id, f"Вы успешно создали работника {message_text} ")
    else:
        await bot.send_message(message.chat.id, "Снанала войдите как Admin")


@dp.callback_query_handler(lambda query: query.data == 'del_dr_dolg')
async def button_pressed_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Введите номер долга')
    await ButtonState.Dolg_delate.set()


@dp.message_handler(Text, state=ButtonState.Dolg_delate)
async def text_handler(message: types.Message, state: FSMContext):
    await state.finish()
    try:
        db.del_dolg(int(message.text))
        await bot.send_message(message.chat.id, f"Вы успешно удалили долг №{message.text}")
    except:
        await bot.send_message(message.chat.id, "Вы ввели не верное значение")


@dp.callback_query_handler(lambda query: query.data == 'create_dr_dolg')
async def button_pressed_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Введите кому и сумму и какую сумму')
    await ButtonState.Dolg_add.set()


@dp.message_handler(Text, state=ButtonState.Dolg_add)
async def text_handler(message: types.Message, state: FSMContext):
    await state.finish()
    db.add_dolg(message.text)
    await bot.send_message(message.chat.id, f"Вы успешно добавили долг")


# ********************************************************************************************
@dp.callback_query_handler(lambda query: query.data == 'del_dolg')
async def button_pressed_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Введите номер долга')
    await ButtonState.Dolg_my_delate.set()


@dp.message_handler(Text, state=ButtonState.Dolg_my_delate)
async def text_handler(message: types.Message, state: FSMContext):
    await state.finish()
    try:
        db.del_my_dolg(int(message.text))
        await bot.send_message(message.chat.id, f"Вы успешно удалили долг №{message.text}")
    except:
        await bot.send_message(message.chat.id, "Вы ввели не верное значение")


# *************************************************************************************************
@dp.callback_query_handler(lambda query: query.data == 'create_dolg')
async def button_pressed_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Введите кто и какую сумму')
    await ButtonState.Dolg_my_add.set()


@dp.message_handler(Text, state=ButtonState.Dolg_my_add)
async def text_handler(message: types.Message, state: FSMContext):
    await state.finish()
    db.add_my_dolg(message.text)
    await bot.send_message(message.chat.id, f"Вы успешно добавили долг")


# **********************************************************************************************

@dp.callback_query_handler(lambda query: query.data == 'button_pressed')
async def button_pressed_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Введите сумму для обновления')
    await ButtonState.Cassa_button.set()


@dp.message_handler(Text, state=ButtonState.Cassa_button)
async def text_handler(message: types.Message, state: FSMContext):
    await state.finish()
    try:
        datatime = datetime.datetime.now()
        now = int (datatime.strftime("%H"))
        db.update_cassa(float(message.text))
        if now < 21 and now > 4:
            with open("Day.txt", "a") as file:
                datatime = datatime.strftime("%d-%m-%Y %H:%M")
                # Записываем данные в файл
                file_old = "\n" + f"Касса: {message.text}  Дата: {datatime} "
                file.write(file_old)
        else:
            with open("Night.txt", "a") as file:
                datatime = datatime.strftime("%d-%m-%Y %H:%M")
                # Записываем данные в файл
                file_old = "\n" + f"Касса: {message.text}  Дата: {datatime} "
                file.write(file_old)
        await message.reply(f'Значение кассы: {message.text} руб')
    except:
        await bot.send_message(message.chat.id,"Введено не верное значение")


#**************************************************************************************


@dp.message_handler()
async def functions_bot(message: types.Message):
    if 'Касса' in message.text:
        cassa = db.select_cassa()
        await bot.send_message(message.chat.id,f"Баланс кассы сейчас: {cassa[0]} руб",reply_markup=marcups.inline_Cassa)
    elif 'Мои долги' in message.text:
        dolg = db.select_my_dolg()
        if dolg == []:
            await bot.send_message(message.chat.id, f"Долгов нет!!")
        else:
            await bot.send_message(message.chat.id, f"Ваши долги:\n {dolg}", reply_markup=marcups.dolg_keybord)
    elif "Дать в долг" in message.text:
        data = db.select__dolg()
        await bot.send_message(message.chat.id, f'Вам должны: \n{data}', reply_markup=marcups.dolg_dryg_keybord)
    elif "Информация" in message.text:
        await bot.send_message(message.chat.id, "Основные команды бота:\n"
                                                "/new_admin Login:password - создаёт нового админа \n"
                                                "/new_worker Login:password - создаёт нового работника \n"
                                                "Все остальные функции работают через кнопки")

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('Button_'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        document = types.InputFile('Day.txt')
        await bot.send_document(chat_id=callback_query.from_user.id, document=document)
        await bot.answer_callback_query(callback_query.id)
    if code == 2:
        document = types.InputFile('Night.txt')
        await bot.send_document(chat_id=callback_query.from_user.id, document=document)
        await bot.answer_callback_query(callback_query.id)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
