def median(nums):
    #print(nums)
    if len(nums) % 2 == 0:
        print( ( (nums[len(nums) // 2]) + (nums[ (len(nums)-1) // 2]) )//2 )
    else:
        print(nums[len(nums)//2])

nums_len = int(input())
nums = input()
nums = [int(nums) for nums in nums.split()]
nums.sort()
median(nums[:nums_len//2])
median(nums)
if nums_len%2 == 0:
    median(nums[nums_len//2:])
else:
    median(nums[(nums_len // 2)+1:])