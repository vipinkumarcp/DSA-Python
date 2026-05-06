

#find the max digit number from 9692341


def  maxdigit(digit: str):

    digits =  list(map(int, digit))

    max_number_list = []

    for i in digits:
        max_val_in_loop = float('-inf')
        if digits[i] >=  max_val_in_loop:
            max_val_in_loop = i

        



            


print(maxdigit("9692341"))