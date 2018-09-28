from turtle import *
def koch(levels, size):
    # solution
    if levels == 0:
        fd(size)
    else:
        koch(levels-1, int(size/3))
        lt(60)
        koch(levels-1, int(size/3))
        rt(120)
        koch(levels-1, int(size/3))
        lt(60)
        koch(levels-1, int(size/3))


setup(1.0,1.0)
for i in range(4):
    koch(i, 500)
    clear()
    reset()
exitonclick()
