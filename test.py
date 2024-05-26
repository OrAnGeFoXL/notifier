from datetime import datetime, timedelta

def month_kb():
    """Клавиатура с месяцами начиная с текущего"""

    now = datetime.now()
    month_names = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август',
                   'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    cur_month = month_names[now.month - 1] 
    cats = month_names[month_names.index(cur_month):] + month_names[:month_names.index(cur_month)]
    cats = ["Текущий месяц"] + cats[1:]



    


month_kb()