### first

x = [i*2 for i in range(50)]

g = (i*2 for i in range(50))   #generator

for i in g:
    print(i)
    
### second

def fib(times):
    n = 0
    a, b = 0, 1
    while n < times:
        print(b)
        a, b = b, a+b
        n += 1
    return 'Done'

print(fib(10))


### third, generator

def lib(times):
    n = 0
    a, b = 0, 1
    while n < times:
        yield b
        a, b = b, a+b
        n += 1

print(lib(10))

for i in lib(10):
    print(i)
