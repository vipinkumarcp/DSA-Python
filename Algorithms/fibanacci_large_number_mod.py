def pissaio_period(m):

    a,b = 0,1



    for i in range(m*m):

        a,b = b, (a+b)%m

        if a == 0 and b == 1:
            return i + 1

def fib(n,m):

    period = pissaio_period(m)

    n = n % period

    a,b = 0,1

    for i in range(n):

        a , b  = b, (a+b) % m 

    return a


if __name__ == '__main__':

    print(fib(10,2))



