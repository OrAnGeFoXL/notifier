from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from datetime import datetime, timedelta

#from libs.data import category_sorter, amount_sorter

def repeat_frq_kb():
    builder = ReplyKeyboardBuilder()

    cats =["Час", "День", "Неделя", "Месяц", "Год", "Своё"]
        
    for cat in cats:
        builder.add(KeyboardButton(text=cat))
    builder.adjust(2,2,2,2)
    return builder.as_markup(resize_keyboard=True) 


#Клавиатура с месяцами начиная с текущего
def month_kb():
    """Клавиатура с месяцами начиная с текущего"""
    builder = ReplyKeyboardBuilder()

    now = datetime.now()
    month_names = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август',
                   'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    cur_month = month_names[now.month - 1] 
    cats = month_names[month_names.index(cur_month):] + month_names[:month_names.index(cur_month)]
    cats = ["Текущий месяц"] + cats[1:]
    
    for cat in cats:
        builder.add(KeyboardButton(text=cat))
    builder.adjust(3,3,3,3)
    return builder.as_markup(resize_keyboard=True)



def yes_no_kb():
    """Да/Нет"""
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="Да"))
    builder.add(KeyboardButton(text="Нет"))
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

def amount_adaptive_kb(user_id):
    builder = ReplyKeyboardBuilder()
    cats = amount_sorter(user_id)    
    
    for cat in cats:
        builder.add(KeyboardButton(text=cat))
    builder.adjust(3,3,3,3)
    return builder.as_markup(resize_keyboard=True) 

if __name__ == "__main__":
    
    month_kb()