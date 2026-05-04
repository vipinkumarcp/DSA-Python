
from typing import List


def revArr( arr: List[int]) -> List[int]:

    start_index = 0
    end_index = len(arr)-1

    while end_index>start_index:
        arr[start_index],arr[end_index] = arr[end_index],arr[start_index]

        start_index += 1
        end_index -= 1


    return arr


print(revArr( [1,"d",3,4,5,6]))


