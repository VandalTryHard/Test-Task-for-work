"""5. Создать процедуру поиска дублей по заполненным значениям, с перечислением номеров строк попарно.
При этом номера строк не должны повторяться, например
1023 и 6740
6740 и 1023.
Сообщать пользователю время старта и окончания обработки поиска дублей, а также затраченное время в секундах.
"""

import csv
import time

start = True
while start == True:
    list_ = open("file_task3.csv", "r")
    csv_reader = csv.reader(list_) # читает по строкам
    user_symbol = input("Plese enter symbol: ")
    list_of_strings = []

    for row in list_: #Проверяет совпадения по строкам
        start_time = time.time() # старт секундомера
        if user_symbol in str(row):
            print(row)
            list_of_strings.append(row)
        elif user_symbol not in str(row):
            print("Not")
        print("--- %s seconds ---" % (time.time() - start_time)) # вывод затраченого времени на поиск одного значения

    user_cont = input("Do you want to continue your search? (y/n): ")
    if user_cont == "y":
        print("Ok")
    else:
        start = False

start = False
print(list_of_strings) # выводит дубли по заполненным значениям, с перечислением номеров строк
list_.close()