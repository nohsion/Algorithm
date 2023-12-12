# Anagram 알파벳의 나열 순서는 다르지만 그 구성이 일치하면 두 단어는 아나그램이라고 합니다.
# 두 단어가 아나그램인지 판별하세요. (대소문자 구분)
from collections import defaultdict

a = input()
b = input()


def is_anagram(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    a_dict = defaultdict(int)
    b_dict = defaultdict(int)
    for i in range(len(a)):
        a_dict[a[i]] += 1
        b_dict[b[i]] += 1
    if a_dict == b_dict:
        return True
    else:
        return False



result = is_anagram(a, b)
print('YES') if result else print('NO')
