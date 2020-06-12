Description of our game and its features:

Our program allows the user to play the game of "frogger". The goal of the game is
for the player to cross the roads without getting hit by the cars, which are
constantly moving back and forth across the screen. If the player
safely reaches the other side of the screen, then you move on to the next level
and restart at the bottom of the screen. With each new level, one more car is added,
making each level increasingly more difficult. There are 5 total levels in the game.
If you pass all five levels (which we have found to be suprisingly difficult), then
you have beaten the game and the game stops, with the text "YOU WIN!!!" being
printed on the screen. If you get hit by a vehicle at any point on any level, you
lose and the game immediately stops, and "Game over" is printed on the screen.
We decided to add some features to make the graphics and layout of our game more
interesting. The user has the ability to pick between red, blue, green, and random
for the color of the player, which is created as a circle. The cars, which are
rectangles, are created newly for each game. The size, color and speed of each car is
randomized (within a range) for each game. This makes the game more variable and more
exciting for the user. At the start of the game, instructions on how to play are
printed and the user is prompted to pick a color for the player, as mentioned
earlier. Then on each successive level, the level is printed on the screen so that the
user knows where they're at. Other than that, the only text that is printed is
"Game over" or "YOU WIN!!!", depending on the outcome of the game, of course.
Our game is similar to frogger in the player's goal, but it has differences in the
layout and the movement of the cars on the screen. We hope that the user enjoys
this new and exciting game!


A brief description/justification of how it is constructed
    (class organization, how data are stored, etc.):

The game is organized into four classes, with a number of functions built-in to help
also. The Car, Road, and Player classes are subclasses of the GraphicsObject class in 
graphics.py. There is a car class, which deals with how the cars are designed. The car
objects take a starting point, speed, color and  window as parameters. The Car class
deals with these parameters and the size and shape of the cars and when the cars are
moving in what direction. The Road class creates the road objects, which take a 
starting point and a window as parameters. The roads are rectangles that extend
horizontally from one edge of the screen to the other. The cars "drive" back and
forth on the roads. The Player class creates the player object, which is what the
user moves in order to play the game. The player object takes a color and a window
as parameters. This class deals with player movement. It accepts input from the user,
who can press the "a", "s", "d", and "w" keys to move left, down, right and up,
respectively. The FroggerGame class deals more with game play. It takes cars, a player
and a window as parameter. This class uses the position of the cars and the player
to tell if the player is ever "hit" by one of the cars, in which case the game is over.
Additionally, this class deals with the levels. Whenever the player reaches the top of
the screen, the next level is created, with a new car at a fast speed being added. This
class ultimately updates at any point whether or not the game is over, which could occur
when the user loses or wins. The function "main" is also important for game play. Within
this function, the window that the game is played in is created and there are calls to
the four classes in the program. It is also within "main" that the car movement in terms
of steps is outlined, and the print statements and game breaks that occur when a game
ends are located here. Data-wise, the five initial cars are created in the createCars
function and are added to a list. For each new level, within the levels method of the
FroggerGame class, a new car is appended to this list. Two key pieces of data that are
always being kept track of are the car and the player locations. For the car locations,
only the x-value is tracked because the cars are moving horizaontally, so once the cars
are drawn in, their vertical position and therefore y-value never changes. The car
locations are tracked as the variable self.x in the step method of the car class.
The player position is tracked as self.x and self.y in the handleKey method of the
Player class. The x and y values refer to the center of the circle that is the player.


A discussion of the current status of your program—what works and what doesn’t, 
    etc.:

The program works mostly how we imagined it working. This includes the movement
and placement of the cars and the player, the progression of levels, the
conditions under which the game is won/lost, and the inputs/outputs presented
to the user. Some things that don't work quite as we hoped include the fact
that the game may begin to lag a bit, especially as higher levels and thus more
cars are created and updated. Another thing we noted is that occasionally, when
the user inputs their desired player color before the game begins, the program
crashes and an error message for line 1 is displayed. This doesn't appear to
happen every time, and when it does, it has always worked for us the second time
we attempted to run it. One other design element we chose to keep is a pause
of one second after the user completes a level and is moved back to the bottom
bar. Keypresses during this time result in the player being moved once the pause
ends, which was unintentional but added an extra layer of frustration to the
user's experience, so we decided to keep it.


Instructions for running your program:

Our program can be found in main.py. Instructions should be printed when
the user clicks "run" on the top of the screen in repl.it. Once the user
clicks "run," the user will also be prompted to input a color for their
character. Typing anything other than 'red,' 'blue,' or 'green,'
(regardless of capitilization), will choose a random color. Sometimes,
apparently only on the first try, the program will say there is an error
on line 1 in response to this input, but upon pressing "run" again, we found
that it then worked. Once the user types a color and hits <enter> on their 
keyboard, the user must click their mouse within the graphics window before 
their key presses will make the player move. If the player loses or wins
the game, they must press the "run" button to start a new game.