def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def test1():
    return "hello,world-1"

def test2():
    return "hello,world-2"

def test3():
    return "hello,world-3"


a = make_bold(test1)
print(a())
print(make_italic(test2)())
print(make_bold(make_italic(test3))())
