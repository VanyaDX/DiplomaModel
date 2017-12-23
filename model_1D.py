from tkinter import *
from time import *


class Ball:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="red")

    def move_ball(self, deltax, deltay):
        #deltax = randint(0,5)
        #deltay = randint(0,5)
        self.canvas.move(self.ball, deltax, deltay)
        #self.canvas.after(50, self.move_ball)


def init_newb(self, balls):
    for i in range(0, 5):
        self.append([balls[i + 1][0], 0])


xsize = 800
ysize = 500
line = ysize // 2
root = Tk()
canvas = Canvas(root, width=xsize, height=ysize)
canvas.pack()
diapason = 0

start = 10
end = 790
step = 20
speed = 10

canvas.create_line(0, line, xsize, line)
canvas.create_line(start, line - 20, start, line + 20)
canvas.create_line(end, line - 20, end, line + 20)
#oval = canvas.create_oval(0, 0, 10, 10)

# initialize root Window and canvas
#root = Tk()
#root.title("Balls")
#root.resizable(False,False)
#canvas = Canvas(root, width = 300, height = 300)
#canvas.pack()

# create two ball objects and animate them
balls = [[]]
N = 10
step = 3
speed = 1
for i in range(0, N):
    balls.append([Ball(canvas, start, line - 5, start + 10, line + 5), speed, start, True])
    start += step
    #ball2 = Ball(canvas, end - 10, line - 5, end, line + 5)

newb = [[]]
#init_newb(newb, balls)
newb = balls
oldb = balls
coef = 1
end = 781
start = 9
print(newb)

while True:
    for i in range(0, N):
        if (newb[i + 1][2] >= end) and (newb[i + 1][1] > 0):
            newb[i + 1][1] = -newb[i + 1][1]
            newb[i + 1][2] += newb[i + 1][1]
            newb[i + 1][3] = False
        elif (newb[i + 1][2] <= start) and (newb[i + 1][1] < 0):
            newb[i + 1][1] = -newb[i + 1][1]
            newb[i + 1][2] += newb[i + 1][1]
            newb[i + 1][3] = False
        elif (i == 0):
            #if (newb[i + 1][2] >= end - speed) or (newb[i + 1][2] <= start + 10):
            if newb[i + 1][1] < 0:
                speedf = - speed
                #speedf = - oldb[N][1]
            else:
                speedf = speed
                #speedf = oldb[N][1]
            newb[i + 1][1] = newb[i + 1][1] - coef * (newb[i + 1][1] - speedf)
            newb[i + 1][2] += newb[i + 1][1]
            newb[i + 1][3] = True
        elif (newb[i + 1][1] * oldb[i][1] < 0):
            newb[i + 1][1] = newb[i + 1][1] - coef * (newb[i + 1][1] + oldb[i][1])
            newb[i + 1][2] += newb[i + 1][1]
        else:
            newb[i + 1][1] = newb[i + 1][1] - coef * (newb[i + 1][1] - oldb[i][1])
            newb[i + 1][2] += newb[i + 1][1]
    oldb = newb
    #print(newb)
    for i in range(0, N):
        newb[i + 1][0].move_ball(balls[i + 1][1], 0)
        #newb[i + 1][2] += newb[i + 1][1]
    #ball2.move_ball(-10, 0)
    root.update()
    sleep(0.005)
    for i in range(0, N):
        print(i +1, newb[i + 1][1], newb[i + 1][2], newb[i + 1][3])

root.mainloop()