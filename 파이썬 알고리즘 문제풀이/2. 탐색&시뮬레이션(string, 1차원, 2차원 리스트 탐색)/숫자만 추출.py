data = input()

# 1. 배열에 넣은 후, join 하는 방법
only_num = []
for x in data:
    if x.isdigit():  # isdecimal()이 좀더 정확
        only_num.append(x)
real_num = int("".join(only_num))
print(real_num)

# 2. 바로 숫자로 계산하는 방법
real_num = 0
for x in data:
    if x.isdigit():
        real_num = real_num*10 + int(x)
print(real_num)

yaksu_cnt = 0
for i in range(1, real_num+1):
    if real_num % i == 0:
        yaksu_cnt += 1
print(yaksu_cnt)
