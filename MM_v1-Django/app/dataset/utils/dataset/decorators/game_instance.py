from game.models import Game


def game_instance(func):
    """A decorator that adds a game instance to a view or model function"""
    """Decorator adds a game instance to a view or model function."""
    def wrapper(request, *args, **kwargs):
        game = Game.objects.get(number=100)
        return func(request, game, *args, **kwargs)
    return wrapper
