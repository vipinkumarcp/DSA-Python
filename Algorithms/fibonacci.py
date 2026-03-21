
def fibrecursion(n):

    if n <= 1:
        return n
    else:
        return fibrecursion(n-1) + fibrecursion(n-2)
    



print(fibrecursion(5))