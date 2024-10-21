from turtle import *
import math 
# исходные данные
x = [30, -10, 3]
y = [40, 10, 4]
l = 100
# проверяем что точки x y разные
if x[0] != y[0] or x[1] != y[1] or x[2] != y[2]:
    # вычисляем нормализующий коэффицент
    nk = l / math.sqrt((y[1] - x[1]) ** 2 + (y[0] - x[0]) ** 2 + (y[2] - x[2]) ** 2)
    print (f'нормализующий коэффицент = {nk}')
    z = [nk * (y[0] - x[0]) + x[0] , nk * (y[1] - x[1]) + x[1] , nk * (y[2] - x[2]) + x[2]]
    print (z)
else :
    print ('точки x , y , z совпадают')
# dot painting func
def dotPaint (point):
    teleport ( point [0] , point [1] )
    dot (5)


home ()
setx (-10)
forward (210)
# стрелка
left (150)
forward (10)
left (180)
forward (10)
right (120)
forward (10)
right (180)
forward (10)
home ()
left (90)
sety (-10)
forward (210)
dotPaint (x)
dotPaint (y)
dotPaint (z)
# teleport ( x [0] , x [1] )
# dot (5)
# teleport ( y [0] , y [1] )
# dot (5)
# teleport ( z [0] , z [1] )
# dot (5)
teleport ( 0 , 0 )
mainloop ()
