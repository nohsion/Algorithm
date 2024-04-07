from collections import deque

n, m = map(int, input().split())
patients = list(map(int, input().split()))

a = deque([(x, i) for i, x in enumerate(patients)])
cnt = 0
while True:
  curr = a[0][0]
  largest = max([x[0] for x in a])
  if largest > curr:
    a.append(a.popleft())
  else:
    x = a.popleft()
    cnt += 1
    if x[1] == m:
      break
print(cnt)
  