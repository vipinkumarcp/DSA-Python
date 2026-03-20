from typing import List

def maxpair(Seq: List[int]) -> int:
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')

    for i in Seq:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            max2 = i

        if i < min1:
            min2 = min1
            min1 = i

        elif i < min2:
            min2 = i

    return max(max1*max2 ,  min1*min2)

if __name__ == '__main__':
    _ = input()
    s = list(map(int,input().split()))
    print(maxpair(s))


