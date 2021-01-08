from math import ceil
from pathlib import Path
from classes import *
import re
import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_dict_key(a_dict, value):
    for key, val in a_dict.items():
        if value == val:
            return key
    return None


def convert_dice_to_d_format(dice):
    """
    Converts an object of the type Dice to the format 'xdy + z',
    so it can be printed
    :param dice: object of the type Dice
    :return: string: string representing the dice, for human read
    """
    string = str(dice.number) + 'd' + str(dice.max)

    return string


def convert_string_to_die(string):
    pattern = r"^(\d+)d(\d+) *(\+|-)? *(\d*)$"
    match = re.match(pattern, string, re.IGNORECASE)

    if match is not None:
        number = int(match.groups()[0])
        maximum = int(match.groups()[1])
        signal = match.groups()[2]

        if signal is not None:
            modifier = int(match.groups()[3])

            if signal == '-':
                modifier = -modifier
        else:
            modifier = 0

        return [Dice(number, maximum), modifier]
    else:
        return [None, None]


def get_typed_dice(dice, objective=None, times=1):
    typed = []

    clear_terminal()
    for _ in range(times):
        value = None
        while value is None:
            if len(typed) > 0:
                print(f'You typed so far: {typed}.\n')

            if objective:
                print(f'Roll a {convert_dice_to_d_format(dice)} to {objective}')
            else:
                print(f'Roll a {convert_dice_to_d_format(dice)}.')
            print('\nType the value rolled.')
            number = get_a_number()

            if dice.number <= number <= dice.max * dice.number:
                value = number
            else:
                print(f'A {convert_dice_to_d_format(dice)} only rolls a number '
                      f'between {dice.number} and {dice.max * dice.number}.')
                print('Press ENTER to try again...')
                input()

            clear_terminal()

        typed.append(value)

    if len(typed) == 1:
        typed = typed[0]

    return typed


def list_with_no_list_or_dict(a_list):
    """
        Transforms a list in a list which all the elements are single elements,
        without tuples, lists or dictionaries inside of it.
        :param a_list: a generic list
        :return: formatted list
    """
    end = False
    final_list = []

    if isinstance(a_list, tuple):
        a_list = list(a_list)

    while not end:
        final_list = []
        all_items = True

        if type(a_list) is dict:
            a_list = list(a_list.values())

        for element in a_list.copy():
            if isinstance(element, dict):
                for key, value in element.items():
                    # If the element is a dict, it stores only the value
                    final_list.append(value)
                all_items = False
            elif isinstance(element, list):
                for value in element:
                    final_list.append(value)
                all_items = False
            else:
                final_list.append(element)

        if all_items:
            end = True
        else:
            a_list = final_list

    return final_list


def print_name(name=None, category=None):
    """
    Prints the name of determined category centralized
    :param name: string of the printed name
    :param category: string of the category of which the name is part of
    """
    if name is not None:
        length = len(name)
        middle_word = ceil(length / 2)
        start_print = 40 - middle_word

        style = ''

        for i in range(start_print - 1):
            if i % 2 == 0:
                style += '='
            else:
                style += '-'

        printed_name = style + ' ' + name.upper() + ' ' + style[::-1]
    else:
        printed_name = '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=' \
                       '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='

    print(printed_name)

    if category is not None:
        adjust = 39 - ceil(len(category) / 2)
        print(' ' * adjust + f'({category})\n')


def select(
        options,
        quantity=1,
        prompt=None,
        show_type=None,
        return_type=None,
        single_item=False,
        clean=True,
        go_back=True,
        finish=True,
):
    """
    A better structured function that allows the user to select among some
    options. It can be used for selecting how many items it is passed in the
    argument quantity for three different kinds of storing items (list, dict,
    tuple). It verifies the user answer and allows to select if the return
    value from a dict, is its key or value. Also prints some prompt and shows
    how many items the user must choose.
    :param options: dict, tuple or list storing all the items the user will
    have to choose from.
    :param quantity: int, how many items the user must choose
    :param prompt: string, a text to the user knows what he is doing
    :param show_type: if a dict, if the code will show the key or the value to
    the user select
    :param return_type: if a dict, if the return value will be a key or value
    :param single_item: boolean, if, in case the user select only one item, the
    return will be a single item instead of a list
    :param clean: boolean, if the program can or not clean the terminal
    :param go_back: boolean, if 'GO BACK' should be in the options
    :param finish: boolean, if 'EXIT' should be in the options
    :return: list with all the selected items from the user
    """
    selections = []
    options_history = []

    if type(options) is tuple:
        copy_options = list(options)
    else:
        copy_options = options.copy()

    if go_back:
        if isinstance(copy_options, dict):
            copy_options['GO BACK'] = 'GO BACK'
        else:
            copy_options += ['GO BACK']

    if finish:
        if isinstance(copy_options, dict):
            copy_options['EXIT'] = 'EXIT'
        else:
            copy_options += ['EXIT']

    inform_quantity = False
    if quantity > 1:
        inform_quantity = True

    latest_choice = None
    while quantity != 0:
        if selections != 'EXIT' and selections != 'GO BACK':
            valid_answer = False
            choice = None

            while not valid_answer:
                if clean:
                    clear_terminal()

                if prompt:
                    print(prompt)

                if selections:
                    selections_names = []
                    for selection in selections:
                        if type(selection) is not str:
                            selections_names.append(selection.name)
                        else:
                            selections_names.append(selection)

                    print('You have chosen so far:')
                    print(selections_names)

                if inform_quantity:
                    print(f'You have {quantity} choices to do.\n')

                aliases = {}
                values = []
                item_number = 1

                if type(copy_options) is dict:
                    for option_key, option_value in copy_options.items():
                        if show_type == 'key':
                            print(f'({item_number:02d}) {option_key.title()}')
                        elif show_type == 'value':
                            print(f'({item_number:02d}) {option_value.title()}')
                        else:
                            raise TypeError('show_type must be key or value')

                        if return_type == 'key':
                            aliases[item_number] = option_key
                            values.append(option_key)
                        elif return_type == 'value':
                            aliases[item_number] = option_value
                            aliases[option_key] = option_value
                            values.append(option_value)
                        else:
                            raise TypeError('return_type must be key or value')
                        item_number += 1
                elif type(copy_options) is list:
                    for option in copy_options:
                        aliases[item_number] = option
                        values.append(option)
                        print(f'({item_number:02d}) {option.title()}')
                        item_number += 1

                choice = input('Select the chosen one: ')
                choice = choice.upper()

                if choice.isnumeric():
                    choice = int(choice)

                if choice in aliases:
                    choice = aliases[choice]
                    valid_answer = True
                elif choice in values:
                    valid_answer = True
                else:
                    print('')
                    print('Not a valid answer. Press ENTER and try again.')
                    input()

            if choice == 'GO BACK':
                if len(selections) > 0:
                    selections.remove(latest_choice)
                    quantity += 1
                    copy_options = options_history.pop()
                else:
                    selections = choice
                    quantity = 0
            elif choice == 'EXIT':
                selections = choice
                quantity = 0
            else:
                selections.append(choice)
                options_history.append(copy_options.copy())

                if type(copy_options) is list:
                    copy_options.remove(choice)
                elif type(copy_options) is dict:
                    if return_type == 'key':
                        copy_options.pop(choice)
                    elif return_type == 'value':
                        copy_options.pop(get_dict_key(copy_options, choice))

                quantity -= 1

                latest_choice = choice

    clear_terminal()
    if len(selections) == 1 and single_item is True:
        selection = selections[0]
        return selection

    return selections


def gets_answer(options_text):
    """
    Prints all the possible options to be chosen and loops until the input by
    the user is one of the them.
    :param options_text: list or dict with strings that are the users options
    :return: string with the verified answer
    """
    valid_answer = False
    answer = None

    while not valid_answer:
        answer_number = 1
        options = {}

        if isinstance(options_text, dict):
            for key, value in options_text.items():
                options[str(answer_number)] = key
                print(f'({answer_number:02d}) {value.title()}')
                answer_number += 1
            options_text = list(options_text.keys())
        elif isinstance(options_text, list):
            for option in options_text:
                options[str(answer_number)] = option
                print(f'({answer_number:02d}) {option.title()}')
                answer_number += 1

        answer = input('\nSelect one of them: ')
        answer = answer.upper()

        if answer in options:
            answer = options[answer]
            valid_answer = True
        elif answer in options_text:
            valid_answer = True
        else:
            print('\nNot a valid answer. Please try again.')

    return answer


def show_armor(armor):
    """
    Prints a formatted table of the armor, showing relevant information.
    :param armor: Object of the class Armor
    """
    print_name(armor.name, armor.armor_type)

    character_info = f'Cost: {armor.cost:04d} gp' \
                     + '                           ' \
                     + f'Weight: {armor.weight:02d} lb.'
    print(character_info)

    armor_info = f'AC: {str(armor.armor_class):16s}'

    if armor.dex_max is not False:
        armor_info += f'Max. Dex: {str(armor.dex_max):10s}'
    else:
        armor_info += ' ' * 20

    if armor.strength is not False:
        armor_info += f'Strength: {str(armor.strength):9s}'
    else:
        armor_info += ' ' * 20

    if armor.stealth_disadvantage is not False:
        armor_info += 'Stealth disadvantage'

    armor_info += '\n'

    print(armor_info)


def show_weapon(weapon):
    """
    Prints a formatted table representing the weapon.
    :param weapon: Object of the class Weapon
    """
    if weapon.simple:
        category = 'SIMPLE '
    else:
        category = 'MARTIAL '

    if weapon.melee:
        category += 'MELEE'
    else:
        category += 'RANGED'

    print_name(weapon.name, category)

    damage = 'Damage: ' + convert_dice_to_d_format(weapon.damage)
    adjust = 40 - len(damage)
    for _ in range(adjust):
        damage += ' '

    damage_type = 'Damage type: ' + weapon.damage_type.title()

    print(damage + damage_type)

    cost = f'Cost: {weapon.cost} gp'
    adjust = 40 - len(cost)
    for _ in range(adjust):
        cost += ' '

    weight = f'Weight: {weapon.weight} lb.'

    print(cost + weight)

    if weapon.properties:
        properties = 'Properties: '
        for i in weapon.properties:
            properties += i.title() + ', '
        properties = properties[:-2]

        print(properties + '\n')


def show_gear(gear):
    """
    Prints a formatted object of a adventuring gear.
    :param gear: object of the class AdventuringGear
    """
    print_name(gear.name, 'ADVENTURING GEAR')

    string = cost = units = size = weight = ''

    if gear.cost:
        cost = f'Cost: {gear.cost} gp'
    if gear.units:
        units = f'Units {gear.units}'
    if gear.size:
        size = f'Size: {gear.size}'
    if gear.weight:
        weight = f'Weight: {gear.weight}'

    adjust = 20 - len(cost)
    for _ in range(adjust):
        cost += ' '
    string += cost

    adjust = 20 - len(units)
    for _ in range(adjust):
        units += ' '
    string += units

    adjust = 20 - len(size)
    for _ in range(adjust):
        size += ' '
    string += size

    adjust = 20 - len(weight)
    for _ in range(adjust):
        weight += ' '
    string += weight

    print(string + '\n')


def create_simple_list(a_list):
    """
    Transforms a list in a list which all the elements are single elements,
    without tuples, lists or dictionaries inside of it.
    :param a_list: a generic list
    :return: formatted list
    """
    end = False

    if isinstance(a_list, tuple):
        a_list = list(a_list)

    if isinstance(a_list, dict):
        a_list = list(a_list.values())

    while not end:
        other_list = []
        all_items = True

        for element in a_list:
            if isinstance(element, dict):
                for key, value in element.items():
                    # If the element is a dict, it stores only the value
                    other_list.append(value)
                all_items = False
            elif isinstance(element, list):
                for value in element:
                    other_list.append(value)
                all_items = False
            elif isinstance(element, tuple):
                for value in element:
                    other_list.append(value)
                all_items = False
            else:
                other_list.append(element)

        if all_items:
            end = True
        else:
            a_list = other_list

    return a_list


def tuple_inside_list(a_list):
    """
    Loop inside a list to see if the type of any element inside it, is a tuple
    :param a_list: a generic list
    :return: number of tuples inside of the list
    """
    tuples = 0
    for item in a_list:
        if isinstance(item, tuple):
            tuples += 1

    return tuples


def dict_of_dicts(dictionary):
    """
    Loop inside a dictionary to see if there is a dictionary inside of it.
    :param dictionary: a generic dictionary
    :return: boolean, if there is or there isn't a dictionary inside.
    """
    inception = True

    for key, value in dictionary.items():
        if not isinstance(value, dict):
            inception = False

    return inception


def search_item_dict(string, dictionary):
    """
    Loops inside a dictionary to see if there is the string inside it.
    :param string: the searched string inside of the dictionary
    :param dictionary: a generic dictionary where the search will happen
    :return: boolean: if the string is or not present in the dictionary
    """
    found = False

    for name, item in dictionary.items():
        if not found:
            if isinstance(item, dict):
                found = search_item_dict(string, item)
            else:
                if name == string:
                    found = True

    return found


def find_in_dict(string, a_dict):
    string_value = None
    for key, value in a_dict.items():
        if string == key:
            string_value = value
        else:
            if isinstance(value, dict):
                if not string_value:
                    string_value = find_in_dict(string, value)

    return string_value


def get_children(sheets_folder):
    """
    Get all the children inside of the given path
    :param sheets_folder: path for the sheets folder
    :return: list with all the paths for the children in the folder
    """
    children = []
    for child in sheets_folder.iterdir():
        children.append(child)

    return children


def get_a_number(prompt=None, go_back_message=None):
    end = False
    while not end:
        if prompt:
            clear_terminal()
            print(prompt)

            if go_back_message is None:
                go_back_message = True
                print('If you want to go back, just type anything that\'s '
                      'not a number.')

        number = input()

        if number.isnumeric():
            clear_terminal()
            number = int(number)

            return number
        else:
            pattern = r'(\d+)(\.|,)(\d+)'
            match = re.match(pattern, number)

            if match:
                groups = match.groups()
                number = groups[0] + '.' + groups[2]
                number = float(number)

                return number
            else:
                print('Not a valid number.')

                end = False
                if go_back_message:
                    end = True
                    print('Press ENTER to go back.')

                input()
                clear_terminal()

                if end:
                    return None


def set_string_size(string, size):
    new_string = string[:size]

    for _ in range(len(new_string), size):
        new_string += ' '

    return new_string


def get_parent():
    return Path(__file__).absolute().parent
