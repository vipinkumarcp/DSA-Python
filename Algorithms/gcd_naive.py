

def findgcd(a: int , b: int):
    best_number = 0
    for i in range(1,a+b):

        if a % i == 0 and b % i == 0:
            best_number = i
    return best_number
    




if __name__ == "__main__":

    print(findgcd(20,10))