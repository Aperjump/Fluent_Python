
def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received: ', x)

def main():
    my_coro = simple_coroutine()
    my_coro
    next(my_coro)
    my_coro.send(42)

if __name__ == "__main__":
    main()
    
"""
%run Example16.1.py
-> coroutine started
-> coroutine received:  42
Traceback (most recent call last):
"""
