#coding=utf-8
"""
@From book Fluent Python
"""
def make_averager(func):
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    return averager

@make_averager
def avg(value):
    pass

def main():
    print avg(10.1)
    print avg(11)
    print avg(15)
    print avg.__code__.co_freevars
    print avg.__closure__[0].cell_contents
if __name__=='__main__':
    from inspect import *
    main()

"""
## Results
10.1
10.55
12.0333333333
('series',)
[10.1, 11, 15]
""
