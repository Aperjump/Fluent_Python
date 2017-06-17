#coding=utf-8
"""
@From book Fluent Python
"""
class Demo:
    @classmethod
    def klassmethod(*args):
        return args
    @staticmethod
    def statmeth(*args):
        return args

def main():
    print Demo.klassmethod()
    print Demo.klassmethod("haha")
    print Demo.statmeth()
    print Demo.statmeth("haha")

if __name__ == "__main__":
    main()

"""
Result
$ python classmethod_staticmethod.py
(<class __main__.Demo at 0x0020FA78>,)
(<class __main__.Demo at 0x0020FA78>, 'haha')
()
('haha',)
"""
