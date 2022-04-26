def mergesort(l):
    if len(l) < 2: # 길이가 1이면 sorted된 것이라 볼 수 있음
        return l
    mid = len(l) // 2
    left = mergesort(l[:mid])
    right = mergesort(l[mid:])
    return merge(left, right) # Key Subroutine: MERGE

def merge(left, right):
    arr = []
    i = 0
    j = 0
    while i < len(left) and j < len(right): # 한 배열이라도 끝나면 비교 종료
        if left[i] <= right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
    # 둘 중에 뭔지는 모르겠지만 남은 배열 합쳐주기 (각 배열은 이미 정렬되어 있기 때문에 just concatenate)
    arr += left[i:]
    arr += right[j:]
    return arr


l = [38, 41, 6, 100, 27, 43, 3, 9, 82, 10]
print(mergesort(l))