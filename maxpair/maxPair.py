from typing import List

def maxpair(Seq: List[int]) -> int:
    # s = [5,4,6,7,9]

    result = 0
    pair_1 = 0
    pair_2 = 0
    for i in range(len(Seq)):
        for j in range(i + 1,len(Seq)):
            prod = Seq[i] * Seq[j]

            if prod > result:
                result = prod
                pair_1 = Seq[i]
                pair_2 = Seq[j]

    return result

if __name__ == '__main__':
    _ = input()
    s = list(map(int,input().split()))
    print(maxpair(s))


