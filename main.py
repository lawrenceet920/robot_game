# Ethan Lawrence
# Robot game
# Dec 13 2024
import time
"""
Plan:
Build and upgrade your bots
challange other bots
equip special predefined and user generated weapons
Fight final boss
"""

# Building
"""pick combat style (DPS, Tank, Support, Champion, Swarm)
    + damage, + armor & Health, + utility slots, + Champion slots, lower build cost
upgrade combat style
apply stat-pool (energy cost)
    Damage, speed, health, armor, support, energy overflow
apply equipment / abilitys
    AOE, DOT, Temp stat buff(self and others), Gather scrap, negate damage, taunt, heal, (?Summon?)
confirm construction"""

# Timeslots
"""pick one of a few challangers | with some info of bot power (Number of bots, cost est)
Select special event (clone a bot, buff a bot, scrap pile, sell a bot, Theft, bot specific mission {drill part can mine})
build a bot takes up a timeslot
day night cycle effects encounter rate & types available

sleep deprication?
rest encounters"""

# Combat
"""Set battle stakes - scrap, capture robot, Gain time
Instruct each bot to do something (pokemon doubles)
other team does random action
both actions execute based on bot speed
bots take damage and could break or need repairs
if hit it high damage cause bot malfunction (lower stats and systems offline)"""
def gain_scrap(amount):
    global scrap
    print(f'+ {amount} scrap | you now have {scrap}')
game_time = {
    'day' : 1,
    'hour' : 1,
    'sleep' : 16
}
scrap = 0
player_name = input('What is your name: ')
print(f'{player_name} you are a roboticist, you have been assigned to defend the city from the next swarm of robots.')
print('You have made it 50 miles deep into enemy territory and will make your stand here, you go to bed, your elite team by your side, you are ready!')
time.sleep(1)
print('You wake up to see your force destroyed, the telltale signs of a powerful emp mark the combatents, they won\'t repower in time.')
print('You scrap the attacking robots')
gain_scrap(1000)
print('What do you use your destroyed force for? \n 1: 500 scrap \n 2: random utility part \n 3: random champion part')
while True:
    question = input('Awaiting imput: ')
    if question == '1':
        gain_scrap(500)
    elif question == '2':
        print('utility')
    elif question == '3':
        print('champion')
    else:
        print('Invalid input, type 1, 2 or 3.')
