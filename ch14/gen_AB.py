def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')

res = (x * 3 for x in gen_AB())
for i in res:
    print('-->', i)

"""
$ python gen_AB.py
start
('-->', 'AAA')
continue
('-->', 'BBB')
end.
"""
