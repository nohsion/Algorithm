n = int(input())
back = list(map(int, input().split()))

tmp = [0] * n
# 내 풀이
# for i, b in enumerate(back):
#   cnt, is_next = 0, b == 0
#   for j in range(n):
#     if is_next and tmp[j] == 0:
#       tmp[j] = i + 1
#       break
#     if tmp[j] == 0:
#       cnt += 1
#     if cnt == b:
#       is_next = True

# for t in tmp:
#   print(t, end=' ')


# 모범 풀이 (good..)
for i in range(n):
  for j in range(n):
    if back[i] == 0 and tmp[j] == 0:
      tmp[j] = i + 1
      break
    if tmp[j] == 0:
      back[i] -= 1
for t in tmp:
  print(t, end=' ')