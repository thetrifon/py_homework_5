'''4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.'''

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
translate = []
with open('task_4.txt', 'r') as translate_items:
    for i in translate_items:
        i = i.split(' ', 1)
        translate.append(rus[i[0]] + '  ' + i[1])
    print(translate)

    with open('task_4_rus.txt', 'w') as translated:
        translated.writelines(translate)
#20.07.2021: тире переносится как вЂ”