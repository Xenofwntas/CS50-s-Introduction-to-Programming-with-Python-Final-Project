import project
from colorama import Back, Style

def test_hp():
    player = project.Player(100)
    player.life = player.hp(5)
    assert player.life == 95
    monster = project.Monster(100)
    monster.life = monster.hp(5)
    assert monster.life == 95


def test_player_attack():
    player = project.Player(100)
    monster = project.Monster(100)
    player.attack("fire", monster)
    assert monster.life == 92
    player.attack("water", monster)
    assert monster.life == 80
    player.attack("punch", monster)
    assert monster.life == 76


def test_monster_attack():
    player = project.Player(100)
    monster = project.Monster(100)
    monster.attack(player)
    assert player.life == 94 or player.life == 92 or player.life == 90


def test_check_life():
    player = project.Player(100)
    monster = project.Monster(0)
    assert project.check_life(player, monster) == f"{Back.GREEN}{Style.BRIGHT}     You win!!!     "
    player = project.Player(0)
    monster = project.Monster(100)
    assert project.check_life(player, monster) == f"{Back.RED}{Style.BRIGHT} Game over! You lose... "
