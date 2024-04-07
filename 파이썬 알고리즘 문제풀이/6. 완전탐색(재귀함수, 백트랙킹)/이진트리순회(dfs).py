"""
아래 이진 트리를 전위순회, 중위순회, 후위순회로 출력하세요.
   1
 2   3
4 5 6 7

전위순회: 1245367
중위순회: 4251637
후위순회: 4526731
"""


# 전위순회 (일반적인 순회. 먼저 처리하고 다음 노드로 간다.)
def dfs_pre(v):
    if v > 7:
        return
    print(v, end='')
    dfs_pre(v * 2)
    dfs_pre(v * 2 + 1)


# 중위순회
def dfs_in(v):
    if v > 7:
        return
    dfs_in(v * 2)
    print(v, end='')
    dfs_in(v * 2 + 1)


# 후위순회 (ex. merge sort)
def dfs_post(v):
    if v > 7:
        return
    dfs_post(v * 2)
    dfs_post(v * 2 + 1)
    print(v, end='')


if __name__ == '__main__':
    dfs_pre(1)
    print()
    dfs_in(1)
    print()
    dfs_post(1)
