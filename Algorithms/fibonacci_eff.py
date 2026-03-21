
def fibrecursion(n):

    arr =[0,1]
    for i in range(2, n+1):
       arr.append(arr[i-1] +arr[i-2] )

    return arr[n]


def fibrecursion_opt(n):

    a,b = 0,1

    for _ in range(n):
        a,b = b,a+b

    return a

print(fibrecursion_opt(4))