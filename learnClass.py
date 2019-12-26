# function definition
def foo():
    print("hello world")
    b = 2
    return b

# class definition
class fooClass:
    aa = 0
    def __init__(self):
        self.aa = 5
        a = 55
    
    def foo(self):
        print("hello world 2")



################
# Usage:
y = foo()


x = fooClass()
x.foo()