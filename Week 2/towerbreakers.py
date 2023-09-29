def towerBreakers(n, m):
    # Check if the number of towers or the tower height is even
    # If either is even, Player 2 wins; otherwise, Player 1 wins
    if n % 2 == 0 or m == 1:
        return 2  # Player 2 wins
    else:
        return 1  # Player 1 wins