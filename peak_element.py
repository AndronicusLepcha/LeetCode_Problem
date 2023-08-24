''' Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6. '''

def find_peak(nums):
    peak=nums[0]
    for x in nums:
        if x>peak:
            peak=x
    return nums.index(peak)
nums=[1,2,1,3,5,6,4]
print(find_peak(nums))

#or
def findPeakElement(nums):
    left=0
    right=len(nums)-1
    if len(nums)==1:
        return 0
    while left<=right:
        mid=(left+right)>>1
        if (mid==0 or nums[mid]>=nums[mid-1] ) and (mid==len(nums)-1 or nums[mid]>=nums[mid+1]) :
            return mid
        elif nums[mid]<=nums[mid+1]:
            left=mid+1
        else:
            right=mid-1
    return -1
nums=[1,2,1,3,5,6,4]
print(findPeakElement(nums))