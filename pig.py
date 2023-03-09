import turtle
def irma_setup():
    import tkinter
    turtle.setup(965, 600)
    wn = turtle.Screen()
    wn.title("Hurricane Irma")
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)
    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)
    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")
    return (t, wn, map_bg_img)
def irma():
    (t, wn, map_bg_img) = irma_setup()
    t.speed(7)
    data = open("data/irma.csv", "r").readlines()
    data[0] = data[1]
    t.penup()
    t.goto(float(data[0].split(",")[3]), float(data[0].split(",")[2]))
    t.pendown()
    for line in data:
        line = line.split(",")
        t.goto(float(line[3]), float(line[2]))
        if int(line[4]) >= 157:
            t.color("red")
            t.write('5')
        elif int(line[4]) >= 130:
                t.color("orange")
                t.write('4')
        elif int(line[4]) >= 111:
                t.color("yellow")
                t.write('3')
        elif int(line[4]) >= 96:
                t.color("green")
                t.write('2')
        elif int(line[4]) >= 74:
                t.color("blue")
                t.write('1')
        else:
            t.color("white")
            t.width(int(line[4])/8)
    turtle.done()
if __name__ == "__main__":
    irma()
