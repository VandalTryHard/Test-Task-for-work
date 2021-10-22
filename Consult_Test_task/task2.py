"""2. Подсвечивать строки в заполненной таблице, содержащие указанную в отдельном поле формы комбинацию символов."""

import csv

start = True
#поиск совпадений по строкам
while start == True:
    list_ = open("file_task1.csv", "r")
    csv_reader = csv.reader(list_) # читает по строкам
    user_symbol = input("Plese enter symbol: ")
    for row in list_: #Проверяет совпадения по строкам
        if user_symbol in str(row):
            print(row)
        elif user_symbol not in str(row):
            print("Not")
    user_cont = input("Do you want to continue your search? (y/n): ")
    if user_cont == "y":
        print("Ok")
    else:
        start = False
start = False
list_.close()
