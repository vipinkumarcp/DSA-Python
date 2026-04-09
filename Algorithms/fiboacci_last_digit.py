

def fib(n,k=1):

    if n <=1:
        return n

    if k == 1:
        period = 60
    else :
        period = 15 * (10 ** (k-1))

    n = n % period

    mod = 10 ** k


    a,b = 0,1

    for _ in range(n):

        a,b = b , (a+b) % mod

    return a     




if __name__ == "__main__":

    n = int(input())

    print(fib(n))