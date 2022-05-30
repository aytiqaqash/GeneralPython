# Задача 2. Дежурство
#
# Дан словарь schedule, в котором хранится информация о дежурствах.
# Ключом является id сотрудника, значением — список из дней, в которые данный сотрудник может выйти на дежурство.
# Обозначения имён всех дней лежат в списке unique_days.
#
# Найдите:
#
# Дни, когда никто не может дежурить (используйте множества для решения этого пункта).
# Для каждого дня недели найдите количество сотрудников, которые могут выйти на дежурство в соответствующий день.
# Используйте функции и декомпозицию.

schedule = {
    '1001': ['пн', 'вс'],
    '1231': ['пн', 'вт'],
    '1232': ['ср', 'чт', 'пт'],
    '1280': ['ср', 'пт', 'вс'],
    '1282': ['чт'],
    '1290': ['пт', 'вс'],
    '1303': ['вт', 'вс'],
}

unique_days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
# option 1 for task1
variant1 = set([])
for days in schedule.values():
    for day in days:
        variant1.add(day)
print(set(unique_days) - variant1)

# option 2 for task1
variant2 = set(unique_days)
for days in schedule.values():
    for day in days:
        variant2.discard(day)
print(variant2)

# task 2
count_emps = {'пн':0, 'вт':0, 'ср':0, 'чт':0, 'пт':0, 'сб':0, 'вс':0}
for d in unique_days:
    for days in schedule.values():
        if d in days:
            count_emps[d]+=1
print(count_emps)