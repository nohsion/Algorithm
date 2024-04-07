from collections import deque

n = int(input())
nums = list(map(int, input().split()))

# 내 풀이
# nums = deque(nums)
# last = 0
# res = []
# while nums:
#   if len(nums) == 1 and nums[0] > last:
#     res.append('L')
#     break
#   l, r = nums[0], nums[-1]
#   if l > last and r > last:
#     if l > r:
#       res.append('R')
#       last = nums.pop()
#     else:
#       res.append('L')
#       last = nums.popleft()
#   elif l > last:
#     res.append('L')
#     last = nums.popleft()
#   elif r > last:
#     res.append('R')
#     last = nums.pop()
#   else:
#     break
# print(len(res))
# print("".join(res))


# 모범 답안
p1, p2 = 0, n-1
last = 0
res = ""
while p1 <= p2:
  tmp: list[tuple] = []
  if nums[p1] > last:
    tmp.append((nums[p1], 'L'))
  if nums[p2] > last:
    tmp.append((nums[p2], 'R'))
  if len(tmp) == 0:
    break
  tmp.sort()
  a: tuple = tmp[0]
  res = res + a[1]
  last = a[0]
  if a[1] == 'L':
    p1 += 1
  else:
    p2 -= 1
print(len(res))
print(res)