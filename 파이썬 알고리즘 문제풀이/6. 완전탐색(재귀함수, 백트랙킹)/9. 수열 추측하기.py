# 가장 윗줄에 1~N까지의 숫자가 한개씩 적혀있을때, 파스칼 삼각형처럼 위 두개를 더한 값이 아랫줄에 저장된다.
# 가장 윗줄의 숫자 개수 N, 가장 아랫줄의 숫자 F가 주어졌을 때, 가장 윗줄의 숫자들을 출력하세요.
"""
(아이디어)
{1,2,3,4}의 모든 순열 경우에서 파스칼 삼각형처럼 더했을때 결과가 16이 나오는지 확인해야 한다.
1. 모든 순열 구하는 dfs 함수 만들기
2. 파스칼 삼각형 합 구하는 함수 만들기
"""

# 모든 순열을 구하는 dfs 함수
def dfs(L):
    if L == N:
        combs.append(res[::])
        return
    for i in range(1, N+1):
        if ch[i] == 0:
            ch[i] = 1
            res[L] = i
            dfs(L+1)
            ch[i] = 0


# 파스칼 삼각형의 합 구하는 함수 만들기 (DFS)
def pascal_sum_dfs(S):
    if len(S) == 1:
        return S[0]
    next = []
    for i in range(len(S)-1):
        next.append(S[i]+S[i+1])
    return pascal_sum_dfs(next)


# 파스칼 삼각형의 합 구하는 함수 만들기 (수학적 계산) -- 아래 식이 아닌것 같음..
# def pascal_sum_math(S):
#     n = len(S)
#     res = 0
#     for i in range(n):
#         if i == 0 or i == n-1:
#             res += S[i]
#         else:
#             res += S[i]*(n-1)
#     return res


if __name__ == '__main__':
    N, F = map(int, input().split())  # 4 16
    ch = [0] * (N+1)  # 사용여부 체크 변수
    res = [0] * N  # 순열 경우를 저장하는 임시 변수
    combs = []  # 모든 순열을 저장하는 변수
    dfs(0)

    for c in combs:
        # 만약 동일하면 사전순 오름차순으로 해야 함.
        # 그런데 오름차순별로 combs에 저장된 상태이므로 바로 종료하면 된다.
        if pascal_sum_dfs(c) == F:
            for x in c:
                print(x, end=' ')
            break


