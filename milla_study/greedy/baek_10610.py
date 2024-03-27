# https://www.acmicpc.net/problem/10610
import sys

n = list(map(int, input()))
if 0 not in n or sum(n) % 3 != 0:
    print(-1)
    sys.exit()
print(''.join(map(str, sorted(n, reverse=True))))
