from time import ctime, sleep

def time_fun(func):
    def wrapped_func():
        print("%s called at %s"%(func.__name__, ctime()))
        func()
    return wrapped_func

def foo():
    print("I am foo")

foo()
sleep(2)

time_fun(foo)()
