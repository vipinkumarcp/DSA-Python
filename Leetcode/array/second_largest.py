

def second_largest(nums):
    
    largest = second = float("-inf")


    for num in nums:

        if num > largest:
            second = largest
            largest = num

        elif largest>nums>second:
            second = num

    return second

print(second_largest([1,2,3,4,70]))
 