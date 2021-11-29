def binary_search(list,target):
    first=0
    last = len(list)-1

    while first <= last :
        midpoint = (first+last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None

def verify(index):
    if index is not None:
        print("Target value found at index:",index)
    else:
        print("Target not found in list")



numbers = [item for item in range(0,11)]

print(numbers)

result = binary_search(numbers,7)

verify(result)