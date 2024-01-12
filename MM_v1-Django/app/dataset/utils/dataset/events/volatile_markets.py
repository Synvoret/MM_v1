def volatile_markets(event: object = None) -> dict[str, str]:
    """
    Notes: 

    Remove the Demand Tokens from every port on the board 

    and replace them with new random Deman Tokens.

    event: Event Card object.
    """

    data = {
        "function1": "drawDemandToken",
        "arg1": "all",
    }

    return data
