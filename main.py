# main.py, CS 111 Final Project. Variation of the classic Frogger game.
# Code by Avery Blumenthal and Henrie Friesen
# Carleton College, CS 111 with David Liben-Nowell, last edited
#   June 5, 2020
# Uses graphics.py from Zelle "Python Programming: An Introduction
#   to Computer Science" (Franklin, Beedle & Associates).


import time
from random import randint
from graphics import *


class Car(GraphicsObject):
    '''A class for the moving cars, which are rectangular graphics objects.'''

    def __init__(self, startPoint, speed, color, window):
        self.start = startPoint
        self.x = self.start.getX()
        self.y = self.start.getY()
        self.speed = speed
        self.color = color
        self.window = window
        self.height = 40
        self.width = randint(60, 120)
        self.goingRight = True
        self.rectangle = Rectangle(startPoint, 
                                   Point(startPoint.getX() + self.width, 
                                   startPoint.getY() + self.height))
        self.rectangle.setFill(color)
        self.rectangle.draw(window)

    def step(self):
        '''Moves the Car object by a given dx and changes its direction if
        it is at either end of the grahpics window boundary.'''

        # Local variable dx is positive or negative depending on direction
        if self.goingRight:
            dx = self.speed
        else:
            dx = -self.speed

        # Updates the car's x position
        self.x = self.x + dx

        # If at either window boundary, reverses the value of self.goingRight
        if self.x + dx >= 750 - self.width:
            self.goingRight = False
        elif self.x + dx <= 0:
            self.goingRight = True
        
        self.rectangle.move(dx, 0)

    def getStart(self):
        '''Returns the starting position as a Point object.'''
        return self.start
            
    def getSpeed(self):
        ''' Returns the speed of the car.'''
        return self.speed

    def getColor(self):
        '''Returns the color of the car.'''
        return self.color


class Road(GraphicsObject):
    '''A class for the horizontal roads that the five initial cars move in.'''

    def __init__(self, startPoint, window):
        self.startPoint = startPoint
        self.width = window.getWidth()
        self.height = 50   
        self.rectangle = Rectangle(startPoint, 
                                   Point(window.getWidth(),
                                   startPoint.getY() + self.height))
        self.rectangle.setFill(color_rgb(100, 100, 100))                           
        self.rectangle.draw(window)


class Player(GraphicsObject):
    '''A class for a user-controlled player.'''

    def __init__(self, color, window):
        self.start = Point(window.getWidth() // 2, 525)
        self.color = color
        self.radius = 20
        self.window = window
        self.circle = Circle(self.start, self.radius)
        self.circle.setFill(color)
        self.circle.draw(window)

    def handleKey(self, window):
        '''Handles user's key-presses and moves the Player object 
        correspondingly.'''

        self.center = self.circle.getCenter()
        self.x, self.y = self.center.getX(), self.center.getY()
        # Checks for a user key input and moves the Player correspondingly
        key = window.checkKey()
        if key == "a":
            if self.x > 30:
                self.circle.move(-50, 0)
        elif key == "w":
            if self.y > 30:
                self.circle.move(0, -50)            
        elif key == "d":
            if self.x < 720:
                self.circle.move(50, 0)
        elif key == "s":
            if self.y < 520:
                self.circle.move(0, 50)
   
   
class FroggerGame:
    '''A class for the Frogger game.'''

    def __init__(self, cars, player, window):
        self.window = window
        self.cars = cars
        self.player = player
        self.level = 1
        self.gameover = False
        self.youWin = False
    
    def gameStatusUpdate(self):
        '''Using the player's position and the boundaries of the cars, 
        returns True if the game is over (player has touched a car), or False
        if the game is not over.'''
        
        # Variables for the Player object's position
        playerRightX = self.player.x + self.player.radius
        playerLeftX = self.player.x - self.player.radius
        playerTopY = self.player.y - self.player.radius
        playerBottomY = self.player.y + self.player.radius
        
        # If any part of the player object is in contact with any part
        # of a car, then the game is over
        for car in self.cars:
            carX, carY = car.x, car.y
            carH, carW = car.height, car.width
            if (carX <= playerRightX <= carX + carW and \
                carY <= playerTopY <= carY + carH) \
            or (carX <= playerRightX <= carX + carW and \
                carY <playerBottomY <= carY + carH) \
            or (carX <= playerLeftX <= carX + carW and \
                carY <playerTopY <= carY + carH) \
            or (carX <= playerLeftX <= carX + carW and \
                carY <playerBottomY <= carY + carH):
                self.gameover = True

        return self.gameover        

    def levels(self):
        '''Increases the level by one and creates a new car if the player
        reaches the top of the screen. If all five levels have been completed,
        sets self.youWin to True. Pauses for one second between levels.'''

        # If the Player is at the top of the screen
        if self.player.y == 25:
            self.level += 1
            if self.level == 6:
                self.youWin = True
            else:
                print("You're on level", self.level)
            
            # Creates a new car and appends it to the list of cars    
            newCar = Car(Point(randint(0, 750), 405 - 100 * (self.level - 2)),25,
            color_rgb(randint(0,255),randint(0,255),randint(0,255)), self.window)
            self.cars.append(newCar)
            # Moves player down to the starting y position
            self.player.circle.move(0, 500)
            # Pauses 1 second between levels
            time.sleep(1)

    def victory(self):
        '''Returns True if the user has won.'''
        if self.youWin:
            return True


def instructions():
    '''Prints the game's instructions and returns the user's input of desired
    player color.'''

    print("Reach the top of the screen to complete the level!")
    print("Use a, s, d, and w keys to move.")
    print("Avoid the cars as you go.")
    print("Complete all 5 levels to win the game!")
    print("")
    userColor = str.lower(input(
                        "Type red, blue, green or random for user color: "))
    print("Click in the window to begin")
    print("You're on level 1")

    return userColor

   
def createRoads(window):
    '''Creates the five roads that the level-1 cars move in.'''
    for i in range(5):
        road = Road(Point(0, 50 + i * 100), window)   


def createCars(window):
    '''Creates and returns the five level-1 Car objects as a list.'''
    
    cars = []
    for i in range(5):
        car = Car(Point(randint(0, 630), 55 + (100 * i)), randint(10, 15), 
              color_rgb(randint(0,255), randint(0,255), randint(0,255)), window)
        cars.append(car) 
    return cars            


def main():
    # Creates a graphics window.
    window = GraphWin("Let's play some games!", 750, 550)
    userColor = instructions()
    createRoads(window)
    
    # Creates a Player object with the appropriate color.
    if userColor == "red" or userColor == "blue" or userColor == "green":
        player = Player(userColor, window)
    else:
        player = Player(color_rgb(randint(0,255), randint(0,255), 
                        randint(0,255)), window)
    
    # Names the list of cars and passes them into the FroggerGame object.
    cars = createCars(window)
    game = FroggerGame(cars, player, window)
    
    # Repeats this loop every 0.025 seconds, which checks for user input,
    # updates and moves the Car and Player objects, increments the level if 
    # applicable, and breaks the loop if the game is lost or won.
    while True:
        for car in cars:
            car.step()
        player.handleKey(window)
        game.levels()
        game.gameStatusUpdate()
        # .gameStatusUpdate() returns True if the game is lost
        if game.gameStatusUpdate():
            print("Game over")
            break
        elif game.victory():
            print("YOU WIN!!!")
            break    
        
        time.sleep(0.025)

if __name__ == "__main__":
    main()