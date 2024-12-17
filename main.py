# Ethan Lawrence
# Robot game
# Dec 13 2024
import time
import random
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
    scrap += amount
    print(f'+ {amount} scrap | you now have {scrap}')
    # End of gain scrap

def get_time():
    global game_time
    print(f'It is hour {game_time["hour"]} on day {game_time["day"]}')
    if 8 < game_time['sleep']:
        print('You are well rested')
    elif 4 < game_time['sleep']:
        print('You are tired')
    elif 0 < game_time['sleep']:
        print('You need sleep')
    else:
        print('You are sleep deprived')
    # End of get time
        
def random_utility():
    '''Generates a random utility part from list'''
    rand = random.randint(1,10)
    return rand
    # End of random utility

def random_champion():
    '''Generates a random champion part from list'''
    rand = random.randint(1,10)
    return rand
    # End of random champion

def build_bot():
    building = True
    while building:
        question = input('What slot do you with to build in? (example: 5)\n')
        if int(question) not in range(1, 11):
            print('Please enter a number between 1 and 10')
        else:
            selected_bot = f'bot{question}'
            question = input(f'What is bot{question}\'s name: ')
            health = 100
            armor = 10
            damage = 50
            support = 50
            energy = health + (armor * 10)
            bot_loadout = {
                'max_hp' : health,
                'hp' : health,
                'armor' : armor,
                'damage' : damage,
                'support' : support,
                'energy' : energy,
            }
            player_bots[selected_bot] = bot_loadout
    # End of build bot
# Selecting bot parts
def select_chasis():
    print('Select a "Chasis", this will determine base stats.')
    chasis = {
    '1' : {
        'material' : 'Wooden',
        'cost' : 50
    },
    '2' : 'Stone',
    '3' : 'Scrap Iron',
    '4' : 'Iron',
    '5' : 'Steel',
    '6' : 'Titainium'
    }
    time.sleep(1)
    for option in chasis:
        print(f'{option} : {chasis[option]['material']} : {chasis[option]['cost']}')
    while True:
        question = input('Awaiting imput: ')
        if question in chasis:
            break
        else:
            print('Enter a number.')
    

select_chasis()
# --- Variables --- #
game_time = {
    'day' : 1,
    'hour' : 1,
    'sleep' : 16
}
main_loop = True
scrap = 0
# Bots
player_bots = {
    'bot1' : 'Empty Slot',
    'bot2' : 'Empty Slot',
    'bot3' : 'Empty Slot',
    'bot4' : 'Empty Slot',
    'bot5' : 'Empty Slot',
    'bot6' : 'Empty Slot',
    'bot7' : 'Empty Slot',
    'bot8' : 'Empty Slot',
    'bot9' : 'Empty Slot',
    'bot10' : 'Empty Slot'
}

# Game start
player_name = input('What is your name: ')
print(f'{player_name} you are a roboticist, you have been assigned to defend the city from the next swarm of robots.')
time.sleep(1)
print('You have made it 50 miles deep into enemy territory and will make your stand here, you go to bed, your elite team by your side, you are ready!')
time.sleep(1)
print('You wake up to see your force destroyed, the telltale signs of a powerful emp mark the combatents, they won\'t repower in time.')
time.sleep(1)
print('You scrap the attacking robots')
time.sleep(0.5)
gain_scrap(1000)
time.sleep(0.5)
print('\nWhat do you use your destroyed force for? \n 1: 500 scrap \n 2: random utility part \n 3: random champion part')
while True:
    question = input('Awaiting imput: ')
    if question == '1':
        gain_scrap(500)
        break
    elif question == '2':
        random_champion()
        break
    elif question == '3':
        random_utility()
        break
    else:
        print('Invalid input, type 1, 2 or 3.')

while main_loop:
    get_time()
    print(player_bots)
    break