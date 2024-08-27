nums = []
if len(nums) > 1:
    nums.insert(0, nums[-1])
    nums.pop()
    print(nums)
elif len(nums) <= 1:
    print(nums)