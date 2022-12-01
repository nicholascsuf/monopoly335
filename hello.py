import random

print("Welcome to the Monopoly Game");
numPlayers = int(input("Please enter number of players: "));
print(numPlayers);

class Player:
    id = 0;
    name="Player1";
    money_left=2000;

    def __init__(self,id,name):
        self.name = name
        self.id = id

playerArray = []
for i in range(numPlayers):
    playerName = input("Please enter player " + str(i) + " name :")
    plr = Player(i, playerName)
    print(plr.name)
    playerArray.append(plr);

def rollDice():
    print("rolling the dice")
    roll = random.randint(1, 6)
    print(roll)
i=0;

for i in range(len(playerArray)):
    plr = playerArray[i];
    print("Welcome, " + plr.name + "It's your turn")
    print("Money left: " + str(plr.money_left))
    print("Press ENTER to roll dice")
    rollDice()
