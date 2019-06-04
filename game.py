from actors import Player, Roll


def build_three_rolls():
    rolls = [
        Roll('rock', 'scissors', 'paper'),
        Roll('scissors', 'paper', 'rock'),
        Roll('paper', 'rock', 'scissors'),
    ]
    return rolls


def get_players_name():

    return input("What's your name? ")


def game_loop(player1, player2, rolls):
    print()
    print('Player1: [{}] Player2: [{}] 3rolls [{}]'.format(player1, player2, rolls))
    print()


def print_header():
    print('----------------------------------')
    print('       Rock Paper Scissors')
    print('----------------------------------')
    print('')


def game():
    print_header()

    rolls = build_three_rolls()

    name = get_players_name()
    player1 = Player(name)
    player2 = Player('Laptop')

    game_loop(player1, player2, rolls)


if __name__ == '__main__':
    game()
