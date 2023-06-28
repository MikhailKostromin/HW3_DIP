# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# Верните все возможные варианты комплектации рюкзака.

from collections import namedtuple
from itertools import *

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]
n = 2500
# n = int(input())
max_sum = 0
for h in range(1, 11):
    a = combinations(items, h)
    for combo in a:
        weight = sum([x.mass for x in combo])
        if weight <= n:
            summa = sum([x.price for x in combo])
            if summa > max_sum:
                max_sum = summa
                arg_max = combo

for i in sorted(arg_max):
    print(i.name)

