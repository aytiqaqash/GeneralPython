# Задача 3. Расстояние между двумя точками
# В списке coords лежат 2 кортежа, каждый из которых является координатами точек A и B соответственно.
# Напишите функцию, которая ищет расстояние между этими точками.
# Найти расстояние между двумя точками можно по следующим формулам:
# Рекомендации к выполнению:
# Используйте функцию zip, чтобы итерироваться одновременно по координатам точки A и точки B.
# Квадратный корень числа можно вычислить, возведя его в степень 0.5.


# generally I googled zip function, as I didn't know what is this function.
coords1 = [(1, 10), (1, 11)]
coords2 = [(0, 20), (20, 20)]
coords3 = [(100, 91, 87), (80, 35, 70)]
coords4 = [(0, 100, 20), (0, 0, 80)]

# first I tried to solve as simple as I can.
res = list(zip(coords1[0], coords1[1]))
xa, xb = res[0]
ya, yb = res[1]
part1 = (xb - xa) ** 2
part2 = (yb - ya) ** 2
# print((part1 + part2) ** 0.5)

# then I tried to make it shorter with for
# also checked what if A and B has 3 points in each tuple
result = list(zip(coords3[0], coords3[1]))
r = 0
for a, b in result:
    r = r + (b - a) ** 2


# print(r**0.5)

# then I made it as a function, so you can pass any coords with 2 tuples
def findDistance(coords):
    result = list(zip(coords[0], coords[1]))
    r = 0
    for a, b in result:
        r = r + (b - a) ** 2
    return r ** 0.5


# Here is the results
print(findDistance(coords1))
print(findDistance(coords2))
print(findDistance(coords3))
print(findDistance(coords4))
