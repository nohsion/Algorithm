# 10진수 N이 입력되면 2진수로 변환하여 출력하세요.
# 단, 재귀함수를 사용하여야 합니다.
# n = int(input())


def dfs(x: int):
    if x == 0:
        return
    dfs(x//2)
    print(x % 2, end='')  # 중요: 출력 순서를 거꾸로 하려면 dfs 함수 다음에 호출하도록 하면 됨


if __name__ == '__main__':
    dfs(11)
