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
    # Add time
    game_time["hour"] += 1
    game_time["sleep"] -= 1
    if game_time["hour"] == 25:
        game_time['day'] += 1
        game_time["hour"] = 1
    time.sleep(0.5)
    # Tell Time
    print('\n******************************')
    print(f'It is {game_time["hour"]}:00 on day {game_time["day"]}')
    if 8 < game_time['sleep']:
        print('You are well rested')
    elif 4 < game_time['sleep']:
        print('You are tired')
    elif 0 < game_time['sleep']:
        print('You need sleep')
    else:
        print('You are sleep deprived')
    print('******************************\n')
    time.sleep(0.5)
    # End of get time
        

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

    while True:
        name = input('Name your bot:    ')
        if name not in player_bots:
            break
        else:
            print('Please use a unique name.')
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
        bot_loadout['max_hp'] = bot_loadout['max_hp'] * 2
        bot_loadout['hp'] = bot_loadout['hp'] * 2
        bot_loadout['armor'] = bot_loadout['armor'] + 10

    if scrap >= cost:
        print('Type y to build the robot?')
        question = input('Awaiting input: ')
        if question in ['y', 'Y', 'Yes', 'yes']:
            player_bots[name] = bot_loadout
            scrap -= cost
    else: 
        print('You do not have enough scrap to build this.')
        time.sleep(1)
    print('Exiting build mode.')
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
    counter = 1
    bot_list = []
    for bot in player_bots:
        bot_list.append(bot)
        print(f"{counter} : {bot}")
        counter += 1
    question = input('Awaiting input: ')
    if question.isdigit():
        question = bot_list[int(question) - 1]
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
                    counter = 1
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
                        question = int(question) - 1
                        question = part_list[question]
                        if question in selected_bot['parts']:
                            print('Part is already in the bot.')
                            return
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
                    elif question.lower == 'quit':
                        installing = False
                    else:
                        print('part not found.')
                else:
                    installing = False
        else:
            print('Exiting')
    # End Of installing parts

# - - - - - - - - - - - - - - - - - - - - -#-BOT PARTS! -#- - - - - - - - - - - - - - - - - - - - - #
def apply_part(new_part, this_bot):
    if new_part == 'Fencing Sword':
        this_bot['parts']['Fencing Sword'] = {
            'name' : 'Fencing Sword',
            'description' : 'T1 Attack',
            'type' : 'attack',
            'damage' : 75
        }
        print('Success!')
    elif new_part == 'Spinning Blade':
        this_bot['parts']['Spinning Blade'] = {
            'name' : 'Spinning Blade',
            'description' : 'T2 Attack',
            'type' : 'attack',
            'damage' : 100
        }
        print('Success!')
    elif new_part == 'Red Laser':
        this_bot['parts']['Red Laser'] = {
            'name' : 'Red Laser',
            'description' : 'T3 Attack',
            'type' : 'attack',
            'damage' : 150
        }
        print('Success!')
    

    elif new_part == 'Repair Nanites':
        this_bot['parts']['Repair Nanites'] = {
            'name' : 'Repair Nanites',
            'description' : 'T1 Heal',
            'type' : 'heal',
            'healing' : 100
        }
        print('Success!')
    elif new_part == 'System Analysis':
        this_bot['parts']['System Analysis'] = {
        'name' : 'System Analysis',
        'description' : 'T2 Heal',
        'type' : 'heal',
        'healing' : 150
    }
        print('Success!')
    elif new_part == 'Reboot':
        this_bot['parts']['Reboot'] = {
        'name' : 'Reboot',
        'description' : 'T3 Heal',
        'type' : 'heal',
        'healing' : 200
    }
        print('Success!')


    elif new_part == 'Raise Shield':
        this_bot['parts']['Raise Shield'] = {
            'name' : 'Raise Shield',
            'description' : 'T1 Block',
            'type' : 'block',
            'guard' : 25
        }
        print('Success!')
    elif new_part == 'Energy Shields':
        this_bot['parts']['Energy Shields'] = {
            'name' : 'Energy Shields',
            'description' : 'T2 Block',
            'type' : 'block',
            'guard' : 50
        }
        print('Success!')


    elif new_part == 'Guard':
        this_bot['parts']['Guard'] = {
            'name' : 'Guard',
            'description' : 'Taunt Foes',
            'type' : 'Special',
        }
        print('Success!')
    elif new_part == 'Repair Nanite Swarm':
        this_bot['parts']['Repair Nanite Swarm'] = {
            'name' : 'Repair Nanite Swarm',
            'description' : 'Group Heal',
            'type' : 'Special',
        }
        print('Success!')
    # end of Apply Part
def random_utility():
    '''Generates a random utility part from list'''
    utilities = [
        'Repair Nanites', 'Raise Shield', 'Reboot', 'Energy Shields', 'System Analysis', 'Guard', 'Repair Nanite Swarm'
    ]
    rand = random.randint(1, 23)
    if rand < 5:
        rand = utilities[0]
    elif rand < 10:
        rand = utilities[1]
    elif rand < 14:
        rand = utilities[2]
    elif rand < 18:
        rand = utilities[3]
    elif rand < 21:
        rand = utilities[4]
    elif rand < 23:
        rand = utilities[5]
    else:
        rand = utilities[6]
    print(f'You got a: {rand}')
    return rand
    # End of random utility
def random_weapon():
    '''Generates a random weapon part from list'''
    weapons = [
        'Fencing Sword', 'Spinning Blade', 'Red Laser'
    ]
    rand = random.randint(1, 10)
    if rand < 5:
        rand = weapons[0]
    elif rand < 9:
        rand = weapons[1]
    else:
        rand = weapons[2]
    print(f'You got a: {rand}')
    return rand
    # End of random Weapon
def random_champion():
    '''Generates a random champion part from list'''
    rand = random.randint(1, 10)
    print(f'You got a: {rand}')
    return rand
    # End of random champion

# End of part listings
def next_event():
    global game_time
    events = ['Build bot', 'Scavange for resources', 'Wait']
    if 20 < game_time['hour'] or game_time['hour'] < 4:
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
        scavenge()
    elif question == 'Install bot parts':
        install_part()
    elif question == 'Wait':
        print('Time passes by')
    elif question == 'Sleep':
        print('You lay your head down, time flies by...')
        while game_time['hour'] != 9:
            get_time()
            game_time['sleep'] += 3
        else:
            game_time['hour'] -=1
            game_time['sleep'] += 1
def scavenge():
    while True:
        print('You scavenge for resources and get: \n 1: scrap \n 2: random Champion part \n 3: random Utility part \n 4: random Weapon part \n')
        question = input('Awaiting input: ')
        if question == '1':
            gain_scrap(500)
            break
        elif question == '2':
            champion_parts.append(random_champion())
            break
        elif question == '3':
            utility_parts.append(random_utility())
            break
        elif question == '4':
            weapon_parts.append(random_weapon())
            break
        else:
            print('Invalid input, material 1, 2 or 3.')
def list_bots():
    global player_bots
    names = []
    for bot in player_bots:
        names.append(bot)
    return names


# - - - - - - - - - - - - - - - - - - - - -#- COMBAT -#- - - - - - - - - - - - - - - - - - - - - #
def summon_evil_bots():
    agro_bots['Test Dummy'] = {
        'name' : 'Test Dummy',
        'max_hp' : 100,
        'hp' : 100,
        'armor' : 25,
        'power' : 100,
        'energy' : 100,
        'specialty' : 'Striker',
        'parts' : {
            'Spinning Blade': {
                'name' : 'Spinning Blade',
                'description' : 'T2 Attack',
                'type' : 'attack',
                'damage' : 100
            }
        }
    }
def combat_cycle():
    # Ensure player has bots
    global main_loop
    if player_bots:
        fighting = True
        summon_evil_bots()
    else:
        fighting = False
        main_loop = False

    # Battle Condition Check
    while fighting:
        player_turn()
        print()
        print()
        if not agro_bots:
            print('You won the fight!')
            scavenge()
            fighting = False
        elif not player_bots:
            fighting = False
            main_loop = False
    # End of combat cycle
        
def player_turn():
    print('It is your turn.')
    for character in player_bots:
        for foe in agro_bots:
            foelist = []
            list_item = f"{foe} : {agro_bots[foe]['hp']}"
            foelist.append(list_item)
        else:
            print()
            print('Aggressive bots:')
            print(foelist)
            print()
        print(f"It is {character}'s turn.")
        if 'guard' in player_bots[character]:
            del player_bots[character]['guard']
            print(f'{character} lowers their guard.')
        if player_bots[character]['parts']:
            counter = 0
            parts = []
            for option in player_bots[character]['parts']:
                counter += 1
                parts.append(option)
                print(f"{counter} : {option}")
            else:
                print('What do you do?')
                question_error_handle = True
                while question_error_handle:
                    question = input('Awaiting input: ')
                    if question.isdigit():
                        question = int(question) - 1
                        if -1 < question < counter:
                            question = parts[question]
                            question_error_handle = False
                        else:
                            print('Please enter a valid number.')
                    else:
                        print('Please enter a number.')
                # End of error handle
                part_use(player_bots, agro_bots, character, question)
                print()
    else:
        print(f'{character}, has no parts to fight with!')
# End of players turn functions

def agro_bots_turn():
    for character in agro_bots:
        print(f"It is {character}'s turn.")
        if 'guard' in agro_bots[character]:
            del agro_bots[character]['guard']
            print(f'{character} lowers their guard.')
        parts = []
        for option in agro_bots[character]['parts']:
            parts.append(option)

        agro_action = random.randint(0, len(parts))
        agro_action = parts[agro_action]
        part_use(agro_bots, player_bots, character, agro_action)
    # End of agrobot turn
        
        # ------------ PART USE ------------
def part_use(myteam, yourteam, user, part):
    print()
    targeting = True
    part_stats = myteam[user]['parts'][part]
    if part_stats['type'] == 'attack':
        damage = part_stats['damage']
        damage = damage * myteam[user]['power'] / 100 
        print('Pick a target for the attack.')
        counter = 0
        bot_list = []
        for bot in yourteam:
            counter += 1
            bot_list.append(bot)
            print(f"{counter} : {bot}")
        while targeting:
            question = input('Awaiting input: ')
            if question.isdigit():
                question = int(question) - 1
                if -1 < question < counter:
                    target = bot_list[question]
                    targeting = False
                else:
                    print('Please enter a valid number.')
            else:
                print('Please enter a number.')
            # End of targeting
        damage -= yourteam[target]['armor']
        if 'guard' in yourteam[target]:
            damage -= yourteam[target]['guard']
        
        yourteam[target]['hp'] -= damage
        print(f'{user} attacks {target} for {damage:.1f} damage.')
        check_life(yourteam, target)

    elif part_stats['type'] == 'heal':
        heal = part_stats['healing']
        heal = heal * myteam[user]['power'] / 100 

        print('Pick a target for the healing.')
        counter = 1
        bot_list = []
        for bot in myteam:
            bot_list.append(bot)
            print(f"{counter} : {bot}")
            counter += 1
        while targeting:
            question = input('Awaiting input: ')
            if question.isdigit():
                target = bot_list[int(question) - 1]
            # End of targeting
        myteam[target]['hp'] += {heal}
        if myteam[target]['hp'] > myteam[target]['max_hp']:
            myteam[target]['hp'] = myteam[target]['max_hp']
        print(f'{user} heals {target} for {heal:.1f} health.')
        # End of healing

    elif part_stats['type'] == 'block':
        guard = part_stats['guard']
        myteam[user]['guard'] = guard
        print(f'{user} braces for {guard:.1f} additional damage.')

    elif part_stats['type'] == 'special':
        print('This special part has no coded use yet! (sorry)')
    print()
# End of part Use

def check_life(team, character):
    if team[character]['hp'] < 1:
        print(f'{character} has been destroyed!')
        del team[character]

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
    'Test Dummy' : {
        'name' : 'Test Dummy',
        'max_hp' : 100,
        'hp' : 100,
        'armor' : 25,
        'power' : 100,
        'energy' : 100,
        'specialty' : 'Striker',
        'parts' : {
            'Spinning Blade': {
                'name' : 'Spinning Blade',
                'description' : 'T2 Attack',
                'type' : 'attack',
                'damage' : 100
            }
        }
    }
    }
agro_bots = {}
utility_parts = []
weapon_parts = ['Red Laser']
champion_parts = []
# Game start
player_name = input('What is your name: ')
print(f'{player_name} you are a roboticist, you have been assigned to defend the city from the next swarm of robots.')
print('You have made it 50 miles deep into enemy territory and will make your stand here, you go to bed, your elite team by your side, you are ready!')
print('You wake up to see your force destroyed, the telltale signs of a powerful emp mark the combatents, they won\'t repower in time.')
time.sleep(1)
print('You scrap the attacking robots')
gain_scrap(250)
# time.sleep(0.5)
print('\nYour old force needs to be put to use...')
scavenge()

while main_loop:
    next_event()
    print(f'Your bots: {list_bots()}')
    combat_cycle()