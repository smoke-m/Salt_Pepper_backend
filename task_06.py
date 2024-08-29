class WrongNumberOfPlayersError(Exception):
    """Если количество игроков больше 2."""

    pass


class NoSuchStrategyError(Exception):
    """Если ход игроков отличается от 'R', 'P' или 'S'."""

    pass


def rps_game_winner(arr):
    """
    Принимает на вход массив следующей структуры
    [["player1", "P"], ["player2", "S"] ],
    где P - бумага, S - ножницы, R - камень.
    """
    if len(arr) != 2:
        raise WrongNumberOfPlayersError()
    for val in arr:
        if val[1] not in ["P", "S", "R"]:
            raise NoSuchStrategyError()
    pair_val = dict(
        P="R",
        S="P",
        R="S",
    )
    if arr[0][1] == pair_val[arr[1][1]]:
        return f"{arr[1][0]} {arr[1][1]}"
    elif arr[1][1] == pair_val[arr[0][1]]:
        return f"{arr[0][0]} {arr[0][1]}"
    else:
        return f"{arr[0][0]} {arr[0][1]}"
