# [달팽이 배열] 밖으로 -> 안으로 -> 밖으로 -> ... (반복 -> 디버깅해보자)

N = 5
M = (N+1)//2
arr = [[0]*(N+2) for _ in range(N+2)]
dr = [(-1,0), (0,1), (1,0), (0,-1)] # 상 -> 우 -> 하 -> 좌

# 달팽이 초기 변수 세팅
cnt_mx, cnt, flag, val = 1, 0, 0, 1
d = 0 # 위(상)로 이동
ci, cj = M, M
for k in range(1, 100):
    cnt += 1
    arr[ci][cj] = k
    ci, cj = ci+dr[d][0], cj+dr[d][1] # 한 칸 이동
    if (ci,cj) == (1,1):
        cnt_mx, cnt, flag, val = cnt_mx, 1, 1, -1 # 안으로 돌아가는 달팽이
        d = 2 # 초기 방향 아래로
    elif (ci, cj) == (M, M):
        cnt_mx, cnt, flag, val = 1, 0, 0, 1  # 바깥으로 돌아가는 달팽이
        d = 0 # 초기 방향 위로

    if cnt == cnt_mx: # 방향 전환
        cnt = 0 # 카운트 초기화
        d = (d+val)%4
        if flag == 0:
            flag = 1
        else:
            flag = 0
            cnt_mx += val # 2번에 한번꼴로 cnt_mx 증가 1->1->2->2->3->3->..
