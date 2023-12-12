# 10진수 N이 입력되면 2진수로 변환하여 출력하세요.
# 단, 재귀함수를 사용하여야 합니다.
# n = int(input())

a = []
def decimal_to_binary(n: int):
    if n == 0:
        return n
    a.append(n % 2)
    decimal_to_binary(n // 2)


decimal_to_binary(11)
print(a[::-1])
