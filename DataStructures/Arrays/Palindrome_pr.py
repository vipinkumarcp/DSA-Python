

def palindrom(p: str) -> bool:

    start_index = 0
    end_index = len(p)-1


    while end_index>start_index:

        if p[start_index] != p[end_index]:
            return False
        start_index += 1
        end_index -=1
    return True



print(palindrom("cac"))


