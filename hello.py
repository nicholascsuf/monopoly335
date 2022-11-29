
print("Welcome to the Monopoly Game");
numPlayers = int(input("Please enter number of players: "));
print(numPlayers);


for i in range(numPlayers):
    playerName = input("Please enter player" + i + " name :");


def rollDice():
    print("rolling the dice");
    roll = random.randint(1, 6)
