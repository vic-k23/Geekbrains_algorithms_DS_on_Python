# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

Company = namedtuple('Company', 'name, q1, q2, q3, q4')
companies = []

with (open('companies.csv', 'r', encoding='UTF-8')) as f:
    for company in f:
        companies.append(Company._make(company[:-1].split(sep=',')))

summ = 0
for comp in companies:
    summ += float(comp.q1) + float(comp.q2) + float(comp.q3) + float(comp.q4)

average = summ / len(companies)
print(f"The annual profit of all companies together is {average:.2f}")

below_average = []
above_average = []
equal_average = []
for c in companies:
    s = float(c.q1) + float(c.q2) + float(c.q3) + float(c.q4)
    if s < average:
        below_average.append(c.name)
    elif s > average:
        above_average.append(c.name)
    else:
        equal_average.append(c.name)

print(f"Companies have annual profit below average annual profit: {below_average}")
print(f"Companies have annual profit above average annual profit: {above_average}")
print(f"Companies have annual profit equal to average annual profit: {equal_average}")
