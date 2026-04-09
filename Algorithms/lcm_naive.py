

def lcm(a,b):



    for i in  range(max(a, b), a * b + 1):
        if a % i == 0  and b % i == 0:

            return i

if __name__ == '__main__':

    a,b = map(int, input().split())

    print(lcm(a,b))
