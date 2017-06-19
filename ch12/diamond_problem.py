## Adjust for object
class A(object):
    def ping(self):
        print('A ping: ', self)

class B(A):
    def pong(self):
        print('B pong: ', self)

class C(A):
    def pong(self):
        print('C pong: ', self)

class D(B,C):
    def ping(self):
        super(D,self).ping()
        print('post-ping: ', self)

    def pingpong(self):
        self.ping()
        super(D, self).ping()
        self.pong()
        super(D, self).pong()
        C.pong(self)
def main():
    d = D()
    d.pong()
    C.pong(d)
    d.pingpong()
if __name__ == "__main__":
    ## D.__mro__
    main()
