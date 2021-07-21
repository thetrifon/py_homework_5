#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.



with open('team_salary.txt', 'r') as salary_calc: # работает только с английскими символами
            salary_mean = []
            salary_low = []
            list = salary_calc.read().split('\n')
            for i in list:
                i = i.split()
                if int(i[1]) < 20000:
                    salary_low.append(i[0])
                salary_mean.append(i[1])
print(f'Оклад меньше 20.000 {salary_low}, средний оклад {sum(map(int, salary_mean)) / len(salary_mean)}')