
def permutations():
    arr = [10, 20, 30, 40, 50]
    r = 3
    cb = [-1] * r  # 조합 r개를 담는 변수 (인덱스)
    cnt = 0

    def dfs(L):
        nonlocal cnt
        if L == r:
            cnt += 1
            for i in range(r):
                print(arr[cb[i]], end=' ')
            print()
            return
        for i in range(len(arr)):
            if i not in cb:
                cb[L] = i
                dfs(L+1)
                cb[L] = -1
    dfs(0)
    print(f"총 경우의 수: {cnt}")


def product():
    arr = [10, 20, 30, 40, 50]
    r = 3
    cb = [-1] * r
    cnt = 0

    def dfs(L):
        nonlocal cnt
        if L == r:
            cnt += 1
            for i in range(r):
                print(arr[cb[i]], end=' ')
            print()
            return
        for i in range(len(arr)):
            cb[L] = i
            dfs(L+1)
    dfs(0)
    print(f"총 경우의 수: {cnt}")




if __name__ == '__main__':
    print("1. 순열")
    permutations()
    print("==============================")

    print("2. 중복 순열")
    product()
    print("==============================")