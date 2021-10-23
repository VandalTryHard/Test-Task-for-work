"""Создать обработку и процедуру заполнения её табличной части. 
Количество строк и длина в символах каждой строки должны задаваться на форме."""

#Автоматическое заполнение таблицы рандомными значениями. С последующим сохранением в csv формат
import random
import csv
#lines = 0 #Точка отсчета нумарции строк
list_name = ["A", "E", "I", "O", "U", "Y", "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z", "1", "2", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
list_name = "".join(list_name).lower() # приводит к нижнему регистру
user_strings = int(input("Please enter the number of lines: "))
user_length = int(input("Please enter the number of characters per line: "))
for i in range(0, user_strings):
    list_name = random.sample(list_name, user_length)
    list_name = "".join(map(str, list_name)) # убирает всё лишнее
    print(list_name)
    #Сохранение в .csv файл
    file_task1 = open("file_task1.csv", "a")
    #lines +=1 # Для введения нумерации строк, раскоментить при необходимости генерации рандомного списка с нумерацией строк
    file_task1.write(str(list_name) + "\n") #str(lines) + "_" +  -добавить для нумарации строк
file_task1.close()