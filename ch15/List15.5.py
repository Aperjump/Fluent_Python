import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield "JABBsfdsf"
    sys.stdout.write = original_write

def main():
    with looking_glass() as what:
        print('Alice, Kitty and Snowdrop')
        print(what)

if __name__ == "__main__":
    main()