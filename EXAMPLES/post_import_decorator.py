from functools import cache
from random import randint
from geometry import circle_area

circle_area = cache(circle_area)
for _ in range(10000):
    result = circle_area(randint(1, 20))

print(circle_area.cache_info())

