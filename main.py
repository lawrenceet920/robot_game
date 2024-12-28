# Ethan Lawrence
# Robot game
# Dec 13 2024
import time
import random
"""Plan:
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

chasis_dict = {
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
def select_chasis():
    global chasis_dict
    print('Select a "Chasis", this will determine base defencive stats.')
    for option in chasis_dict:
        player_select = chasis_dict[option]
        cost = player_select['cost']
        material = player_select['material']
        print(f'{option} : {material} : {cost} Scrap')
    while True:
        question = input('Awaiting input: ')
        if question in chasis_dict:
            chasis = {
                'material' : chasis_dict[question]['material'],
                'cost' : chasis_dict[question]['cost'],
                'armor' : chasis_dict[question]['armor'],
                'health' : chasis_dict[question]['health']
            }
            return chasis
        else:
            print('Enter a number.')
    # End of select chasis

bot_core_dict = {
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
def select_core():
    global bot_core_dict
    print('Select a "Core", this will determine avalible energy.')
    for option in bot_core_dict:
        player_select = bot_core_dict[option]
        cost = player_select['cost']
        material = player_select['material']
        print(f'{option} : {material} : {cost} Scrap')
    while True:
        question = input('Awaiting input: ')
        if question in bot_core_dict:
            core = {
                'material' : bot_core_dict[question]['material'],
                'cost' : bot_core_dict[question]['cost'],
                'energy' : bot_core_dict[question]['energy']
            }
            return core
        else:
            print('Enter a number.')
    # End of select core

engine_dict = {
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
def select_engine():
    global engine_dict
    print('Select a "Engine", this will determine attack and support stats.')
    for option in engine_dict:
        player_select = engine_dict[option]
        cost = player_select['cost']
        material = player_select['material']
        print(f'{option} : {material} : {cost} Scrap')
    while True:
        question = input('Awaiting input: ')
        if question in engine_dict:
            engine = {
                'material' : engine_dict[question]['material'],
                'cost' : engine_dict[question]['cost'],
                'power' : engine_dict[question]['power'],
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
    print(new_part)

    if new_part == 'Fencing Sword':
        this_bot['parts']['Fencing Sword'] = {
            'name' : 'Fencing Sword',
            'description' : 'T1 Attack',
            'type' : 'attack',
            'damage' : 75
        }
    elif new_part == 'Spinning Blade':
        this_bot['parts']['Spinning Blade'] = {
            'name' : 'Spinning Blade',
            'description' : 'T2 Attack',
            'type' : 'attack',
            'damage' : 100
        }
    elif new_part == 'Red Laser':
        this_bot['parts']['Red Laser'] = {
            'name' : 'Red Laser',
            'description' : 'T3 Attack',
            'type' : 'attack',
            'damage' : 150
        }
    

    elif new_part == 'Repair Nanites':
        this_bot['parts']['Repair Nanites'] = {
            'name' : 'Repair Nanites',
            'description' : 'T1 Heal',
            'type' : 'heal',
            'healing' : 100
        }
    elif new_part == 'System Analysis':
        this_bot['parts']['System Analysis'] = {
        'name' : 'System Analysis',
        'description' : 'T2 Heal',
        'type' : 'heal',
        'healing' : 150
    }
    elif new_part == 'Reboot':
        this_bot['parts']['Reboot'] = {
        'name' : 'Reboot',
        'description' : 'T3 Heal',
        'type' : 'heal',
        'healing' : 200
    }


    elif new_part == 'Raise Shield':
        this_bot['parts']['Raise Shield'] = {
            'name' : 'Raise Shield',
            'description' : 'T1 Block',
            'type' : 'block',
            'guard' : 25
        }
    elif new_part == 'Energy Shields':
        this_bot['parts']['Energy Shields'] = {
            'name' : 'Energy Shields',
            'description' : 'T2 Block',
            'type' : 'block',
            'guard' : 50
        }


    elif new_part == 'Guard':
        this_bot['parts']['Guard'] = {
            'name' : 'Guard',
            'description' : 'Taunt Foes',
            'type' : 'Special',
        }
    elif new_part == 'Repair Nanite Swarm':
        this_bot['parts']['Repair Nanite Swarm'] = {
            'name' : 'Repair Nanite Swarm',
            'description' : 'Group Heal',
            'type' : 'Special',
        }
    
    elif new_part == 'Overclock':
        this_bot['parts']['Overdrive'] = {
            'name' : 'Overdrive',
            'description' : 'buff friendly bot stats',
            'type' : 'Special',
        }
    elif new_part == 'Crusher':
        this_bot['parts']['Crusher'] = {
            'name' : 'Crusher',
            'description' : 'Sacrifice friendly bot, deal damage equal to scrap value of sacrificed bot',
            'type' : 'Special',
        }

    else:
        print(f'Error in function: apply_part, {new_part}part not in elif list ~406 - ~483')
    # print only when player using
    print('Success')
    # end of Apply Part
def random_utility(team):
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
    
    if team == 'player':
        print(f'You got a: {rand}')
    return rand
    # End of random utility
def random_weapon(team):
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

    if team == 'player':
        print(f'You got a: {rand}')
    return rand
    # End of random Weapon
def random_champion(team):
    '''Generates a random Champion part from list'''
    utilities = [
        'Crusher', 'Overclock'
    ]
    rand = random.randint(1, 2)
    if rand < 2:
        rand = utilities[0]
    elif rand < 3:
        rand = utilities[1]
    
    if team == 'player':
        print(f'You got a: {rand}')
    return rand
    # End of random champion

# End of part listings
# ----- EVENT TRACKER ----- #
def next_event():
    global game_time
    # Defualt event list (Always available)
    events = ['wait', 'Build bot']
    # Conditional events
    if 20 < game_time['hour'] or game_time['hour'] < 4: 
        events.append('Sleep')
    if len(player_bots) >= 1:
        events.append('Install bot parts')
    if random.randint(1,4) == 1:
        events.append('Scavange for resources')
    else:
        print('You decide that you need more supplies.')
        start_fight_quotes = [
            'You spot a group of corrupt, you move in.',
            'A group of scouts are on the way, you ambush them!',
            'A momentary standoff starts as you run into a group of corrupt, you don\'t let them go first.',
            'You hear a loud sound approch, you hide, after it passes you set your eyes on a squadren that fell behind.',
            'A new group of corrupt stop juuust outside of camp, you move in.',
            'You take a breath, these couldv\'e been anorher swarm, but you are here now.',
            'You approch distracted, one of the bots have an fresh apple in a storage compartment, "that one goes first", you decide.'
        ]
        print(start_fight_quotes[random.randint(0, len(start_fight_quotes) - 1)])
        events.append('Fight')

    get_time()
    print('\nWhat do you do now?')
    counter = 0
    for event in events: # Log all event options and number them
        counter += 1
        print(f'{counter} : {event}') 
    while True: # Find event
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
        scavenge_quotes = [
            'You spot a pile of rubble, score!',
            'Somehow you missed a group of corrupt arrive, lucky you however, they are powered down!',
            'You check on your water filter by the river and harvest out all the usable material',
            'You empty out your trash and sort and seperate all the recycleables.',
            'You follow the river upstream and find a pile of material collected at it\'s side.',
            'You return to a fight from a few days ago, some stuff has been untouched'
        ]
        print(scavenge_quotes[random.randint(0, len(scavenge_quotes) - 1)])
        scavenge()
    elif question == 'Install bot parts':
        install_part()
    elif question == 'Wait':
        print('Time passes by')
    elif question == 'Fight':
        combat_cycle()
    elif question == 'Sleep':
        print('You lay your head down.')
        resting_quotes = [
            'A cold breeze takes out your fire, you shiver to keep warm.',
            'An animal passes your tent, you don\'t know if you should feel worried or better protected.',
            'It begins to rain, you are grateful your tent can\'t be corrupted.',
            'heavy fog rolls in, you are cold, but safe.',
            'You think about the city, you have to do this.',
            'The crackling of your fire gives you nightmares, it was never your fault.',
            'You miss your city, at least if you fail you can\'t fail them again, right?',
            'You hope your measly piles of scrap will somehow beat the swarm.',
            'Nothing disturbs you'
        ]
        print(resting_quotes[random.randint(0, len(resting_quotes) - 1)])
        print('Time flies by...')
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
            champion_parts.append(random_champion('player'))
            break
        elif question == '3':
            utility_parts.append(random_utility('player'))
            break
        elif question == '4':
            weapon_parts.append(random_weapon('player'))
            break
        else:
            print('Invalid input, material 1, 2, 3 or 4.')
def list_bots():
    global player_bots
    names = []
    for bot in player_bots:
        names.append(bot)
    return names


# - - - - - - - - - - - - - - - - - - - - -#- COMBAT -#- - - - - - - - - - - - - - - - - - - - - #
'''    complete Bot example
    ## - Bots cannot have same name while they are acitively in agrobots (Because it is a dictonary)
    agro_bots['Blade Bot'] = {
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
'''
# - - - - - build - - - - - #
def summon_evil_bots():
    global game_time
    global agro_bots
    challenge_rating = game_time['day'] * 50 # Day > Hour
    challenge_rating += game_time['hour']
    challenge_rating += 49 # game starts at CR 100 (Unmodified)
    agro_count = random.randint(1, 4)
    if agro_count == 4:
        agro_count = 5
        challenge_rating /= 5
        if challenge_rating < 50:
            challenge_rating = 50
    while agro_count != 0:
        summon_this_agro_bot(challenge_rating)
        agro_count -= 1

def summon_this_agro_bot(bot_cr):
    global chasis_dict
    global bot_core_dict
    global engine_dict

    agro_bot_name_list = [
        'Jim-bot', 'Mr bot', 'Super Robot', '2D-2R', 'Toaster 2 (The sequel to Toaster)'
    ]
    while True: # Ensure unique bot name
        name = agro_bot_name_list[random.randint(0, len(agro_bot_name_list) - 1)]
        if not name in agro_bots:
            agro_bots[name] = {'name' : name, 'parts' : {}}
            break

    # - - Chasis
    counter = 0
    for option in chasis_dict:
        if chasis_dict[option]['cost'] < bot_cr:
            counter += 1
        else:
            break
    if counter <= 1:
        rand = '1'
    else:
        rand = str(random.randint(1, counter))

    bot_cr -= chasis_dict[rand]['cost']
    agro_bots[name]['hp'] = chasis_dict[rand]['health']
    agro_bots[name]['max_hp'] = chasis_dict[rand]['health']
    agro_bots[name]['armor'] = chasis_dict[rand]['armor']
    bot_cr += 5 # Ensure bot has at least enough CR to build full bot

    # - - Engine
    counter = 0
    for option in engine_dict:
        if engine_dict[option]['cost'] < bot_cr:
            counter += 1
        else:
            break
    if counter <= 1:
        rand = '1'
    else:
        rand = str(random.randint(1, counter))
        
    bot_cr -= engine_dict[rand]['cost']
    agro_bots[name]['power'] = engine_dict[rand]['power']
    bot_cr += 5 # Ensure bot has at least enough CR to build full bot

    # - - Core
    counter = 0
    for option in bot_core_dict:
        if bot_core_dict[option]['cost'] < bot_cr:
            counter += 1
        else:
            break
    if counter <= 1:
        rand = '1'
    else:
        rand = str(random.randint(1, counter))
        
    bot_cr -= bot_core_dict[rand]['cost']
    agro_bots[name]['energy'] = bot_core_dict[rand]['energy']
    bot_cr += 5 # Ensure bot has at least enough CR to build full bot

    # - - Specialty
    specialties = { # Swarm and Support removed because they make the bots more RNG dependent as both as agro bots only add parts
    0 : 'Striker', # Higher damage
    1 : 'Defender', # Better armor and health
    2 : 'Champion', # Allows champion parts to be equiped
    }
    agro_bots[name]['specialty'] = specialties[random.randint(0,2)]
    
    if agro_bots[name]['specialty'] == 'Striker':
        agro_bots[name]['power'] = agro_bots[name]['power'] * 1.5
    elif agro_bots[name]['specialty'] == 'Defender':
        agro_bots[name]['max_hp'] = agro_bots[name]['max_hp'] * 2
        agro_bots[name]['hp'] = agro_bots[name]['hp'] * 2
        agro_bots[name]['armor'] = agro_bots[name]['armor'] + 10

    # - - parts
    if agro_bots[name]['specialty'] == 'Champion': # If bot is champ give it another part
        bot_cr += 100
    apply_part(get_agro_parts(name), agro_bots[name]) # This part is here to ensure the bot can act
    while bot_cr > 99 and len(agro_bots[name]['parts']) < 5:
        apply_part(get_agro_parts(name), agro_bots[name])
        bot_cr -= 100


# - - - - - Battle - - - - - #
def get_agro_parts(name):
    if agro_bots[name]['specialty'] == 'Champion':
        reciver_is_champ = 6
    else:
        reciver_is_champ = 3
    while True:
        bot_part = random.randint(1, reciver_is_champ)
        if int(bot_part) == 1:
            bot_part = random_utility('agro')
        elif int(bot_part) <= 3:
            bot_part = random_weapon('agro')
        elif int(bot_part) > 3:
            bot_part = random_champion('agro')

        if not bot_part in agro_bots[name]['parts']:
            break
    return bot_part

def combat_cycle():
    global taunt_list
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    taunt_list = {}
    print('Combat has started')
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
        agro_bots_turn()
        print()
        if not agro_bots:
            print('You won the fight!')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            scavenge()
            fighting = False
        elif not player_bots:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            fighting = False
            main_loop = False
    # End of combat cycle
        
def player_turn():
    print('It is your turn.')
    for character in player_bots:
        foelist = []
        for foe in agro_bots:
            list_item = f"{foe} : {agro_bots[foe]['hp']}hp"
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

        if len(parts) == 1:
            agro_action = 0
        else:
            agro_action = random.randint(0, len(parts) - 1)
        agro_action = parts[agro_action]
        part_use(agro_bots, player_bots, character, agro_action)
    # End of agrobot turn
        
        # ------------ PART USE ------------

def part_use(myteam, yourteam, user, part):
    global taunt_list
    print()
    part_stats = myteam[user]['parts'][part]
    if part_stats['type'] == 'attack':
        damage = part_stats['damage']
        damage = damage * myteam[user]['power'] / 100 
        targeting_ability(myteam, yourteam, False)
        damage -= yourteam[target]['armor']
        if 'guard' in yourteam[target]:
            damage -= yourteam[target]['guard']
        
        yourteam[target]['hp'] -= damage
        print(f'{user} attacks {target} for {damage:.1f} damage.')
        check_life(yourteam, target)

    elif part_stats['type'] == 'heal':
        heal = part_stats['healing']
        heal = heal * myteam[user]['power'] / 100 
        target = targeting_ability(myteam, yourteam, True)
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
        if part_stats['name'] == 'Guard':
            taunt_list[myteam[user]['name']]
        else:
            print('This special part has no coded use yet! (sorry)')
    print()
# End of part Use

def check_life(team, character):
    if team[character]['hp'] < 1:
        print(f'{character} has been destroyed!')
        if team[character]['name'] in taunt_list:
            del taunt_list[team[character]['name']]
        del team[character]

# Part specific functions
def targeting_ability(myteam, yourteam, is_positive_ability):
    global taunt_list
    if is_positive_ability:
        print('Pick a target for the attack.')
        counter = 0
        bot_list = []
        for bot in myteam:
            counter += 1
            bot_list.append(bot)
            print(f"{counter} : {bot}")
        while True:
            question = input('Awaiting input: ')
            if question.isdigit():
                question = int(question) - 1
                if -1 < question < counter:
                    return bot_list[question]
                else:
                    print('Please enter a valid number.')
            else:
                print('Please enter a number.')
    else:
        taunted = False
        if taunt_list:
            for character in taunt_list:
                if character not in myteam:
                    taunted = True
        if taunted:
            print('taunted')
        else:
            print('Pick a target for the attack.')
            counter = 0
            bot_list = []
            for bot in yourteam:
                counter += 1
                bot_list.append(bot)
                print(f"{counter} : {bot}")
            while True:
                question = input('Awaiting input: ')
                if question.isdigit():
                    question = int(question) - 1
                    if -1 < question < counter:
                        return bot_list[question]
                    else:
                        print('Please enter a valid number.')
                else:
                    print('Please enter a number.')
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
# Battle globals
taunt_list = {}
# Game start
player_name = input('What is your name: ')
'''
print(f'{player_name} you are a roboticist, you have been assigned to defend the city from the next swarm of corrupted robots.')
print('You have made it 50 miles deep into corrupted territory, You have to make your stand here, you go to sleep, your elite team by your side, you are ready!')
print('You wake up to see your force destroyed, the telltale signs of a powerful emp mark the combatents.')
print('You take a look at them, even if they repower it won\'t be in time.')
time.sleep(1)
print('You scrap the corrupted robots, you\'ll need all the materials you can get.')
gain_scrap(250)
# time.sleep(0.5)
print('\nYour old force needs to be put to use...')
scavenge()
'''

while main_loop:
    combat_cycle()
    next_event()
    print(f'Your bots: {list_bots()}')