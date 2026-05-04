


def reverse_int( n:int) -> int:

    reverse_num = 0

    while n > 0:

        reminder = n % 10
        n = n //10

        reverse_num = reverse_num * 10 + reminder

    return reverse_num
    

print(reverse_int(345))
        
