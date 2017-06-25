#coding=utf-8
"""
@From book Fluent Python
Cannot run in Python 2.7
"""
class LookinGlass:
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        ## Monkey patch sys.stdout.write, replace it with our own code
        sys.stdout.write = self.reverse_write
        return "JABBERWOCKY"

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please Do not divide by zero')
            return True


def main():
    with LookinGlass() as what:
        print('Alice, Kitty and Snowdrop')
        print(what)

if __name__ == "__main__":
    main()
