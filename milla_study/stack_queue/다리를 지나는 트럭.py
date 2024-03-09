from collections import deque


def solution(bridge_length, weight, truck_weights):
    w_trucks = deque(truck_weights)
    g_trucks = deque()
    res = 0

    while g_trucks or w_trucks:
        if g_trucks:
            if g_trucks[0][1] == 1:
                g_trucks.popleft()
            new_trucks = deque()
            for g in g_trucks:
                g[1] -= 1
                new_trucks.append(g)
            g_trucks = new_trucks

        if w_trucks and w_trucks[0] + sum(map(lambda x: x[0], g_trucks)) <= weight:  # 다리가 트럭의 무게를 견딜 수 있다면
            g_trucks.append([w_trucks.popleft(), bridge_length])
        res += 1

    return res
