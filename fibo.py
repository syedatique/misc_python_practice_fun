# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    if n!= 1:
        a, b = 0, 1
        while b < n:
            print b
            a, b = b, a+b
    else:
        print n

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

# f = fib2(12)
# print 'f'