from game import game, print_header, build_three_rolls, get_players_name, game_loop


def test_game():
    assert game() == None
    assert print_header() == None
    assert build_three_rolls == False
    assert get_players_name == None
    assert game_loop() == None


