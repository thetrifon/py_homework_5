#Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

file_counter = open('my_file_2.txt', 'r')
lines = file_counter.readlines()
print(f'Количество строк в файле:  {len(lines)}')
for i in range(len(lines)):
    print(f'Количество символов {i+1}-й строки {len(lines[i])}')
words = file_counter.split('')
file_counter.close()



'''На момент 20.07.2021 не решил вопрос с полсчетом слов'''