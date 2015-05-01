# BattleTanks

Battle Tanks is a two player artillery shooting game in a distributed environment. The objective of the game is to blow the opponent's tank using weapons at your disposal, while dodging the weapons hurled at you by your opponent.

System Requirements:
Please ensure you have the following installed in your machine before trying to run this game.

Server: Python 2.7+
Client: Python 2.7+, PyGame 1.9+

The game can run on any OS, but has been developed and tested primarily on Windows platform.

Directions to run the program:

* Locate the server file "GameServer.py" and run it on the machine where you want to host the server. The Server needs Python 2.7+ installed. To know whether or not Python is installed on your target machine, open the command prompt and type in "python --version" to check the version of python running on that machine. Run the GameServer.py file using the command "py GameServer.py"

* To run the client, locate the menu.py file and run it using command "py menu.py". It is recommended that you run separate clients on separate machines. 

* The menu pops up. Click on play to start playing. Enter the IP addess of the server (the machine you used in Step 1). Click on Quit to exit. Press ESC during any point in the game to exit the game.

Game Controls:

* The game controls are simple. Left and right arrow keys to move the tank.
* Up and down arrow keys to move the gun.
* ALT to activate the shield
* CTRL to fire napalm
* SPACE to fire cannons
* Icons are available for each weapon for each tank to indicate cooldown times, and available weapons that can be fired by each player
* Health bars indicate current level of health of each player

Note: It is recommended that you do not run any computationally intensive programs on the same machine while the client is running. It is recommended that you put the laptop in High Performance and plug in the charger while playing this game for best results. 
