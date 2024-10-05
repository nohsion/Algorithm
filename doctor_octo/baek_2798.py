# https://www.acmicpc.net/problem/2798

def get_mx():
    mx = 0
    for i in range(N-2):
        for j in range(i+1, N):
            for k in range(j+1, N):
                sm = lst[i] + lst[j] + lst[k]
                if sm <= M and sm > mx:
                    mx = sm
                    if mx == M:
                        return mx
    return mx

N, M = map(int, input().split())
lst = list(map(int, input().split()))

ans = get_mx()
print(ans)