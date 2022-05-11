# todo: Изучаем пакет pandas
#
# После установки библиотеки pandas выполните следующие действия:
#
# Изучите справку по модулю (для чего нужен модуль , какие возможности предоставляет)
# Найдите расположение директории модуля pandas и изучите его содержимое
# Получите список доступных атрибутов модуля pandas
# Импортируйте модуль pandas в исполняемый скрипт
# С помощью модуля pandas ознакомьтесь со структурой  DataFrame, фильтрации данных,
# загрузки данных из формата сsv (рассмотрите примеры статьи)
# Установите библиотеку matplotlib, создайте график на своем наборе данных.

# Опорная статья:  https://egorovegor.ru/pandas-obrabotka-i-analiz-dannyh-v-python/


import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime
from dateutil.parser import parse

df_FoodPrice = pd.read_csv("food_price_index_march_2022.csv") # выгрузка данных из файла .csv
df_FoodPrice['Period'] = df_FoodPrice['Period'].astype(object) # изменение типа столбца,
# чтобы с ним было далее можно работать как со str
df_FoodPrice = df_FoodPrice.drop(["STATUS", "Subject", "UNITS", "Series_reference", "Group"], axis="columns")
# удаление одинаковых столбцов
df_FoodPrice = df_FoodPrice.rename(columns={'Series_title_1': 'Product_type'}) # переименование столбца
# с названием продукта

# создание нового датафрейма, ориентированного на данные по яблокам и с новой нумерацией индексов
df_FoodPrice_Product = df_FoodPrice[df_FoodPrice["Product_type"].str.contains("Apples")].reset_index(drop=True)

df_FoodPrice_Product['Year'] = df_FoodPrice_Product['Period'].astype(str).str.slice(0,4) # добавление
# столбца с годом
df_FoodPrice_Product['Month'] = df_FoodPrice_Product['Period'].astype(str).str.slice(5,7) # добавление
# столбца с месяцем
df_FoodPrice_Product.loc[df_FoodPrice_Product["Month"] == "1", "Month"] = "10" # решение проблемы
# с содержимым столбца "Месяц" в связи с тем, что изначально столбец "Период" # был распарсен как float,
# и при переводе его в тип str # (то есть object) ноль после единицы в варианте октября ("10") пропадал
df_FoodPrice_Product['Date'] = df_FoodPrice_Product['Month'] + "/" + df_FoodPrice_Product['Year']# добавление
# столбца "Дата"

# фильтрация датафрейма, ориентированного на яблочные данные за 2006 год и с новой нумерацией индексов
df_FoodPrice_Product = df_FoodPrice_Product[df_FoodPrice_Product["Year"].str.contains("2006")].reset_index(drop=True)

df_FoodPrice_Product = df_FoodPrice_Product.drop(["Period", "Month"], axis="columns")
# удаление столбцов (спасибо, парни, вы нам больше не понадобитесь)

print(df_FoodPrice_Product)
print("--------------------")
print(df_FoodPrice_Product.dtypes)


# Подготовка данных для графика
x  = df_FoodPrice_Product['Date'].values.tolist()
y = df_FoodPrice_Product['Data_value'].values.tolist()

# вывод графика
plt.title(df_FoodPrice_Product.loc[1]['Product_type'] + " , " + df_FoodPrice_Product.loc[1]['Year']) # заголовок
plt.xlabel('date') # ось абсцисс
plt.ylabel("price, in dollars") # ось ординат
plt.grid()      # включение отображение сетки
plt.plot(x, y)  # построение графика
plt.show()
