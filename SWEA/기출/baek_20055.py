N, K = map(int, input().split())
lst = list(map(int, input().split()))
v = [0]*(N)

ans = 1
cnt = 0
while True:
    # [1] 벨트 회전
    lst.insert(0, lst.pop())
    v.insert(0, v.pop())
    v[N-1] = 0  # 로봇이 내리는 위치라면 즉시 내린다.

    # [2] 로봇 이동 (가장 뒤부터)
    for i in range(N-2, -1, -1):
        if v[i] == 1 and v[i+1] == 0 and lst[i+1] >= 1: # 로봇이 있고, 다음칸에 로봇이 없으며 내구도 1이상이면 이동시킴
            v[i], v[i+1] = 0, 1
            lst[i+1] -= 1
            if lst[i+1] == 0:
                cnt += 1  # 내구도가 감소해서 0이되면 cnt 1 증가
            v[N-1] = 0  # 로봇이 내리는 위치라면 즉시 내린다.

    # [3] 로봇 올리기
    if lst[0] > 0:
        v[0] = 1
        lst[0] -= 1
        if lst[0] == 0:
            cnt += 1  # 내구도가 감소해서 0이되면 cnt 1 증가

    # [4] 내구도 체크
    # if lst.count(0) >= K: # lst.count(0)하면 느리다. 매번 리스트 O(N) 순회하기 때문
    #     break
    if cnt >= K:
        break

    ans += 1

print(ans)