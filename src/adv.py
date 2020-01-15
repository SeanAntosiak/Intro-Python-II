from player import Player
from item import Item
from rooom import Room  # changed file name because import error on name?

# Declare all the rooms
room = {'outside':  Room("Outside Cave Entrance",
                         "North of you, the cave mount beckons",
                         'outside'),

        'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", 'foyer'),

        'overlook': Room("Grand Overlook", """A steep cliff appears before you,
falling into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", 'overlook'),

        'narrow':   Room("Narrow Passage", """The narrow passage bends here
from west to north. The smell of gold permeates the air.""", 'narrow'),

        'treasure': Room("Treasure Chamber", """You've found the long-lost
treasure chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", 'treasure'),
        }


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# creates items to be used in the game
coin = Item('coin', 'money')
rock = Item('rock', 'useless item')
plant = Item('plant', 'more useless than the rock')

# Makes a new player object that is currently in the 'outside' room.
guy = Player('guy', 'outside', [coin, rock, plant])

# starts a loop to run the game
gaming = True
while gaming is True:

    # takes a users input for the action to take
    action = input('Input an action or type "help": ')

    # creates a list from each word in action to use when dealing with items
    item_action = action.split()

    # returns possible actions when called
    if action == 'help':
        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('enter "loc" to get current location')
        print('enter "n", "e", "s", "w" to move in the cardinal directions')
        print('enter "check" to check items in the room and inventory')
        print('enter "take [item name]" to pick up an item')
        print('enter "drop [item name]" to drop an item')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

    # gives current location when called
    elif action == 'loc':
        print('\n------------------------------------------------------------')
        print(f'You are currently at: {room[guy.room].name}\n')
        print(f'{room[guy.room].desc}')
        print('------------------------------------------------------------\n')

    # runs when the action is a dirction
    elif action in ['n', 'e', 's', 'w']:
        if action == 'n':
            if room[guy.room].n_to is not None:
                print('\nYou move north')
                guy.room = room[guy.room].n_to.key
            else:
                print('\nThere is nothing that way')
        elif action == 'e':
            if room[guy.room].e_to is not None:
                print('\nYou move east')
                guy.room = room[guy.room].e_to.key
            else:
                print('\nThere is nothing that way')
        elif action == 's':
            if room[guy.room].s_to is not None:
                print('\nYou move south')
                guy.room = room[guy.room].s_to.key
            else:
                print('\nThere is nothing that way')
        elif action == 'w':
            if room[guy.room].w_to is not None:
                print('\nYou move west')
                guy.room = room[guy.room].w_to.key
            else:
                print('\nThere is nothing that way')

        print(f'You are now at: {room[guy.room].name}')
        print(f'{room[guy.room].desc}\n')

    # runs when an item check is called
    elif action == 'check':
        invintory = guy.inv
        room_items = room[guy.room].list

        if invintory == []:
            print('\nYou have nothing\n')
        else:
            print('\nIn your invintory you have...')
            for i in invintory:
                print(f'{i.name}: {i.desc}')

        if room_items == []:
            print('\nThere is nothing in the room\n')
        else:
            print('\nIn the room there is...')
            for i in room_items:
                print(f'{i.name}: {i.desc}')

    # runs when the action is two words
    elif len(item_action) == 2:

        invintory_strings = []
        for i in guy.inv:
            invintory_strings.append(i.name)

        room_item_strings = []
        for i in room[guy.room].list:
            room_item_strings.append(i.name)

        item_dict = {'coin': coin,
                     'rock': rock,
                     'plant': plant}

        if item_action[0] == 'drop':
            if item_action[1] in invintory_strings:
                room[guy.room].list.append(item_dict[item_action[1]])
                guy.inv.remove(item_dict[item_action[1]])
                print(f'You dropped {item_action[1]} at: {room[guy.room].name}\n')  # noqa
            else:
                print("You don't have that to drop\n")

        if item_action[0] == 'take':
            if item_action[1] in room_item_strings:
                guy.inv.append(item_dict[item_action[1]])
                room[guy.room].list.remove(item_dict[item_action[1]])
                print(f'You got {item_action[1]} from: {room[guy.room].name}\n')
            else:
                print("You can't take something that dosent exist\n")

    # quits the game
    elif action == 'q':
        gaming = False

    # runs if there was an issue with the input
    else:
        print('Type a valid command to do something')
        print('enter "help" to learn valid commands')
