n = int(input())
data: list[str] = [input().lower() for _ in range(n)]  # 문자열 리스트

# 1. 파이썬 문자열 슬라이싱 방법
for i, x in enumerate(data):
    if x == x[::-1]:
        print(f"#{i+1} YES")
    else:
        print(f"#{i+1} NO")


# 2. 문자열 앞뒤 인덱스 비교
for i, x in enumerate(data):
    size = len(x)
    is_palindrome: bool = True
    for j in range(size // 2):
        if x[j] != x[size - j - 1]:
            is_palindrome = False
            break
    if is_palindrome is True:
        print(f"#{i + 1} YES")
    else:
        print(f"#{i + 1} NO")
