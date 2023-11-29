n = int(input())
nums = list(map(int, input().split()))
m = int(input())

for i in range(m):
    nums.sort()
    nums[0] += 1
    nums[-1] -= 1
nums.sort()
print(nums[-1] - nums[0])
