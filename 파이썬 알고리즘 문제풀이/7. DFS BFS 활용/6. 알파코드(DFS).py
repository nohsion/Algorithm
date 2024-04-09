# 철수와 영희는 서로의 비밀편지를 암호화해서 서로 주고받기로 했다. 그래서 서로 어떻게 암호화를 할 것인지 의논을 하고 있다.
# 영희: 우리 알파벳 A에는 1로, B에는 2로 이렇게 해서 Z에는 26을 할당하여 번호로 보내기로 하자.
# 철수: 정말 바보같은 생각이군!! 생각해 봐!! 만약 내가 "BEAN"을 너에게 보낸다면 그것을 암호화하면 25114이잖아!!
# 그러면 이것을 다시 알파벳으로 복원할 때는 많은 방법이 존재하는 데 어떻게 할건데...
# 이것을 알파벳으로 바꾸면 BEAAD, YAAD, YAN, YKD 그리고 BEKD로 BEAN말고도 5가지나 더 있군.
# 당신은 위와 같은 영희의 방법으로 암호화된 코드가 주어지면 그것을 알파벳으로 복원하는데 얼마나 많은 방법인 있는지 구하세요.

# 알파벳은 A=1 ~ Z=26까지 존재
"""
25114
            init D(0, '')
        1           2
    2 D(1, 'B')      25 D(2, 'Y')
...
"""
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def dfs(i, letter):
    global res
    # 자릿수 넘어가면 종료
    if i > len(code):
        return
    # 딱 맞게 종료
    if i == len(code):
        print(letter)
        res += 1
        return
    for idx in range(1, 3):
        if idx == 2 and code[i] == '0':
            continue
        num = int(code[i:i+idx])
        if 1 <= int(num) <= 26:
            dfs(i+idx, letter+alphabet[num-1])


if __name__ == '__main__':
    code = input()  # 25114
    res = 0
    dfs(0, '')
    print(res)
