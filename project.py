import random, time, sys
from golem import raawr
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

# Create a class for all Characters
class Character:
    def __init__(self, life):
        self.life = life

    # Getter
    @property
    def life(self):
        return self._life

    # Setter
    @life.setter
    def life(self, life):
        self._life = life

    # Decrease life per n
    def hp(self, n):
        return self.life - n


# Create a subclass for Player
class Player(Character):

    # Attack choices
    attacks = [
        {
            "name": "fire",
            "dmg": 8,
            "description": "🔥 You throw a fireball in his direction. \n The impact was good but the flames disperce, you cant set fire to stone",
        },
        {
            "name": "water",
            "dmg": 12,
            "description": "🌊 You water-beam his torso! \n The rock starts cracking",
        },
        {
            "name": "punch",
            "dmg": 4,
            "description": "✊ You try to make this a fistfight by punching him. \n His stonelike body is too hard",
        },
        {
            "name": "super_attack",
            "dmg": random.randrange(15, 31),
            "description": "You feel a strange surge of power coming from within. \n ⚡You unleash a bolt of destruction towards the Golem",
        },
    ]

    # Attack choice
    def attack(self, choice, monster):
        # Find the attack of user's input
        attack = [d for d in Player.attacks if d["name"] == choice]
        # Lower Monster's hp
        monster.life = monster.hp(attack[0]["dmg"])
        typescript(attack[0]["description"])

    # Printingplayer's life
    def __str__(self):
        return f"Player[{self.life}]"


# Create a subclass for Monster
class Monster(Character):

    # Attack patterns
    attacks = [
        {
            "name": "roar",
            "dmg": 6,
            "description": "The golem roars in anger!  \n Your ears start bleeding",
        },
        {
            "name": "Punch",
            "dmg": 8,
            "description": "The golem punches you in the face!! \n Awch",
        },
        {
            "name": "Throw",
            "dmg": 10,
            "description": "The golem throws a huge rock at you!!! \n ✨✨ You see stars",
        },
    ]

    # Random attack
    def attack(self, player):
        # Pick an attack randomly
        attack = random.choice(self.attacks)
        # Lower Players hp
        player.life = player.hp(attack["dmg"])
        # Return description
        typescript(attack["description"])

    # Printintg monster's life
    def __str__(self):
        return f"Monster[{self.life}]"


def game_play(player, monster):
    # Start a while loop
    while player.life > 0 and monster.life > 0:
        print(f"{Fore.GREEN}-----------Your Turn------------")
        # Call extra_attack() if player's life is below 20
        if player.life <= 20:
            extra_attack(player, monster)
        # Else call player_attack_pattern()
        else:
            player_attack_pattern(player, monster)
        # End game if monster dies and break
        if monster.life <= 0:
            break
        # Show player and monster hp
        print(f"{Style.DIM}{player} ---------- {monster}")
        time.sleep(1)
        print(f"{Fore.RED}----------Monster Turn-----------")
        monster.attack(player)
        # End game if player dies and break
        if player.life <= 0:
            break
        # Show player and monster hp
        print(f"{Style.DIM}{player} ---------- {monster}")
        time.sleep(1)
    # Call check-life() to see if u win or lose
    check_life(player, monster)


# Player's attack pattern
def player_attack_pattern(player, monster):
    typescript("Your attack choices: (1)fire (2)water (3)punch")
    # Users input
    choice = input("You choose: ").lower()
    # Perform an attack based on input
    if choice == "1" or choice == "fire":
        player.attack("fire", monster)
    elif choice == "2" or choice == "water":
        player.attack("water", monster)
    elif choice == "3" or choice == "punch":
        player.attack("punch", monster)
    # If not correct input, make player lose turn
    else:
        typescript("You panic in fear, but the Golem is coming at you!!")
        print(
            "<Your options are either the numbers corresponding to the attack or the attack itself>"
        )


# Perform an extra attack
def extra_attack(player, monster):
    typescript("On the verge of death, you discover a new ability...")
    # Get user's input
    choice = input("(1)fire (2)water (3)punch (4)unknown").lower()
    # If user pick the (4):extra attack
    if choice == "4" or choice == "unknown":
        # Generate a random number 1-3
        random_attack = random.randrange(1, 4)
        if random_attack == 1:
            typescript("It's a Health Potion!")
            # Heal player
            player.life *= 3
            print(player)
        elif random_attack == 2:
            typescript("Super Lucky Attack ! !")
            # Unleash super attack
            player.attack("super_attack", monster)
            print(monster)
        else:
            typescript("Action surge!! \nYou gain 2 attacks.")
            # Run player's attack pattern x2
            player_attack_pattern(player, monster)
            typescript("Now your extra attack:")
            player_attack_pattern(player, monster)


# Check the game result
def check_life(player, monster):
    # If player is alive and monster is dead print win
    if player.life >= 0 and monster.life <= 0:
        print(f"{Back.GREEN}{Style.BRIGHT}     You win!!!     ")
    # Else print lose
    else:
        print(f"{Back.RED}{Style.BRIGHT} Game over! You lose... ")


# Delay text function
def typescript(text):
    # Loop through each character
    for char in text + "\n":
        # Write character in terminal
        sys.stdout.write(char)
        sys.stdout.flush()
        # Delay next character
        time.sleep(0.08)
        if char == "\n":
            time.sleep(0.4)


def main():
    # Initialize player and monster
    player = Player(60)
    monster = Monster(80)
    typescript("You encounter a huge creature made of stone mud and rock.")
    # Golem ascii art by TEXTART.io
    raawr()
    typescript("You have a plethora of attacks at your disposal. Pick one!")
    # Start game
    game_play(player, monster)


if __name__ == "__main__":
    main()
