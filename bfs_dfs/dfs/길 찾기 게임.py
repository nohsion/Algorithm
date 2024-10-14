# https://school.programmers.co.kr/learn/courses/30/lessons/42892

import sys
sys.setrecursionlimit(10 ** 6)  # 파이썬 재귀 limit 늘려주는 코드


def make_tree(num_node_info):
    def insert(cn, tn, tx, ty):
        # 현재 num값, 넣어줄 타겟 num,x,y
        (cx, cy), cl, cr = tree[cn]
        if tx < cx:  # x가 더 작으면, left
            if cl == 0:  # left가 비어 있으면, 바로 넣어준다.
                tree[cn][1] = tn
                tree[tn] = [(tx, ty), 0, 0]
            else:
                insert(cl, tn, tx, ty)  # left 자식으로 들어가자!
        else:
            if cr == 0:  # right가 비어 있으면, 바로 넣어준다.
                tree[cn][2] = tn
                tree[tn] = [(tx, ty), 0, 0]
            else:
                insert(cr, tn, tx, ty)

    tree = {}
    n, x, y = num_node_info.pop(0)
    tree[n] = [(x, y), 0, 0]  # (x,y)좌표, left, right
    rootn = n  # 트리 root 번호

    while num_node_info:
        cn, cx, cy = num_node_info.pop(0)
        insert(rootn, cn, cx, cy)

    # x,y 좌표만 있는 트리로 변경
    xy_tree = {}
    for tk in tree.keys():
        xy_tree[tk] = (tree[tk][1], tree[tk][2])
    return xy_tree


def preord(cn):
    if len(v_pre) == N:
        return
    cl, cr = tree[cn]

    v_pre.append(cn)
    # left
    if cl != 0:  # left 자식이 있는 경우에만
        preord(cl)
    # right
    if cr != 0:  # right 자식이 있는 경우에만
        preord(cr)


def postord(cn):
    if len(v_post) == N:
        return
    cl, cr = tree[cn]

    # left
    if cl != 0:
        postord(cl)
    # right
    if cr != 0:
        postord(cr)
    v_post.append(cn)


def solution(nodeinfo):
    global N, v_pre, v_post, tree
    N = len(nodeinfo)

    num_node_info = []
    for i, [x, y] in enumerate(nodeinfo, 1):
        num_node_info.append((i, x, y))
    num_node_info.sort(key=lambda x: (-x[2], x[1]))
    rootn = num_node_info[0][0]  # 루트 넘버 지정

    tree = make_tree(num_node_info)  # 이진 트리 만들기

    v_pre = []
    preord(rootn)

    v_post = []
    postord(rootn)

    ans = [v_pre, v_post]
    return ans