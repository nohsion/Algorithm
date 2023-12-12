# Anagram 알파벳의 나열 순서는 다르지만 그 구성이 일치하면 두 단어는 아나그램이라고 합니다.
# 두 단어가 아나그램인지 판별하세요. (대소문자 구분)
a = input()
b = input()


def is_anagram(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    s1 = sorted(list(map(str, a)))
    s2 = sorted(list(map(str, b)))
    for i in range(len(a)):
        if s1[i] != s2[i]:
            return False
    return True


result = is_anagram(a, b)
print('YES') if result else print('NO')
