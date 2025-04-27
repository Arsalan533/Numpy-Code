import numpy as np

# players = np.random.randint(10 ,50, (5 ,3))
# print("All players:\n", players)

# my_team = players[[0, 2, 3]]
# print("My team (Player 1, 3, 4):\n", my_team)

players = np.random.randint(10, 50, (4, 3))
print("All players :\n", players)

my_team = players[[0, 2]]
print("My team (player 1, 3, 4) :\n", my_team)