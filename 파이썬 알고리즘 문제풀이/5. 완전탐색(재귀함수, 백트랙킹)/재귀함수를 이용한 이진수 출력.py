# 10진수 N이 입력되면 2진수로 변환하여 출력하세요.
# 단, 재귀함수를 사용하여야 합니다.


def dfs(x: int):
    if x == 0:
        return
    # res.append(x % 2)
    dfs(x // 2)
    res.append(x % 2)


if __name__ == '__main__':
    n = int(input())
    res = []
    dfs(n)
    for a in res:
        print(a, end='')
