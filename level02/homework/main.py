import turtle

def draw_rectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.beginfill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_triangle(x, y, base, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.goto(x + base / 2, y + height)
    turtle.goto(x + base, y)
    turtle.goto(x, y)
    turtle.end_fill()

def draw_castle():
    turtle.speed(10)

#Draw main building
    draw_rectangle(-150, -100, 300, 200, "gray")

#Draw side towers
    draw_rectangle(-200, -100, 50, 250, "darkgray")
    draw_rectangle(150, -100, 50, 250, "darkgray")

#Draw tower roofs
    draw_triangle(-200, 150, 50, 50, "red")
    draw_triangle(150, 150, 50, 50, "red")

#Draw central tower
    draw_rectangle(-50, 100, 100, 150, "darkgray")
    draw_triangle(-50, 250, 100, 60, "red")

#Draw doors
    draw_rectangle(-30, -100, 60, 100, "brown")

#Draw windows
    draw_rectangle(-100, 20, 40, 40, "black")
    draw_rectangle(60, 20, 40, 40, "black")

    turtle.hideturtle()
    turtle.done()

#Run the function
draw_castle()