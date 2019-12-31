def median(nums):
    #print(nums)
    if len(nums) % 2 == 0:
        return  ( ( (nums[len(nums) // 2]) + (nums[ (len(nums)-1) // 2]) )/2 )
    else:
        return (nums[len(nums)//2])

nums_len = int(input())
nums_ary = [int(s) for s in input().split()]
freq_ary = [int(s) for s in input().split()]
real_ary = []
for x in range(nums_len):
    for z in range(freq_ary[x]):
        real_ary.append(nums_ary[x])

real_ary.sort()
nums_len = len(real_ary)

q1 = median(real_ary[:nums_len//2])
if nums_len%2 == 0:
    q3 = median(real_ary[nums_len//2:])
else:
    q3 = median(real_ary[(nums_len // 2)+1:])

print(float(q3 - q1))