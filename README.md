# Final Project --- Mini Game

CS50's Introduction to Programming with Python

#### Video Demo: <https://youtu.be/toC70pcs49Y>

### Description:

A mini-game built in Python where the user encounters a Golem. The user is able to choose one of the three available attack choices (fire, water, punch). The Golem(computer) has also three attack patterns which are randomly generated. Both of them begin with a standard health pool which during the fight is decreasing. The last man standing is the winner of the game!

### Project Structure:

#### project (.py)

##### Classes

###### -- class Character:

The class for all characters.
This class includes the attribute life, a getter and setter function and the function hp which is responsible of the players' health decrease.

###### -- class Player:

A sub-class of the class Character for the user.
This class includes the attribute attacks, it is a list of dictionaries with the name, the damage and the description of each attack. It also includes a print function and the function attack. The last one, given the user's choice it is searching for the specific input in the list, lowers the Golem's life through hp function and prints the description.

###### -- class Monster

A sub-class of the class Character for the Golem.
This class includes the attribute attacks, it is a list of dictionaries with the name, the damage and the description of each attack. It also includes a print function and the function attack. The last one, picks an attack randomly from the list, lowers the user's life through hp function and prints the description.

##### Functions

###### -- game_play():

It is responsible for the main game play while both the user and the Golem are still alive. On user's turn, it calls the extra_attack() if the user's life is below 20, otherwise it calls the player_attack_pattern(). On Golem's turn, the function attack is called. In both cases, the user's and the Golem's updated life are printing in the terminal. If one of them dies the check_life() is called.

###### -- player_attack_pattern():

It prompts the user for an attack choice and based on his input it calls the attack funtion for the player. If the input is incorrect, the user loses his turn.

###### -- extra_attack():

It is responsible for the extra attack that pops up when the user's life is below 20 health. The user now has a fourth choice and it is a random attack between a healing potion that increases user's life 3 times, a super power attack that strikes randomly somewhere between (15,30) and a double attack that gives the opportunity to the user to attack twice in his turn.

###### -- check_life():

It checks the game result and returns a corresponding message.
If the user is still alive and the Golem is dead, then it is a winning message, otherwise it is not.

###### -- typescript():

It is a delay text function. Given a text it loops through each character and prints the character in terminal with some delay.

###### -- main():

Initiliaze the Player and the Monster. Prints the Golem and starts the game.

#### test_project (.py)

##### Functions

###### -- test_hp():

We create a Player and a Monster object and we call the hp() with a random number, asserting that their life decreased by this number.

###### -- test_player_attack():

We create a Player and a Monster object and we call the attack() for each player's attack choice, asserting that monster's life decreased by the number of the damage of the attack.

###### -- test_monster_attack():

We create a Player and a Monster object and we call the attack() for the monster, asserting that player's life decreased by the number of the damage of any monster's attack.

###### -- test_check_life():

We create a Player and a Monster object. In the first case, the Monster is dead so after calling the check_life() we assert that it will be a winning message. In the second case, the Player is dead and check_life() returns a losing message.

#### golem (.py)

##### Functions

###### -- raawr():

Golem made with ASCII art by TEXTART.io

### Requirements:

- pytest
- colorama
