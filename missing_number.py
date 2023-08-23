#fiind the missing number in an array
#input=[1,2,3,4,6]
#output=6
def missing(nums):
    mini=min(nums)
    maxi=max(nums)
    for x in range(mini,maxi):
        if x not in nums:
            print(x)

nums=[1,2,3,4,7]
missing(nums)