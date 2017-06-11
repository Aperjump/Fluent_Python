#coding=utf-8
"""
@From book Fluent Python
"""
from operator import itemgetter
metro_data = [
('A','B','C'),
('D','E','F')
]
for city in sorted(metro_data, key = itemgetter(1)):
    print city
cc_name = itemgetter(1,0)
for city in metro_data:
    print(cc_name(city))
