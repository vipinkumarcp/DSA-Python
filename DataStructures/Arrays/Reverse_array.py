

def reverse(arr):

    start_index  = 0
    end_index = len(arr)-1

    while end_index > start_index:

        arr[start_index],arr[end_index] = arr[end_index],arr[start_index]

        start_index += 1
        end_index -=1


    return arr


print(reverse([1,2,3,4,6,7]))