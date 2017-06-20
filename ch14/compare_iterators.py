s = 'ABC'
for char in s:
    print(char)

it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break
        
