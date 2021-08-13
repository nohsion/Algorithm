# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하시오.

n = int(input())

count = 0
# 시
for i in range(n+1):
    # 분
    for j in range(60):
        # 초
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)