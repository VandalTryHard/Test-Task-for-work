"""3. Создать процедуру обратного отражения порядка строк (сортировки по номеру строки в обратном порядке.
Например номер строки был 
1   ae1234
2   bc5678
стал
10000 ae1234
9999   bc5678"""

import csv

with open('file_task3.csv', 'r') as textfile:
    for row in reversed(list(csv.reader(textfile))): #reversed возвращает в обратной последовательности весь документ
        print (', '.join(row))