# 1~9까지의 자연수 7*7 격자판에서, 5자리 회문이 몇 개있는지 출력하세요
a = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for i in range(7):
    for j in range(3):
        row_tmp = ''
        col_tmp = ''
        for k in range(j, j+5):
            row_tmp += str(a[i][k])
            col_tmp += str(a[k][i])
        if row_tmp[::] == row_tmp[::-1]:
            cnt += 1
        if col_tmp[::] == col_tmp[::-1]:
            cnt += 1
print(cnt)
