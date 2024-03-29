'''Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.


Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
 '''


def triple(nums):
    first=second=float('inf')
    for n in nums:
        if n<=first:
            first=n
        elif n<=second:
            second=n
        else:
            return True
    return False

nums=[5,4,3,2,1]
print(triple(nums))