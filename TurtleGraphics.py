#TurtleGraphics.py
#Name: Ayo Fatoye
#Date: 23 September, 2024
#Assignment: Turtle Talkin'

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides)
      
def fillCorner(alice, corner):
    #draw a big square
    drawSquare(alice,100)
    
    if corner==1:
        alice.begin_fill()
        drawSquare(alice,50)
        alice.end_fill()
    elif corner==2:
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice,50)
        alice.end_fill()
    elif corner==3:
        alice.right(90)
        alice.forward(50)
        alice.left(90)
        alice.begin_fill()
        drawSquare(alice,50)
        alice.end_fill()
    elif corner==4:
        alice.right(90)
        alice.forward(50)
        alice.left(90)
        alice.up()
        alice.forward(50)
        alice.down()
        alice.begin_fill()
        drawSquare(alice,50)
        alice.end_fill()

def squaresInSquares(sean, amount):
    size=400
    sean.up()
    sean.goto(-200,200)
    sean.down()
    
    for s in range(amount):
        drawSquare(sean, size)
        size-=30
        sean.up()
        sean.forward(10)
        sean.right(90)
        sean.forward(10)
        sean.left(90)
        sean.down()
  
    

        

def main():
    myTurtle = turtle.Turtle()

#Drawing A Square
    #drawSquare(myTurtle,100)
    
#Drawing a Polygon
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon
    #drawPolygon(myTurtle,3)
#Corners
    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.
    # fillCorner(myTurtle, 4)


   # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
