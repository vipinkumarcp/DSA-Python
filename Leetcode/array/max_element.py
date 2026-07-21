def largest(nums):

    largest = nums[0]

    for ch in nums:

        if ch > largest:

            largest = ch

    return largest


print(largest([1,45,56,32]))

