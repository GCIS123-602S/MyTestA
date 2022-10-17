import turtle 

pixelSize = 15

def turtleSettings(): 
    turtle.speed(15)
    turtle.tracer(False)
    
def drawSquare():
    turtle.begin_fill()
    turtle.down()
    i = 0
    while i < 4:
        turtle.fd(pixelSize) 
        turtle.rt(90) 
        i += 1
    turtle.up()
    turtle.end_fill()
    turtle.fd(pixelSize)

def draw_20x20_checkerboard(numberPixels):
    i = numberPixels
    while i > 0:
        turtle.up()
        turtle.setpos(0, pixelSize * i) 
        turtle.down()
        i = i - 1

        for x in range(numberPixels):
            if (x + i) % 2 == 0:
                pencolor = 'black'
            else: 
                pencolor = 'red'
            turtle.color(pencolor)
            drawSquare()

def main():
    turtleSettings()
    draw_20x20_checkerboard(20)
    input("END")
    
main() 