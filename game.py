
def build_three_rolls():
    pass


def get_players_name():
    pass


def game_loop():
    pass


def print_header():
    print('----------------------------------')
    print('       Rock Paper Scissors')
    print('----------------------------------')
    print('')

def game():
    print_header()

    rolls = build_three_rolls()

    player1 = get_players_name()

    game_loop()


if __name__ == '__main__':
    game()
