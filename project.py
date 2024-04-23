import random
import json

# Load JSON data
with open('project.json', 'r') as file:
    data = json.load(file)
    team1_ships = data['team_andriy']['ships_types']
    team2_ships = data['team_bot']['ships_types']

# Define function to simulate battle
def simulating_battle(andriy_ships, bot_ships):
    team1 = andriy_ships.copy()
    team2 = bot_ships.copy()

    # Print initial ship information
    print("Battle INFO:")
    print("Andriy's ships:", team1)
    print("Bot's ships:", team2)
    print()

    # Start the battle loop
    while team1 and team2:
        attack1 = random.choice(team1)
        attack2 = random.choice(team2)

        damage1 = random.uniform(0.25 * attack1['strength'], attack1['strength'])
        damage2 = random.uniform(0.25 * attack2['strength'], attack2['strength'])

        attack2['health'] -= damage1
        attack1['health'] -= damage2

        if attack1["health"] <= 0:
            team1.remove(attack1)
        if attack2['health'] <= 0:
            team2.remove(attack2)

        print("Andriy's team attacks bot's team", attack2)
        print("Bot's team attacks andriy's team", attack1)
        print("Andriy's team", team1)
        print("Bot's team", team2)
        print()

    # Determine the winner
    if team1:
        print('Andriy wins')
    else:
        print("Bot wins")

# Run the simulation
simulating_battle(team1_ships, team2_ships)
