"""Создать обработку и процедуру заполнения её табличной части. 
Количество строк и длина в символах каждой строки должны задаваться на форме."""

#Автоматическое заполнение таблицы рандомными значениями.
#С последующим сохранением в csv формат
import random
import csv

list_name = ["A", "E", "I", "O", "U", "Y", "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z", "1", "2", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
list_name = "".join(list_name).lower()
user_strings = int(input("Please enter the number of lines: "))
user_length = int(input("Please enter the number of characters per line: "))
for i in range(0, user_strings):
    list_name = random.sample(list_name, user_length)
    list_name = "".join(map(str, list_name))
    print(list_name)
    #Сохранение в .csv файл
    file_task1 = open("file_task1.csv", "a")
    file_task1.write(str(list_name) + "\n")
file_task1.close()