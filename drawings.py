#import os
import turtle 

#ADJUSTING TURTLE NEW ROW LINE FORWARDING PROCESS
adjustPicture = 20

#PIXEL SIZE
pixelSize = 10

def turtleSettings(): 
    turtle.speed(10)
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
    
def nextRow(): 
    turtle.rt(90)
    turtle.fd(pixelSize)
    turtle.rt(90)
    turtle.fd(adjustPicture*pixelSize)
    turtle.lt(180)
    turtle.down()


def drawBlack():
    turtle.fillcolor('black')
    drawSquare()    

def drawWhite():
    turtle.fillcolor('white')
    drawSquare()

def drawYellow():
    turtle.fillcolor('yellow')
    drawSquare()

def drawOrange():
    turtle.fillcolor('orange')
    drawSquare()
    
def drawYellowGreen():
    turtle.fillcolor('yellowgreen')
    drawSquare()

def drawSeinna():
    turtle.fillcolor('sienna')
    drawSquare()
    
def drawTan():
    turtle.fillcolor('tan')
    drawSquare()
    
def drawGray():
    turtle.fillcolor('gray')
    drawSquare()
    
def drawDarkGray():
    turtle.fillcolor('darkgray')
    drawSquare()

def drawRed():
    turtle.fillcolor('red')
    drawSquare()    

def translateColor(string):
    if string == "0": 
        drawBlack()
        return True
    elif string == "1":
        drawWhite()
        return True
    elif string == "2":
        drawRed()
        return True
    elif string == "3":
        drawYellow()
        return True
    elif string == "4":
        drawOrange()
        return True
    elif string == "5":
        drawYellow()
        return True
    elif string == "6":
        drawYellowGreen()
        return True
    elif string == "7":
        drawSeinna()
        return True
    elif string == "8":
        drawTan()
        return True
    elif string == "9":
        drawGray()
        return True
    elif string == "A":
        drawDarkGray()
        return True
    else:
        print("Invalid Color - Terminating the program :(") 
        return False
 
def main():    
    #print(os.getcwd())

    turtleSettings()
    scanSequence = input("Enter a valid sequence color: ")

    interrupt = False
    while interrupt == False:
        for string in scanSequence: 
            if translateColor(string) == False:
                interrupt = True
                break        
        nextRow()
        if interrupt == False:
            scanSequence = input("Enter a valid sequence color: ")


main()