'''
2차원 리스트 생성과 접근
'''

# 1차원 리스트 생성
a = [0] * 3
print(a)

# 2차원 리스트 (리스트 컴프리헨션)
b = [[0]*3 for _ in range(3)]
print(b)

for i_list in b:
    for i in i_list:
        print(i, end=' ')
    print()