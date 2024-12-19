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
day night cycle effects encounter rate & materials available

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
    print('\n******************************')
    print(f'It is hour {game_time["hour"]} on day {game_time["day"]}')
    if 8 < game_time['sleep']:
        print('You are well rested')
    elif 4 < game_time['sleep']:
        print('You are tired')
    elif 0 < game_time['sleep']:
        print('You need sleep')
    else:
        print('You are sleep deprived')
    print('******************************\n')
    # End of get time
        
def random_utility():
    '''Generates a random utility part from list'''
    rand = random.randint(1,10)
    return rand
    # End of random utility
def random_weapon():
    '''Generates a random weapon part from list'''
    rand = random.randint(1,10)
    return rand
    # End of random utility
def random_champion():
    '''Generates a random champion part from list'''
    rand = random.randint(1,10)
    return rand
    # End of random champion

# - - - - - - - - - - - - - - - - - - - - -#- BUILD BOT -#- - - - - - - - - - - - - - - - - - - - - #

def build_bot():
    global scrap
    global player_bots
    cost = 100
    print()

    chasis = select_chasis()
    cost += chasis['cost']
    print()

    core = select_core()
    cost += core['cost']
    print()

    engine = select_engine()
    cost += engine['cost']
    print()

    specialty = select_specialty()
    print()

    name = input('Name your bot:    ')
    bot_loadout = {
        'name' : name,
        'max_hp' : chasis['health'],
        'hp' : chasis['health'],
        'armor' : chasis['armor'],
        'power' : engine['power'],
        'energy' : core['energy'],
        'specialty' : specialty,
        'parts' : {}
    }

    print(f"This robot specialises in {specialty} and is will use these parts")
    print(f"Chasis : {chasis['material']} | Core : {core['material']} | Engine : {engine['material']}")
    if specialty == 'Swarmer':
        cost -= cost / 2
    elif specialty == 'Striker':
        bot_loadout['power'] = bot_loadout['power'] * 1.5
    elif specialty == 'Defender':
        bot_loadout['health'] = bot_loadout['health'] * 2
        bot_loadout['armor'] = bot_loadout['armor'] + 10

    if scrap >= cost:
        print('Type y to build the robot?')
        question = input('Awaiting input: ')
        if question in ['y', 'Y', 'Yes', 'yes']:
            player_bots[name] = bot_loadout
    print('Exiting build mode.')
    get_time()
    # End of build bot
# Selecting bot parts
def select_chasis():
    print('Select a "Chasis", this will determine base defencive stats.')
    chasis = {
    '1' : {
        'material' : 'Wooden',
        'cost' : 50,
        'armor' : 0,
        'health' : 100
    },
    '2' : {
        'material' : 'Stone',
        'cost' : 75,
        'armor' : 10,
        'health' : 100
    },
    '3' : {
        'material' : 'Scrap Iron',
        'cost' : 150,
        'armor' : 15,
        'health' : 250
    },
    '4' : {
        'material' : 'Glass',
        'cost' : 150,
        'armor' : 100,
        'health' : 1
    },
    '5' : {
        'material' : 'Iron',
        'cost' : 250,
        'armor' : 25,
        'health' : 500
    },
    '6' : {
        'material' : 'Steel',
        'cost' : 500,
        'armor' : 50,
        'health' : 1000
    }
    }
    for option in chasis:
        player_select = chasis[option]
        cost = player_select['cost']
        material = player_select['material']
        print(f'{option} : {material} : {cost} Scrap')
    while True:
        question = input('Awaiting input: ')
        if question in chasis:
            chasis = {
                'material' : chasis[question]['material'],
                'cost' : chasis[question]['cost'],
                'armor' : chasis[question]['armor'],
                'health' : chasis[question]['health']
            }
            return chasis
        else:
            print('Enter a number.')
    # End of select chasis
def select_core():
    print('Select a "Core", this will determine avalible energy.')
    core = {
    '1' : {
        'material' : 'Copper Battery',
        'cost' : 5,
        'energy' : 50
    },
    '2' : {
        'material' : 'Car Battery',
        'cost' : 50,
        'energy' : 100
    },
    '3' : {
        'material' : 'Carbon',
        'cost' : 100,
        'energy' : 250
    },
    '4' : {
        'material' : 'Green',
        'cost' : 200,
        'energy' : 500
    },
    '5' : {
        'material' : 'Hydrogen',
        'cost' : 500,
        'energy' : 1000
    }
    }
    for option in core:
        player_select = core[option]
        cost = player_select['cost']
        material = player_select['material']
        print(f'{option} : {material} : {cost} Scrap')
    while True:
        question = input('Awaiting input: ')
        if question in core:
            core = {
                'material' : core[question]['material'],
                'cost' : core[question]['cost'],
                'energy' : core[question]['energy']
            }
            return core
        else:
            print('Enter a number.')
    # End of select core
def select_engine():
    print('Select a "Engine", this will determine attack and support stats.')
    engine = {
    '1' : {
        'material' : 'Toy',
        'cost' : 5,
        'power' : 20
    },
    '2' : {
        'material' : 'Car',
        'cost' : 50,
        'power' : 100
    },
    '3' : {
        'material' : 'Racecar',
        'cost' : 100,
        'power' : 150
    },
    '4' : {
        'material' : 'Truck',
        'cost' : 200,
        'power' : 200
    },
    '5' : {
        'material' : 'Jet',
        'cost' : 500,
        'power' : 250
    }
    }
    for option in engine:
        player_select = engine[option]
        cost = player_select['cost']
        material = player_select['material']
        print(f'{option} : {material} : {cost} Scrap')
    while True:
        question = input('Awaiting input: ')
        if question in engine:
            engine = {
                'material' : engine[question]['material'],
                'cost' : engine[question]['cost'],
                'power' : engine[question]['power'],
            }
            return engine
        else:
            print('Enter a number.')
    # End of select engine
def select_specialty():
    print('Bot specialty determines what a bot is made to do. But any bot can be any specialty.')
    specialties = {
    '1' : 'Striker', # Higher damage
    '2' : 'Defender', # Better armor and health
    '3' : 'Support', # Additional bot part slots
    '4' : 'Champion', # Allows champion parts to be equiped
    '5' : 'Swarmer' # Cheaper
    }
    for option in specialties:
        print(f'{option} : {specialties[option]}')
    question = input('Awaiting input: ')
    if question in specialties:
        specialty = specialties[question]
        return specialty
    else:
        print('Enter a number.')

def install_part():
    global player_bots
    print("Pick a robot, or type 'quit' to quit (Capitalisation matters)")
    counter = 0
    bot_list = []
    for bot in player_bots:
        bot_list.append(bot)
        print(f"{counter} : {bot}")
        counter += 1
    question = input('Awaiting input: ')
    if question.isdigit():
        question = bot_list[int(question)]
    if question in ['quit', 'Quit', 'QUIT']:
        return
    elif question in player_bots:
        selected_bot = player_bots[question] # Bot found
        specialty = selected_bot['specialty'] # Specialty found
        if specialty == 'Support': # Support?
            allowed_parts = 6
        else: 
            allowed_parts = 4
        if specialty == 'Champion': # Champion?
            champ = True
        else:
            champ = False
        
        print(f"You are installing parts in: {question}. Specialty : {specialty}")
        total_parts = 0 # Find part count
        if selected_bot['parts']: # Empty dict is false
            for part in selected_bot['parts']:
                total_parts += 1
        else:
            total_parts = 0

        installing = True
        while installing:
            if total_parts < allowed_parts:
                print("current installed parts:")
                if not selected_bot['parts']:
                    print('No parts installed')
                for part in selected_bot['parts']:
                    print(part)
                while installing:
                    print('Type in the part number you want to install, or "quit" to quit.')
                    print('Current owned parts:')
                    counter = 0
                    part_list = []
                    if weapon_parts:
                        print('\nWeapon Part List: ')
                        for part in weapon_parts:
                            print(f'{counter} : {part}')
                            part_list.append(part)
                            counter += 1
                    if utility_parts:
                        print('\nUtility Part List: ')
                        for part in utility_parts:
                            print(f'{counter} : {part}')
                            part_list.append(part)
                            counter += 1
                    if champion_parts and champ: # List parts
                        print('\nChampion Part List: ')
                        for part in champion_parts:
                            print(f'{counter} : {part}')
                            part_list.append(part)
                            counter += 1
                    # Stop listing
                    print() 
                    question = input('Awaiting input: ')
                    if question.isdigit:
                        question = int(question)
                        question = part_list[question]

                    if question.lower == 'quit':
                        installing = False
                    elif question in selected_bot['parts']:
                        print('Part is already in the bot.')
                    elif question in [part_list]:
                        print('Part found! installing...')
                        if champ:
                            for part in champion_parts:
                                if part == question:
                                    champion_parts.remove(part)
                                    apply_part(part, selected_bot)
                                    installing = False
                        for part in utility_parts:
                            if part == question:
                                utility_parts.remove(part)
                                apply_part(part, selected_bot)
                                return
                        for part in weapon_parts:
                            if part == question:
                                weapon_parts.remove(part)
                                apply_part(part, selected_bot)
                                return
                    else:
                        print('part not found.')
                else:
                    installing = False
        else:
            print('Exiting')
    # End Of installing parts
def apply_part(new_part, this_bot):
    if new_part == 'Blade':
        this_bot['parts']['Blade'] = {
            'name' : 'Blade',
            'type' : 'attack',
            'damage' : 100
        }
        print('Success!')
    
    # end of Apply Part
def next_event():
    global game_time
    events = ['Build bot', 'Scavange for resources']
    if game_time['hour'] >= 19:
        events.append('Sleep')
    if len(player_bots) >= 1:
        events.append('Install bot parts')
    get_time()
    print('\nWhat do you do now?')
    counter = 0
    for event in events:
        counter += 1
        print(f'{counter} : {event}')
    while True:
        question = input('Awaiting input: ')
        if question.isdigit():
            if int(question) <= len(events):
                question = events[int(question) - 1]
                break
            else:
                print('Please enter a number listed by an event')
        else:
            print('Please type a number.')
    print()
    if question == 'Build bot':
        build_bot()
    elif question == 'Scavange for resources':
        print('You scavenge for resources and look for? \n 1: 500 scrap \n 2: random utility part \n 3: random champion part')
        scavenge()
    elif question == 'Install bot parts':
        install_part()
def scavenge():
    while True:
        question = input('Awaiting input: ')
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
            print('Invalid input, material 1, 2 or 3.')
def list_bots():
    global player_bots
    names = []
    for bot in player_bots:
        names.append(bot)
    return names

# --- Variables --- #
game_time = {
    'day' : 1,
    'hour' : 1,
    'sleep' : 16
}
main_loop = True
scrap = 0
# Bots
player_bots = {}
utility_parts = []
weapon_parts = ['Blade', 'Blade']
champion_parts = []
# Game start
player_name = input('What is your name: ')
# print(f'{player_name} you are a roboticist, you have been assigned to defend the city from the next swarm of robots.')
# time.sleep(1)
# print('You have made it 50 miles deep into enemy territory and will make your stand here, you go to bed, your elite team by your side, you are ready!')
# time.sleep(1)
# print('You wake up to see your force destroyed, the telltale signs of a powerful emp mark the combatents, they won\'t repower in time.')
# time.sleep(1)
# print('You scrap the attacking robots')
# time.sleep(0.5)
gain_scrap(1000)
# time.sleep(0.5)
print('\nWhat do you use your destroyed force for? \n 1: 500 scrap \n 2: random utility part \n 3: random champion part')
scavenge()

while main_loop:
    next_event()
    print(f'Your bots: {list_bots()}')
    question = input('Oops! you made it to the end of the current build! quit?\n')
    if question == 'quit':
        break