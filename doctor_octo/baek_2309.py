# https://www.acmicpc.net/problem/2309

def dfs(n, sm, lt):
    global ans
    if n == N:
        if len(lt) == 7 and sm == 100:
            ans = lt
        return
    dfs(n+1, sm+lst[n], lt+[lst[n]]) # 선택 O
    dfs(n+1, sm, lt)                 # 선택 X


N = 9
lst = [int(input()) for _ in range(N)]

ans = [] # 선택된 난쟁이 키 리스트
dfs(0, 0, [])
for x in sorted(ans):
    print(x)