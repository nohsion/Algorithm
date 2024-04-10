import time
import turtle as t
import random as r


class Brick:
    def __init__(self):
        self.y = 0
        self.x = 6
        self.color = r.randint(1, 6)

    def move_left(self, grid):
        if grid[self.y][self.x-1] == 0 and grid[self.y+1][self.x-1] == 0:
            grid[self.y][self.x] = 0
            self.x -= 1

    def move_right(self, grid):
        if grid[self.y][self.x+1] == 0 and grid[self.y+1][self.x+1] == 0:
            grid[self.y][self.x] = 0
            self.x += 1


def draw_grid(block, grid):
    block.clear()
    top = 250
    left = -150
    colors = ['black', 'red', 'blue', 'orange', 'yellow', 'green', 'purple', 'white']
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            sc_x = left + (x*22)
            sc_y = top - (y*22)
            block.goto(sc_x, sc_y)
            block.color(colors[grid[y][x]])
            block.stamp()


if __name__ == '__main__':
    sc = t.Screen()
    sc.bgcolor("black")
    sc.tracer(False)
    sc.setup(width=500, height=600)
    # 게임판 움직일 수 있는 판
    grid = [[0] * 12 for _ in range(24)]
    # 벽 만들어주기(왼쪽, 오른쪽, 아래)
    for i in range(24):
        grid[i].insert(0, 7)
        grid[i].append(7)
    grid.append([7] * 14)
    for y in range(23, 20, -1):
        for x in range(1, 13):
            grid[y][x] = r.randint(1, 6)

    block = t.Turtle()
    block.penup()
    block.speed(0)
    block.shape("square")
    block.color("red")
    block.setundobuffer(None)

    brick = Brick()
    grid[brick.y][brick.x] = brick.color
    draw_grid(block, grid)

    sc.onkeypress(lambda: brick.move_left(grid), "Left")
    sc.onkeypress(lambda: brick.move_right(grid), "Right")
    sc.listen()

    while True:
        sc.update()
        if grid[brick.y+1][brick.x] == 0:
            grid[brick.y][brick.x] = 0
            brick.y += 1
            grid[brick.y][brick.x] = brick.color
        else:
            brick = Brick()


        draw_grid(block, grid)
        time.sleep(0.05)

    sc.mainloop()
