# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVJ-_6qfsDFAWg#

def inord(n):
    global cnt
    if n <= N:
        inord(n*2)  # 자식 left
        lst[n] = cnt
        cnt += 1
        inord(n*2 + 1) # 자식 right

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cnt = 1
    lst = [0]*(N+1)

    inord(1)

    print(f"#{test_case} {lst[1]} {lst[N//2]}")
