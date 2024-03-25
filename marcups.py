from aiogram.types import  ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardMarkup ,InlineKeyboardButton

info = KeyboardButton("Информация")
Cassa = KeyboardButton("Касса")
Dolg = KeyboardButton("Дать в долг")
My_dolg = KeyboardButton("Мои долги")
Admin_keybord = ReplyKeyboardMarkup(resize_keyboard=True).add(Cassa, Dolg, My_dolg, info)
#*****************************************************************************************



inlain_buttom_cassa = InlineKeyboardButton("История кассы",callback_data='Button_1')
inlain_buttom_cassa_noch = InlineKeyboardButton("Ночная касса",callback_data="Button_2")
inline_Cassa = InlineKeyboardMarkup().add(inlain_buttom_cassa,inlain_buttom_cassa_noch)
#*******************************************************************************************************

Update_cassa = InlineKeyboardButton('Обновить кассу',callback_data="button_press")
Update_markup = InlineKeyboardMarkup().add(Update_cassa)

# ********************************************************************************************

button = InlineKeyboardButton('Обновить кассу', callback_data='button_pressed')
keyboard = InlineKeyboardMarkup().add(button)

dolg_delate = InlineKeyboardButton("Удалить долг", callback_data="del_dolg")
create_dolg = InlineKeyboardButton("Добавить долг", callback_data="create_dolg")
dolg_keybord = InlineKeyboardMarkup().add(dolg_delate, create_dolg)
# ***********************************************************************************************

dolg_drug_delate = InlineKeyboardButton("Удалить долг", callback_data="del_dr_dolg")
create_drug_dolg = InlineKeyboardButton("Добавить долг", callback_data="create_dr_dolg")
dolg_dryg_keybord = InlineKeyboardMarkup().add(dolg_drug_delate, create_drug_dolg)
