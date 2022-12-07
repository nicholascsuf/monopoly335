#335 Project Fall Semester 2022
#Last Modified: December 7th, 2022 by Nicholas J. Harney
#Instructor: Naveen Yalla
#Nicholas Harney
#Sri
#Monika

import random

print("Welcome to the Monopoly Game");
numPlayers = int(input("Please enter number of players: "));
print(numPlayers);

class Property:
    name= "";
    cost = 0.00;
    owner = "";
    avail = 1;

class Lot:
    color = "blue";
    utilitiesOwned = "";
    rent = 0;
    housePrice = 0.00;
    hotelOwned = "";
    housesOwned = "";



class Player:
    id = 0;
    name="Player1";
    money_left=2000;
    properties = []
    bankrupt = 1;
    railroadsOwned = "";
    utilitiesOwned = "";

    def __init__(self,id,name):
        self.name = name
        self.id = id



class Card:
    def __init__(self, card_name, color_group, card_cost, house_cost, houses_built, rent_prices, mortgage_amt, owner, mortgaged):
        self.card_name = card_name                  # string
        self.color_group = color_group              # string
        self.card_cost = card_cost                  # integer
        self.house_cost = house_cost                # integer
        self.houses_built = houses_built            # integer
        self.rent_prices = rent_prices              # integer
        self.mortgage_amt = mortgage_amt            # integer
        self.owner = owner                          # string
        self.mortgaged = mortgaged                  # boolean

go = Card("Go", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "Bank", False)
med_ave = Card("Mediterranean Avenue", "Brown", 60, 50, 0, {0: 2,
                                                                      1: 10,
                                                                      2: 30,
                                                                      3: 90,
                                                                      4: 160,
                                                                      5: 250}, 30, "Bank", False)
comm_chest = Card("Community Chest", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "Bank", False)
baltic_ave = Card("Baltic Avenue", "Brown", 60, 50, 0, {0: 4,
                                                                  1: 20,
                                                                  2: 60,
                                                                  3: 180,
                                                                  4: 320,
                                                                  5: 450}, 30, "Bank", False)
income_tax = Card("Income Tax", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "Bank", False)
reading_rr = Card("Reading Railroad", "Railroad", 200, "N/A", "N/A", "N/A", 100, "Bank", False)
oriental_ave = Card("Oriental Avenue", "Light Blue", 100, 50, 0, {0: 6,
                                                                            1: 30,
                                                                            2: 90,
                                                                            3: 270,
                                                                            4: 400,
                                                                            5: 550}, 50, "Bank", False)
chance = Card("Community Chest", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "Bank", False)
vermont_ave = Card("Vermont Avenue", "Light Blue", 100, 50, 0, {0: 6,
                                                                          1: 30,
                                                                          2: 90,
                                                                          3: 270,
                                                                          4: 400,
                                                                          5: 550}, 50, "Bank", False)
conn_ave = Card("Connecticut Avenue", "Light Blue", 120, 50, 0, {0: 8,
                                                                           1: 40,
                                                                           2: 100,
                                                                           3: 300,
                                                                           4: 450,
                                                                           5: 600}, 60, "Bank", False)
    # new row
jail = Card("Jail/Visiting Jail", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "Bank", False)
st_charles_place = Card("St. Charles Place", "Pink", 140, 100, 0, {0: 10,
                                                                             1: 50,
                                                                             2: 150,
                                                                             3: 450,
                                                                             4: 625,
                                                                             5: 750}, 70, "Bank", False)
electric_company = Card("Electric Company", "Utilities", 150, "N/A", "N/A", "N/A", 75, "Bank", False)
states_ave = Card("States Avenue", "Pink", 140, 100, 0, {0: 10,
                                                                   1: 50,
                                                                   2: 150,
                                                                   3: 450,
                                                                   4: 625,
                                                                   5: 750}, 70, "Bank", False)
virginia_ave = Card("Virginia Avenue", "Pink", 160, 100, 0, {0: 12,
                                                                       1: 60,
                                                                       2: 180,
                                                                       3: 500,
                                                                       4: 700,
                                                                       5: 900}, 80, "Bank", False)
penn_rr = Card("Pennsylvania Railroad", "Railroad", 200, "N/A", "N/A", "N/A", 100, "Bank", False)
st_james_place = Card("St. James Place", "Orange", 180, 100, 0, {0: 14,
                                                                           1: 70,
                                                                           2: 200,
                                                                           3: 550,
                                                                           4: 750,
                                                                           5: 950}, 90, "Bank", False)
    # comm chest
ten_ave = Card("Tennessee Avenue", "Orange", 180, 100, 0, {0: 14,
                                                                     1: 70,
                                                                     2: 200,
                                                                     3: 550,
                                                                     4: 750,
                                                                     5: 950}, 90, "Bank", False)
ny_ave = Card("New York Avenue", "Orange", 200, 100, 0, {0: 16,
                                                                   1: 80,
                                                                   2: 220,
                                                                   3: 600,
                                                                   4: 800,
                                                                   5: 1000}, 100, "Bank", False)
free_parking = Card("Free Parking", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "Bank", False)
    # rotate
kentucky_ave = Card("Kentucky Avenue", "Red", 220, 150, 0, {0: 18,
                                                                      1: 90,
                                                                      2: 250,
                                                                      3: 700,
                                                                      4: 875,
                                                                      5: 1050}, 110, "Bank", False)
    # chance
indiana_ave = Card("Indiana Avenue", "Red", 220, 150, 0, {0: 18,
                                                                    1: 90,
                                                                    2: 250,
                                                                    3: 700,
                                                                    4: 875,
                                                                    5: 1050}, 110, "Bank", False)
illinois_ave = Card("Illinois Avenue", "Red", 240, 150, 0, {0: 20,
                                                                      1: 100,
                                                                      2: 300,
                                                                      3: 750,
                                                                      4: 925,
                                                                      5: 1100}, 120, "Bank", False)
bno_rr = Card("B. & O. Railroad", "Railroad", 200, "N/A", "N/A", "N/A", 100, "Bank", False)
atlantic_ave = Card("Atlantic Avenue", "Yellow", 260, 150, 0, {0: 22,
                                                                         1: 110,
                                                                         2: 330,
                                                                         3: 800,
                                                                         4: 975,
                                                                         5: 1150}, 130, "Bank", False)
ventnor_ave = Card("Ventnor Avenue", "Yellow", 260, 150, 0, {0: 22,
                                                                       1: 110,
                                                                       2: 330,
                                                                       3: 800,
                                                                       4: 975,
                                                                       5: 1150}, 130, "Bank", False)
water_works = Card("Water Works", "Utilities", 150, 0, 0, {1: 100}, 75, "Bank", False)
marvin_gardens = Card("Marvin Gardens", "Yellow", 280, 150, 0, {0: 24,
                                                                          1: 120,
                                                                          2: 360,
                                                                          3: 850,
                                                                          4: 1025,
                                                                          5: 1200}, 140, "Bank", False)
    # rotate
go_to_jail = Card("Go to Jail", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "Bank", False)
pacific_ave = Card("Pacific Avenue", "Green", 300, 200, 0, {0: 26,
                                                                      1: 130,
                                                                      2: 390,
                                                                      3: 900,
                                                                      4: 1100,
                                                                      5: 1275}, 150, "Bank", False)
nc_ave = Card("North Carolina Avenue", "Green", 140, 200, 0, {0: 26,
                                                                        1: 130,
                                                                        2: 390,
                                                                        3: 900,
                                                                        4: 1100,
                                                                        5: 1275}, 150, "Bank", False)
    # comm chest
penn_ave = Card("Pennsylvania Avenue", "Green", 300, 200, 0, {0: 28,
                                                                        1: 150,
                                                                        2: 450,
                                                                        3: 1000,
                                                                        4: 1200,
                                                                        5: 1400}, 160, "Bank", False)
short_line_rr = Card("Short Line", "Railroad", 200, "N/A", "N/A", "N/A", 100, "Bank", False)
    # chance
park_place = Card("Park Place", "Blue", 350, 200, 0, {0: 35,
                                                                1: 175,
                                                                2: 500,
                                                                3: 1100,
                                                                4: 1300,
                                                                5: 1500}, 175, "Bank", False)
luxury_tax = Card("Luxury Tax", "N/A", "N/A", "N/A", "N/A", "N/A", 0, "Bank", False)
boardwalk = Card("Boardwalk", "N/A", 400, 200, 0, {0: 50,
                                                             1: 200,
                                                             2: 600,
                                                             3: 1400,
                                                             4: 1700,
                                                             5: 2000}, 200, "Bank", False)
    # end


gameBoard = [
            go,
            med_ave,
            comm_chest,
            baltic_ave,
            income_tax,
            reading_rr,
            oriental_ave,
            chance,
            vermont_ave,
            conn_ave,
            jail,
            st_charles_place,
            electric_company,
            states_ave,
            virginia_ave,
            penn_rr,
            st_james_place,
            comm_chest,
            ten_ave,
            ny_ave,
            free_parking,
            kentucky_ave,
            chance,
            indiana_ave,
            illinois_ave,
            bno_rr,
            atlantic_ave,
            ventnor_ave,
            water_works,
            marvin_gardens,
            go_to_jail,
            pacific_ave,
            nc_ave,
            comm_chest,
            penn_ave,
            short_line_rr,
            chance,
            park_place,
            luxury_tax,
            boardwalk
    ]



playerArray = []
for i in range(numPlayers):
    playerName = input("Please enter player " + str(i) + " name :")
    plr = Player(i, playerName)
    print(plr.name)
    playerArray.append(plr);

def rollDice():
    print("rolling the dice")
    roll = random.randint(1, 6)
    print("You rolled a " + str(roll) )
    return roll

i=0;

for i in range(len(playerArray)):
    plr = playerArray[i];
    print("Welcome, " + plr.name + " It's your turn")
    print("Money left: " + str(plr.money_left))
    print("Properties :")
    textIn = input("Press ENTER to roll dice")
    if textIn == "":
        result = rollDice()
    else: print("Try again")
    print("You landed on " + gameBoard[result].card_name)
