# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

file_1 = open('my_file.txt', 'w')
users_text = [input('Введите текст: ')]
while users_text:
    file_1.writelines(users_text)
    file_1.writelines('\n')
    users_text = input('Введите текст:')
    if not users_text:
        break
file_1.close()


