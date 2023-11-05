import  turtle

draw = turtle.Turtle()

#for i in range (4):
#   draw.forward(100)
#  draw.right(90)

#num_side = 360
#side_leght = 0.5
#angle = 360.0 / num_side

#for i in range(num_side):
#   draw.forward(side_leght)
#   draw.right(angle)



#window = turtle.Screen()
#window.bgcolor("deeppink")
#window.title("My window for turtle")

#draw.color("white")

#def shapefun(size, sides):
#   for i in range(sides):
#      draw.fd(size)
#     draw.left(360.0 / sides)
#    size = size + 5

#shapefun(150, 4)
#shapefun(170, 4)
#shapefun(190, 4)
#shapefun(210, 4)
#shapefun(230, 4)

window2 = turtle.Screen()
pen = turtle.Pen()
pen.penup()
pen.goto(-220, 50)
pen.pendown()

def drawM():
    pen.right(90)
    pen.forward(40)
    pen.left(180)
    pen.forward(40)
    pen.right(135)
    pen.forward(40)
    pen.left(90)
    pen.forward(40)
    pen.left(225)
    pen.forward(40)
drawM()

pen.left(90)
pen.penup()
pen.forward(30)
pen.pendown()

def drawa(A):
    pen.right(35)
    pen.forward(40)
    pen.left(35)
    pen.forward(40)
    pen.right(135)
    pen.forward(40)
    pen.left(90)
    pen.forward(40)
    pen.left(225)
    pen.forward(40)

#colors = ['red', 'yellow', 'orange', 'green', 'skyblue', 'indigo', 'darkblue', 'purple', 'pink']
#window2.bgcolor('black')
#turtle.speed(109034)

#for i in range(3846):
#    var = i / 100 + 1
#    pen.pencolor(colors[i%9])
#    pen.width(var)
#    pen.forward(i)
#    pen.left(60)







turtle.done()
turtle.exitonclick()