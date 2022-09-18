import pandas as pd
import numpy as np
import ipywidgets as wid
import numbers as num
from random import randint

# Задание 1.
# Виджеты
out = wid.Output()
out2 = wid.Output()
out3 = wid.Output()
label = wid.HTML(value = f"<b><font color='black'><font size=3>{'Введите параметры расчета'}</b>")
bound_a = wid.Text(description='Длина стороны A, ед.',style={'description_width': '150px'},layout=wid.Layout(width='458px'))
bound_b = wid.Text(description='Длина стороны B, ед.',style={'description_width': '150px'},layout=wid.Layout(width='458px'))
bound_c = wid.Text(description='Длина стороны C, ед.',style={'description_width': '150px'},layout=wid.Layout(width='458px'))
area_but = wid.Button(description='Рассчитать площадь', layout=wid.Layout(width='150px'))
vol_but = wid.Button(description='Рассчитать объем', layout=wid.Layout(width='150px'))
clean_but = wid.Button(description='Очистить', layout=wid.Layout(width='150px'))

# Расположение в ноутбуке
params = wid.VBox([label, bound_a, bound_b, bound_c, wid.HBox([area_but, vol_but, clean_but]), out, out2])

class cuboid:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def vol(self):
        '''Функция расчета объема прямоугольного параллелепипеда'''
        return self.a * self.b * self.c
    def area_surf(self):
        '''Функция расчета площади поверхности прямоугольного параллелепипеда'''
        return 2 * (self.a * self.b + self.b * self.c + self.a * self.c)

# Функции вывода виджетов на экран и считывания заполненных значений
def input_parameters():
    display(params)

def wid_area(b):
    with out:
        out.clear_output()
        try:
            a = int(bound_a.value)
            b = int(bound_b.value)
            c = int(bound_c.value)
            ex = cuboid(a, b, c).area_surf()
            if isinstance(ex, num.Number) == True:
                display(wid.HTML(value = f"<b><font size=2> Площадь параллелепипеда равна {ex}</b>"))
        except ValueError:
            display(wid.HTML(value = "<b><font size=2> Параметры введены некорректно. Попробуйте снова.</b>"))
    
def wid_volume(b):
    with out2:
        out2.clear_output()
        try:
            a = int(bound_a.value)
            b = int(bound_b.value)
            c = int(bound_c.value)
            ex = cuboid(a, b, c).vol()
            if isinstance(ex, num.Number) == True:
                display(wid.HTML(value = f"<b><font size=2> Объем параллелепипеда равен {ex}</b>"))
        except ValueError:
            display(wid.HTML(value = "<b><font size=2> Параметры введены некорректно. Попробуйте снова.</b>"))

def wid_cleaning(b):
    with out3:
        out.clear_output()
        out2.clear_output()
        bound_a.value = ''
        bound_b.value = ''
        bound_c.value = ''

# Кнопки
clean_but.on_click(wid_cleaning)
vol_but.on_click(wid_volume)
area_but.on_click(wid_area)


# Задание 3.
out_weeks = wid.Output()
out_weeks2 = wid.Output()
weeks_count = wid.Text(description='Введите количество прошедших дней',style={'description_width': '300px'},layout=wid.Layout(width='450px'))
weeks_but = wid.Button(description='Рассчитать количество целых прошедших недель', layout=wid.Layout(width='340px'))
clean_weeks_but = wid.Button(description='Очистить', layout=wid.Layout(width='107px'))
weeks_params = wid.VBox([weeks_count, wid.HBox([weeks_but, clean_weeks_but]), out_weeks])


def week(days):
    return int(days/7)

def weeks_input_parameters():
    display(weeks_params)

def wid_weeks(b):
    with out_weeks:
        out_weeks.clear_output()
        try:
            days = int(weeks_count.value)
            weeks_cnt = week(days)
            if isinstance(weeks_cnt, num.Number) == True:
                display(wid.HTML(value = f"<b><font size=2> Количество прошедших недель: {weeks_cnt}</b>"))
        except ValueError:
            display(wid.HTML(value = "<b><font size=2> Параметры введены некорректно. Попробуйте снова.</b>"))         

def wid_cleaning_weeks(b):
    with out_weeks2:
        out_weeks.clear_output()
        weeks_count.value = ''

#Кнопки
weeks_but.on_click(wid_weeks)
clean_weeks_but.on_click(wid_cleaning_weeks)


# Задание 7.

#Виджеты
out_num = wid.Output()
out_num2 = wid.Output()
out_num3 = wid.Output()
file_name = wid.Text(description='Введите имя файла (без формата)',style={'description_width': '300px'},layout=wid.Layout(width='700px'))
n_digit = wid.Text(description='Сгенерировать N-значное число (введите N)',style={'description_width': '300px'},layout=wid.Layout(width='500px'))
top_count = wid.Text(description='Вывести TOP-N встречающихся цифр (введите N)',style={'description_width': '300px'},layout=wid.Layout(width='500px'))
num_but = wid.Button(description='Сгенерировать число', layout=wid.Layout(width='196px'))
top_but = wid.Button(description='Вывести TOP', layout=wid.Layout(width='196px'))
clean_num_but = wid.Button(description='Очистить выходные данные', layout=wid.Layout(width='700px'))

num_params = wid.VBox([file_name, wid.HBox([n_digit, num_but]), wid.HBox([top_count, top_but]), clean_num_but, out_num, out_num2])

def num_input_parameters():
    display(num_params)

# Генерируем число
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

# Кладем его в файл
def wid_to_txt(b):
    n_dig = int(n_digit.value)
    file_name_val = str(file_name.value) + '.txt'
    with out_num:
        out_num.clear_output()
        out_num2.clear_output()
        over_digit_num = random_with_N_digits(n_dig)
        lines = [str(over_digit_num)]
        with open(file_name_val, 'w') as f:
            f.write('\n'.join(lines))
        if over_digit_num % 2 == 0:
            display(wid.HTML(value = f"<b><font size=2> Число сгенерировано, является четным и размещено в файле: {file_name_val}</b>"))
        else:
            display(wid.HTML(value = f"<b><font size=2> Число сгенерировано, является нечетным и размещено в файле: {file_name_val}</b>"))
        #print('Число сгенерировано и размещено в файле') # попросить ввести имя файла

# Задание 8.
names_map = {'numbers': 'Цифра', 'counts': 'Сколько раз она встречалась'}

def wid_read_file(b):
    top = int(top_count.value)
    with out_num2:
        out_num2.clear_output()
        with open('readme.txt') as f:
            lines = f.readlines()
        num = lines[0]
        temp_dict = {'1':[], '2':[], '3':[], '4':[], '5':[], '6':[], '7':[], '8':[], '9':[], '0':[]}
        for i in num:
            temp_dict[i].append(i)
        max_cnt = []
        for key, value in temp_dict.items():
            cnt = len(temp_dict[key])
            max_cnt.append([key, cnt])
        df = pd.DataFrame(max_cnt, columns=['numbers', 'counts'])
        df_top = df.sort_values('counts', ascending=False).head(top).reset_index(drop=True)
        df_top = df_top.rename(columns=names_map)
        display(df_top)

def wid_cleaning_num(b):
    with out_num3:
        out_num.clear_output()
        out_num2.clear_output()
        file_name.value = ''
        n_digit.value = ''
        top_count.value = ''
        

#Кнопки
num_but.on_click(wid_to_txt)
top_but.on_click(wid_read_file)
clean_num_but.on_click(wid_cleaning_num)