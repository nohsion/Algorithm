# N개의 정수가 주어지면 그 숫자들 중 K개를 뽑는 조합의 합이 임의의 정수 M의 배수인 개수는 몇 개가 있는지 출력하는 프로그램을 작성하세요.
# 예를 들면 5개의 숫자 2 4 5 8 12가 주어지고, 3개를 뽑은 조합의 합이 6의 배수인 조합을 찾으면 4+8+12 2+4+12로 2가지가 있습니다.
"""
1. nCk 조합 dfs 함수
2. 그 합이 M의 배수인지 체크
                D(0,0) - init
    2         4      5      8   12
4 5 8 12    5 8 12  8 12    12

"""
def dfs(L, s, sum):
    global cnt
    if L == K:
        if sum % M == 0:
            cnt += 1
        return
    for i in range(s, N):
        # res[L] = nums[i]
        dfs(L+1, i+1, sum+nums[i])


if __name__ == '__main__':
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    M = int(input())
    # res = [0] * K  # 조합 경우를 임시 저장해놓는 변수
    cnt = 0

    dfs(0, 0, 0)
    print(cnt)
