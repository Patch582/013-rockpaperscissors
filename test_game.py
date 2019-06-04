from game import game, print_header, build_three_rolls, get_players_name, game_loop


def test_game():
    assert game() == True
    assert print_header() == True
    assert build_three_rolls == True
    assert get_players_name == True
    assert game_loop() == True


