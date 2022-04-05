'''
lambda 함수
'''


def plus_one(x):
    return x + 1


print(plus_one(4))

plus_two = lambda x: x + 2  # 람다 함수에 이름 붙이기 (근데 이러는 것은 사실 람다 사용의미가 없음)
print(plus_two(5))

a = [1, 2, 3, 4, 5]
print(list(map(plus_one, a)))
print(list(map((lambda x: x + 1), a)))  # 람다 사용법 (함수명에다가 그냥 람다함수를 넣어버림)

# sort에서 많이 쓰임
data = ['but', 'i', 'wont', 'hesitate', 'no', 'more', 'no', 'more', 'it', 'cannot', 'wait', 'im', 'yours']
data = list(set(data))  # set을 이용한 중복 제거
data.sort(key=lambda x: len(x))
print(data)
