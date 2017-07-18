from time import ctime, sleep

def time_fun(func):
    def wrapped_fun(a, b):
        print("%s called at %s"%(func.__name__, ctime()))
        print(a, b)
        func(a, b)
    return wrapped_fun

def foo(a, b):
    print(a + b)

foo(2,3)
sleep(2)

time_fun(foo)(2, 3)
