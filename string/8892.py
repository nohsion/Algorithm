def isPalin(s):
  if s == s[::-1]:
    return True

t = int(input())
answer = [0 for _ in range(t)]

for i in range(t):
  n = int(input())
  datas = []
  for _ in range(n):
    datas.append(input())
  for j in range(n):
    for k in range(j+1, n):
      tmp1 = datas[j] + datas[k]
      tmp2 = datas[k] + datas[j]
      if isPalin(tmp1):
        answer[i] = tmp1
        break
      if isPalin(tmp2):
        answer[i] = tmp2
        break

for a in answer:
  print(a)


