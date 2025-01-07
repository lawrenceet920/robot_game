# Ethan Lawrence
# Robot game
# Dec 13 2024
import time
import random
"""Plan:
Fight final boss
Select special event (clone a bot, buff a bot, scrap pile, sell a bot, Theft, bot specific mission {drill part can mine})
rest encounters?
"""
RANDOM_BOT_NAME_LIST = [
    'Jim-bot', 'Mr bot', 'Super Robot', '2D-2R', 'Toaster)', 'Tickle Me Elmo', 'Prof Cogsworth', 'Alan the Wrench', 'Cyber Bot', 'Cyborg', 'Android', 'Apple', 'Ton Meta', 'Iron Golem', 'Man of Tungsten', 'Blightsteel Destroyer'
]

def gain_scrap(amount):
    global scrap
    scrap += amount
    if 0 > game_time['sleep']:
        print(f'+ scrap | you are to tired to count the new total or even collect all of it')
    else:
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
    global RANDOM_BOT_NAME_LIST
    global scrap
    global player_bots
    global player_exp
    cost = 100
    print('\n\n\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'You have {scrap} Scrap, the base cost of a bot is 100.')
    print('Your bot will also need a: Chasis, Core, and Engine.')
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
        name = input('Name your bot, or type "r" to use a random name:    ')
        if name == 'r':
            while True: # Generate random (Unused)name 
                name = RANDOM_BOT_NAME_LIST[random.randint(0, len(RANDOM_BOT_NAME_LIST) - 1)]
                if name not in player_bots:
                    print(f'name chosen: {name}')
                    break
            break
        elif name not in player_bots:
            break
        else:
            print('Please use a unique name.')
    print()
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
    if specialty == 'Swarmer':
        cost -= cost / 2
    elif specialty == 'Striker':
        bot_loadout['power'] = bot_loadout['power'] * 1.5
    elif specialty == 'Defender':
        bot_loadout['max_hp'] = bot_loadout['max_hp'] * 2
        bot_loadout['hp'] = bot_loadout['hp'] * 2
        bot_loadout['armor'] = bot_loadout['armor'] + 50
    bot_loadout['scrap value'] = cost

    print(f"This robot specialises in {specialty} and is will use these parts")
    print(f"Chasis : {chasis['material']} | Core : {core['material']} | Engine : {engine['material']}")

    print(f'This bot will cost {cost} scrap to construct.')
    if scrap >= cost:
        print('Type y to build the robot.')
        question = input('Awaiting input: ')
        if question in ['y', 'Y', 'Yes', 'yes']:
            player_bots[name] = bot_loadout
            scrap -= cost
            if player_exp != '3':
                print('---------------\nYou have finished building this bot, make sure to install parts to give them functionality\n---------------')
                time.sleep(1)
            else:
                print('Bot construction finished.')
    else: 
        print('You do not have enough scrap to build this.')
        time.sleep(1)
    print('Exiting build mode.')
    time.sleep(2)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n\n\n')
    # End of build bot
# Selecting bot parts

chasis_dict = {
    '1' : {
        'material' : 'Wooden',
        'cost' : 50,
        'armor' : 0,
        'health' : 300
    },
    '2' : {
        'material' : 'Stone',
        'cost' : 75,
        'armor' : 50,
        'health' : 300
    },
    '3' : {
        'material' : 'Scrap Iron',
        'cost' : 150,
        'armor' : 100,
        'health' : 500
    },
    '4' : {
        'material' : 'Glass',
        'cost' : 150,
        'armor' : 300,
        'health' : 1
    },
    '5' : {
        'material' : 'Iron',
        'cost' : 250,
        'armor' : 150,
        'health' : 750
    },
    '6' : {
        'material' : 'Steel',
        'cost' : 500,
        'armor' : 250,
        'health' : 2500
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
        'material' : 'Hydrogen',
        'cost' : 200,
        'energy' : 500
    },
    '5' : {
        'material' : 'Nuclear',
        'cost' : 500,
        'energy' : 10000
    }
    }
def select_core():
    global bot_core_dict
    print('Select a "Core", this will determine avalible energy (Parts passively use energy).')
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
        'power' : 70
    },
    '3' : {
        'material' : 'Racecar',
        'cost' : 100,
        'power' : 100
    },
    '4' : {
        'material' : 'Truck',
        'cost' : 250,
        'power' : 150
    },
    '5' : {
        'material' : 'Jet',
        'cost' : 750,
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
    global ALL_PARTS
    while True:
        pick_bot = True
        while pick_bot:
            print("Pick a robot, or type 'quit' to quit")
            counter = 1
            bot_list = []
            for bot in player_bots:
                bot_list.append(bot)
                print(f"{counter} : {bot}")
                counter += 1
            question = input('Awaiting input: ')
            if question.isdigit():
                question = int(question) - 1
                if -1 < question < len(bot_list):
                    question = bot_list[question]
                else:
                    print('number not in range \n')
            elif question.lower() in 'quit':
                return
            
            if question in player_bots:
                print('\n\n\n')
                selected_bot = question # Bot found
                specialty = player_bots[selected_bot]['specialty'] # Specialty found
                if specialty == 'Support': # Support?
                    allowed_parts = 6
                else: 
                    allowed_parts = 4
                if specialty == 'Champion': # Champion?
                    champ = True
                else:
                    champ = False
                pick_bot = False
        
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
                if not player_bots[selected_bot]['parts']:
                    print('No parts installed')
                for part in selected_bot['parts']:
                    print(part)
                print()
                while installing:
                    print('Type in the part number you want to install, or "quit" to quit.')
                    energy = player_bots[selected_bot]['energy']
                    print(f"Remaining energy: {energy}00 Watts")
                    print('Current owned parts:')
                    counter = 1
                    part_list = []
                    for unused_part in weapon_parts:
                        print(f'{counter} : {unused_part} | {ALL_PARTS[unused_part]["energy"]}00 Watts')
                        part_list.append(unused_part)
                        counter += 1
                    for unused_part in utility_parts:
                        print(f'{counter} : {unused_part} | {ALL_PARTS[unused_part]["energy"]}00 Watts')
                        part_list.append(unused_part)
                        counter += 1
                    if champ: # List parts
                        print('\nChampion Part List: ')
                        for unused_part in champion_parts:
                            print(f'{counter} : {unused_part} | {ALL_PARTS[unused_part]["energy"]}00 Watts')
                            part_list.append(unused_part)
                            counter += 1
                    # Stop listing

                    print() 
                    question = input('Awaiting input: ')
                    if question.isdigit():
                        question = int(question) - 1
                        if -1 < question < len(part_list):
                            question = part_list[question]
                            if question in selected_bot['parts']:
                                print('Part is already in the bot.')
                                return
                            print('Part found! installing...')
                            if champ:
                                for part in champion_parts:
                                    if part == question:
                                        champion_parts.remove(part)
                                        apply_part(part, selected_bot, True)
                                        installing = False
                            for part in utility_parts:
                                if part == question:
                                    utility_parts.remove(part)
                                    apply_part(part, selected_bot, True)
                                    installing = False
                            for part in weapon_parts:
                                if part == question:
                                    weapon_parts.remove(part)
                                    apply_part(part, selected_bot, True)
                                    installing = False
                        else:
                            print('Part not in range')
                    elif question.lower() == 'quit':
                        installing = False
                    else:
                        print('part not found.')
            else:
                print('Bot has maxed equipped parts (Support bots can equip more parts)')
        print('\n\n')
    # End Of installing parts

# - - - - - - - - - - - - - - - - - - - - -#-BOT PARTS! -#- - - - - - - - - - - - - - - - - - - - - #
ALL_PARTS = {
    'Fencing Sword' : {
            'name' : 'Fencing Sword',
            'description' : 'T1 Attack',
            'type' : 'attack',
            'damage' : 75,
            'energy' : 50
        },
    'Spinning Blade' : {
            'name' : 'Spinning Blade',
            'description' : 'T2 Attack',
            'type' : 'attack',
            'damage' : 100,
            'energy' : 100
        },
    'Red Laser' : {
            'name' : 'Red Laser',
            'description' : 'T3 Attack',
            'type' : 'attack',
            'damage' : 150,
            'energy' : 250
        },
    
    'Repair Nanites': {
            'name' : 'Repair Nanites',
            'description' : 'T1 Heal',
            'type' : 'heal',
            'healing' : 50,
            'energy' : 50
        },
    'System Analysis': {
        'name' : 'System Analysis',
        'description' : 'T2 Heal',
        'type' : 'heal',
        'healing' : 75,
            'energy' : 100
    },
    'Reboot': {
        'name' : 'Reboot',
        'description' : 'T3 Heal',
        'type' : 'heal',
        'healing' : 100,
            'energy' : 250
    },

    'Raise Shield':{
            'name' : 'Raise Shield',
            'description' : 'T1 Block',
            'type' : 'block',
            'guard' : 50
        },
    'Energy Shields':{
            'name' : 'Energy Shields',
            'description' : 'T2 Block',
            'type' : 'block',
            'guard' : 50,
            'energy' : 100
        },


    'Guard':{
            'name' : 'Guard',
            'description' : 'Taunt foes, until end of combat, or bot dies. While taunted, foes can only attack bots that have taunted.',
            'type' : 'Special',
            'energy' : 100
        },
    'Repair Nanite Swarm':{
            'name' : 'Repair Nanite Swarm',
            'description' : 'Heal all friendly bots',
            'type' : 'Special',
            'energy' : 250
        },
    
    'Rally':{
            'name' : 'Rally',
            'description' : 'buff friendly bot attacks for rest of comabt',
            'type' : 'Special',
            'energy' : 100
        },
    'Crusher':{
            'name' : 'Crusher',
            'description' : 'Sacrifice friendly bot, deal damage equal to scrap value of sacrificed bot',
            'type' : 'Special',
            'energy' : 0
        }
}
def apply_part(new_part, this_bot, isplayer):
    global ALL_PARTS
    if isplayer:
        if ALL_PARTS[new_part]['energy'] <= player_bots[this_bot]['energy']:
            player_bots[this_bot]['energy'] -= ALL_PARTS[new_part]['energy']
            print('Success')
            bot_name = this_bot['parts'][new_part]['name']
            bot_description = this_bot['parts'][new_part]['description']
            print('part info:')
            if this_bot['parts'][new_part]['type'] == 'Special':
                print(f'{bot_name} will {bot_description}')
            else:
                print(f'{bot_name} is a {bot_description}')
            time.sleep(1)
        else:
            print('Not enough Watts avalible in bot, consider building bots with better "cores"')
    else:
        this_bot['parts'][new_part] = ALL_PARTS[new_part]
    # end of Apply Part
def random_utility(team):
    '''Generates a random utility part from list'''
    utilities = [
        'Repair Nanites', 'Raise Shield', 'Reboot', 'Energy Shields', 'System Analysis', 'Guard', 'Repair Nanite Swarm'
    ]
    global ALL_PARTS
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
        print(f'{ALL_PARTS[rand]["description"]}')
    return rand
    # End of random utility
def random_weapon(team):
    '''Generates a random weapon part from list'''
    global ALL_PARTS
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
        print(f'{ALL_PARTS[rand]["description"]}')
    return rand
    # End of random Weapon
def random_champion(team):
    '''Generates a random Champion part from list'''
    global ALL_PARTS
    utilities = [
        'Crusher', 'Rally'
    ]
    rand = random.randint(1, 2)
    if rand < 2:
        rand = utilities[0]
    elif rand < 3:
        rand = utilities[1]
    
    if team == 'player':
        print(f'You got a: {rand}')
        print(f'{ALL_PARTS[rand]["description"]}')
    return rand
    # End of random champion

# End of part listings
#- - - - - - - - - - - - - - - - - - - - -#-EVENT TRACKER-#- - - - - - - - - - - - - - - - - - - - -#
def next_event():
    global game_time
    # Defualt event list (Always available)
    events = ['Save Game', 'Build bot']
    # Conditional events
    if 20 < game_time['hour'] or game_time['hour'] < 4: 
        if not 8 < game_time['sleep']:
            events.append('Sleep')
    elif 0 > game_time['sleep']:
        events.append('Sleep')
    if len(player_bots) >= 1:
        events.append('Install bot parts')
    for bot in player_bots:
        if player_bots[bot]['hp'] != player_bots[bot]['max_hp']:
            events.append('Repair bots')
            break
    if random.randint(1,4) == 1:
        events.append('Scavange for resources')
    else:
        events.append('Fight')
    if player_name == 'E':
        events.append('wait')

    get_time()
    if 0 > game_time['sleep']:
        print('\nWhat now do you do now? I hopes its is sleeps')
    else:
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
        print('You decide that you need more bots.')
        time.sleep(0.5)
        build_bot()
    elif question == 'Save Game':
        print('Saving...\n')
        time.sleep(1)
        save_game()
        time.sleep(5)
        print()
    elif question == 'Repair bots':
        repair_bots()
    elif question == 'Scavange for resources':
        SCAVENGE_QUOTES = [
            'You spot a pile of rubble, score!',
            'Somehow you missed a group of corrupt arrive, lucky you however, they are powered down!',
            'You check on your water filter by the river and harvest out all the usable material',
            'You empty out your trash and sort and seperate all the recycleables.',
            'You follow the river upstream and find a pile of material collected at it\'s side.',
            'You return to a fight from a few days ago, some stuff has been untouched'
        ]
        print(SCAVENGE_QUOTES[random.randint(0, len(SCAVENGE_QUOTES) - 1)])
        scavenge()
    elif question == 'Install bot parts':
        print('You prepare to install your bot parts.')
        time.sleep(0.5)
        install_part()
    elif question == 'Wait':
        print('Time passes by')
    elif question == 'Fight':
        print('You decide that you need more supplies.')
        time.sleep(0.5)
        START_FIGHT_QUOTES = [
            'You spot a group of corrupt, you move in.',
            'A group of scouts are on the way, you ambush them!',
            'A momentary standoff starts as you run into a group of corrupt, you don\'t let them go first.',
            'You hear a loud sound approch, you hide, after it passes you set your eyes on a squadren that fell behind.',
            'A new group of corrupt stop juuust outside of camp, you move in.',
            'You take a breath, these couldv\'e been anorher swarm, but you are here now.',
            'You approch distracted, one of the bots have an fresh apple in a storage compartment, "that one goes first", you decide.'
        ]
        print(START_FIGHT_QUOTES[random.randint(0, len(START_FIGHT_QUOTES) - 1)])
        time.sleep(0.75)
        combat_cycle()
    elif question == 'Sleep':
        print('You lay your head down.')
        RESTING_QUOTES = [
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
        print(RESTING_QUOTES[random.randint(0, len(RESTING_QUOTES) - 1)])
        print('Time flies by...')
        while game_time['hour'] != 9:
            get_time()
            game_time['sleep'] += 3
        else:
            game_time['hour'] -=1
            game_time['sleep'] += 1
def scavenge():
    while True:
        if 0 > game_time['sleep']:
            print('You scavenge for resources and get: \n 1: That wonky metal thingi \n 2: the one for just that one guysis \n 3: useful stuffs i would hope \n 4: The thing that does the bad things to the other things that do bad\n')
        else:
            print('You scavenge for resources and get: \n 1: scrap \n 2: random Champion part \n 3: random Utility part \n 4: random Weapon part \n')
        question = input('Awaiting input: ')
        if question == '1':
            if 0 > game_time['sleep']:
                gain_scrap(250)
            else:
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
        names.append(player_bots[bot]['name'])
    return names

def save_game():
    global game_time
    global player_bots
    global scrap
    global utility_parts
    global champion_parts
    global weapon_parts

    print(f'game_time = {game_time}')
    print(f'player_bots = {player_bots}')
    print(f'scrap = {scrap}')
    print(f'utility_parts = {utility_parts}')
    print(f'champion_parts = {champion_parts}')
    print(f'weapon_parts = {weapon_parts}')

def repair_bots():
    global scrap
    cost = 0
    for bot in player_bots:
        cost += player_bots[bot]['max_hp'] - player_bots[bot]['hp']
    print(f'To repair your bots you will need {cost} scrap.')
    print('1 : Don\'t repair')
    can = False
    if cost <= scrap:
        print(f'2 : Make repairs')
        can = True
    while True:
        question = input('Awaiting input: ')
        if question.isdigit():
            question = int(question)
            if question == 1:
                break
            elif question == 2 and can:
                scrap -= cost
                for bot in player_bots:
                    player_bots[bot]['hp'] = player_bots[bot]['max_hp']
                print('Your bots have been repaired')
                break
            else:
                print('Please enter a valid number.')
        else:
            print('Please enter a number.')

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
    challenge_rating /= agro_count
    if challenge_rating < 50:
        challenge_rating = 50
    while agro_count != 0:
        summon_this_agro_bot(challenge_rating)
        agro_count -= 1

def summon_this_agro_bot(bot_cr):
    global chasis_dict
    global bot_core_dict
    global engine_dict
    global RANDOM_BOT_NAME_LIST
    while True: # Ensure unique bot name
        name = RANDOM_BOT_NAME_LIST[random.randint(0, len(RANDOM_BOT_NAME_LIST) - 1)]
        if not name in agro_bots:
            if not name in player_bots:
                agro_bots[name] = {'name' : name, 'parts' : {}}
                break
    
    agro_bots[name]['scrap value'] = 0

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

    agro_bots[name]['scrap value'] += chasis_dict[rand]['cost']
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
        
    agro_bots[name]['scrap value'] += chasis_dict[rand]['cost']
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
        
    agro_bots[name]['scrap value'] += chasis_dict[rand]['cost']
    # bot_cr -= bot_core_dict[rand]['cost']
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
        agro_bots[name]['armor'] = agro_bots[name]['armor'] + 50

    # - - parts
    if agro_bots[name]['specialty'] == 'Champion': # If bot is champ give it another part
        bot_cr += 100
    apply_part(get_agro_parts(name), agro_bots[name], False) # This part is here to ensure the bot can act
    while bot_cr > 99 and len(agro_bots[name]['parts']) < 5:
        apply_part(get_agro_parts(name), agro_bots[name], False)
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
    global damage_modifications
    global turn
    global taunt_list
    print('\n\n\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
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
        turn = True
        player_turn()
        turn = False
        print()
        agro_bots_turn()
        print()
        if not agro_bots:
            print('You won the fight!')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            time.sleep(1)
            print('\n\n\n\n\n')
            scavenge()
            fighting = False
        elif not player_bots:
            print('You ran out of bots, to fight with.')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            time.sleep(1)
            print('\n\n\n\n\n')
            fighting = False
            main_loop = False
    damage_modifications = {
    'player add' : 0,
    'player mult' : 1,
    'corrupt add' : 0,
    'corrupt mult' : 1
}
    # End of combat cycle
        
def player_turn():
    print()
    print('It is your turn.')
    print()
    time.sleep(0.5)
    for character in player_bots:
        if not agro_bots:
            return

        time.sleep(0.2)
        foelist = []
        for foe in agro_bots:
            list_item = f"{foe} : {agro_bots[foe]['hp']}hp"
            foelist.append(list_item)
        else:
            print('Aggressive bots:')
            print(foelist)
            print()
        print('===========================')
        print(f"It is {character}'s turn.")
        time.sleep(0.2)
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
                print()
                time.sleep(0.2)
                part_use(player_bots, agro_bots, character, question)
        else:
            print(f'{character}, has no parts to fight with!')
        print('===========================')
# End of players turn functions

def agro_bots_turn():
    for character in agro_bots:
        time.sleep(0.5)
        if not player_bots:
            return
        print('===========================')
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
        print('===========================')
    time.sleep(0.5)
    # End of agrobot turn
        
        # ------------ PART USE ------------

def part_use(myteam, yourteam, user, part):
    global taunt_list
    global damage_modifications
    part_stats = myteam[user]['parts'][part]
    if part_stats['type'] == 'attack':
        target = targeting_ability(myteam, yourteam, False)
        if target != False:
            damage = part_stats['damage']
            damage = damage * myteam[user]['power'] / 100 
            if myteam == player_bots:
                damage += damage_modifications['player add']
                damage *= damage_modifications['player mult']
            else:
                damage += damage_modifications['corrupt add']
                damage *= damage_modifications['player mult']
            damage -= yourteam[target]['armor']
            if 'guard' in yourteam[target]:
                damage -= yourteam[target]['guard']
            if damage <= 0:
                damage = 0
                print(f'{user} attacks {target}, but it doesn\'t do any damage')
            else:
                yourteam[target]['hp'] -= damage
                print(f'{user} attacks {target} for {damage:.1f} damage.')
                check_life(yourteam, target)

    elif part_stats['type'] == 'heal':
        heal = part_stats['healing']
        heal = heal * myteam[user]['power'] / 100 
        target = targeting_ability(myteam, yourteam, True)
        myteam[target]['hp'] += heal
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
        elif part_stats['name'] == 'Crusher':
            print('Pick bot to destroy for base damage')
            target = targeting_ability(myteam, yourteam, True)
            myteam[target]['hp'] -= myteam[target]['hp']
            print(f'{user} crushes {target}')
            damage = myteam[target]['scrap value']
            check_life(myteam, target)

            print('Pick bot to attack')
            target = targeting_ability(myteam, yourteam, False)
            yourteam[target]['hp'] -= damage
            print(f'{user} attacks {target} for {damage:.1f} damage.')
        elif part_stats['name'] == 'Rally':
            print(f'{user} rallys their allies, + 10% damage multiplier')
            if myteam == player_bots:
                damage_modifications['player mult'] += 0.1
            else:
                damage_modifications['corrupt mult'] += 0.1
        else:
            print('This special part has no coded use yet! (sorry)')
# End of part Use

def check_life(team, character):
    if team[character]['hp'] < 1:
        print(f'{character} has been destroyed!')
        if team[character]['name'] in taunt_list:
            del taunt_list[team[character]['name']]
        del team[character]

# Part specific functions
def targeting_ability(myteam, yourteam, target_my_team):
    global taunt_list
    global turn
    taunted = False 

    if target_my_team:
        if turn:
            print('Pick a target for the ability.')
        counter = 0
        bot_list = []
        for bot in myteam:
            counter += 1
            bot_list.append(bot)
            if turn:
                print(f"{counter} : {bot}")
    else:
        # Find if taunted
        if taunt_list:
            for character in taunt_list:
                if character not in myteam:
                    taunted = True

        if taunted: # TAUNTED
            if turn:
                print('Pick a target for the attack.')
            counter = 0
            bot_list = []
            for bot in yourteam:
                if bot in taunt_list:
                    counter += 1
                    bot_list.append(bot)
                    if turn:
                        print(f"{counter} : {bot}")

        else: # NOT TAUNTED
            if turn:
                print('Pick a target for the attack.')
            counter = 0
            bot_list = []
            if yourteam:
                for bot in yourteam:
                    counter += 1
                    bot_list.append(bot)
                    if turn:
                        print(f"{counter} : {bot}")
            else:
                print('However there was nothing to hit.')
                return False

    # After target options are declared
    while True:
            if turn:
                question = input('Awaiting input: ')
            else:
                question = str(random.randint(1, len(bot_list)))
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
player_bots = {}
agro_bots = {}
utility_parts = []
weapon_parts = []
champion_parts = []
# Battle globals
taunt_list = {}
damage_modifications = {
    'player add' : 0,
    'player mult' : 1,
    'corrupt add' : 0,
    'corrupt mult' : 1
}
turn = True # True is playerturn
# Game start
while True:
    print('How much have you played this game? (Enter the number to the left of the ":")')
    print('1 : Never, full tutorial')
    print('2 : Some, remove tutorials')
    print('3 : A lot, remove tutorial, and reduce wait time, and flavor text')
    player_exp = input('Awaiting input:\n')
    if player_exp == '3':
        game_speed = 2
        break
    elif player_exp in ['1', '2']:
        game_speed = 1
        break
    else:
        print('Input must be either "1" "2", or "3"\n')
player_name = input('What is your name: ')


# ----------------------------------------------Save data----------------------------------------------#
# - - Paste here - - then set load save to True - -
game_time = {'day': 1, 'hour': 15, 'sleep': 2}
player_bots = {'rick': {'name': 'rick', 'max_hp': 500, 'hp': 500, 'armor': 100, 'power': 225.0, 'energy': 50, 'specialty': 'Striker', 'parts': {'Spinning Blade': {'name': 'Spinning Blade', 'description': 'T2 Attack', 'type': 'attack', 'damage': 100}, 'Fencing Sword': {'name': 'Fencing Sword', 'description': 'T1 Attack', 'type': 'attack', 'damage': 75}}, 'scrap value': 455}, 'bob': {'name': 'bob', 'max_hp': 2500, 'hp': 2500, 'armor': 250, 'power': 20, 'energy': 50, 'specialty': 'Defender', 'parts': {'Raise Shield': {'name': 'Raise Shield', 'description': 'T1 Block', 'type': 'block', 'guard': 25}}, 'scrap value': 360}, 'morty': {'name': 'morty', 'max_hp': 500, 'hp': 500, 'armor': 100, 'power': 225.0, 'energy': 50, 'specialty': 'Striker', 'parts': {'Fencing Sword': {'name': 'Fencing Sword', 'description': 'T1 Attack', 'type': 'attack', 'damage': 75}, 'System Analysis': {'name': 'System Analysis', 'description': 'T2 Heal', 'type': 'heal', 'healing': 75}}, 'scrap value': 455}}
scrap = 600
utility_parts = []
champion_parts = ['Crusher', 'Crusher']
weapon_parts = []
load_save = True

# Introduction
if load_save:
    print()
    print('Save data located.')
    time.sleep(1)
    print('Save loaded')
    time.sleep(1)
    print()
else:
    if player_exp == '1':
        print(f'{player_name} you are a roboticist, you have been assigned to defend the city from the next swarm of corrupted robots.')
        time.sleep(2)
        print('You have made it 50 miles deep into corrupted territory, Scrap sticks out of the scorched earth and flows down the rivers, life is still here, but only faintly.')
        time.sleep(2)
        print('You have to make your stand here, you set up camp, go to sleep, your elite team by your side, you are ready!')
        time.sleep(2)
        print('You wake up to see your force destroyed, a huge force has had a large battle last night.')
        time.sleep(2)
        print('You judge that this was the main army and all that could be left of this assault are smaller groups and their commander.')
        time.sleep(2)
        print('You check local energy readings. compaired to last night you have about 10 days until the commander arrives.')
        time.sleep(2)
        print('If you can take out the commander they will be too divided and disorginised for this assault to work.')
        time.sleep(2)
        print('You scrap the corrupted robots, you\'ll need all the materials you can get.\n')
        time.sleep(2)
    gain_scrap(500)
    utility_parts.append(random_utility('player'))
    weapon_parts.append(random_weapon('player'))
    champion_parts.append(random_champion('player'))
    time.sleep(0.5)
    print('\nYour old force also needs to be put to use...')
    scavenge()
    scavenge()
    if player_exp == '1':
        print('Your bots were just wreaked, you should build a bot quickly before you get attacked so you can defend yourself.')

while main_loop:
    print(f'Your bots: {list_bots()}')
    next_event()
time.sleep(1)
print('Oh. oh no...')
time.sleep(1)
if 0 > game_time['sleep']:
    print('Nap tiimeee-.')
else:
    print('Game over!')