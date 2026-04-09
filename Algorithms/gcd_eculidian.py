

def findgcd(a: int , b: int):
    while b != 0:
           a,b = b, a % b
    return a
       



    


if __name__ == "__main__":

    a,b = map(int, input().split())

 

    print(findgcd(a,b))