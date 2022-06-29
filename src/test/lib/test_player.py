from cgi import test
from main.lib.player import Player
import pytest

@pytest.fixture()
def player():
    return Player(name="test")

def test_instatiate_of_player_object(player):
    test_player = player
    assert isinstance(test_player, Player)


CURRENCY_AMOUNTS = [-1,0,5,10,20,25,50,100,200,500,1000]
@pytest.mark.parametrize("test_amounts", CURRENCY_AMOUNTS)
def test_add_currency(player,test_amounts):
    test_player = player
    assert test_player.currency == Player("").currency
    test_player.add_currency(test_amounts)
    assert test_player.currency == Player("").currency + test_amounts
    
@pytest.mark.parametrize("test_amounts", CURRENCY_AMOUNTS)
def test_remove_currency(player,test_amounts):
    test_player = player
    assert test_player.currency == Player("").currency
    test_player.remove_currency(test_amounts)
    assert test_player.currency == Player("").currency - test_amounts
    