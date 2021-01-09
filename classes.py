from random import randint
from math import floor


class Dice:
    """
    Representation of dices.
    """

    def __init__(self, number=1, maximum=20):
        self.number = number
        self.max = maximum

    def roll(self, modifier=0):
        values = []

        for i in range(self.number):
            values.append(randint(1, self.max))

        return sum(values) + modifier


class Abilities:
    """
    Representation of the abilities that the character has.
    """

    def __init__(
            self,
            strength=10,
            dexterity=10,
            constitution=10,
            intelligence=10,
            wisdom=10,
            charisma=10,
    ):
        """
        Initialize the attributes to describe the abilities
        """
        self.values = {
            'STR': strength,
            'DEX': dexterity,
            'CON': constitution,
            'INT': intelligence,
            'WIS': wisdom,
            'CHA': charisma,
        }

    def assign_new_scores(
            self,
            strength,
            dexterity,
            constitution,
            intelligence,
            wisdom,
            charisma,
    ):
        self.values['STR'] = strength
        self.values['DEX'] = dexterity
        self.values['CON'] = constitution
        self.values['INT'] = intelligence
        self.values['WIS'] = wisdom
        self.values['CHA'] = charisma

    def score(self, ability):
        """
        Returns tha ability score to a given ability
        """
        ability = ability.upper()
        chosen_ability = self.values[ability]

        return floor((chosen_ability - 10) / 2)

    def increment_ability(self, ability, value=1):
        """
        Adds 1 to the ability value
        """
        self.values[ability] += value

    def decrement_ability(self, ability, value=1):
        """
        Subtracts 1 of the the ability value
        """
        self.values[ability] -= value

    def change_value_ability(self, ability, value):
        """
        Adds any given value to the ability value
        """
        self.values[ability] += value


class Armor:
    """
    Represents a traditional armor
    """

    def __init__(
            self,
            name,
            armor_type,
            weight,
            armor_class,
            cost=0,
            stealth_disadvantage=False,
            dex_max=False,
            strength=False,
    ):
        self.name = name
        self.armor_type = armor_type
        self.cost = cost
        self.armor_class = armor_class
        self.stealth_disadvantage = stealth_disadvantage
        self.weight = weight
        self.dex_max = dex_max
        self.strength = strength


class Weapon:
    """
    Represents a traditional weapon
    """

    def __init__(
            self,
            name,
            damage_type,
            properties=None,
            melee=False,
            ranged=False,
            simple=False,
            martial=False,
            cost=0,
            damage=Dice(number=1, maximum=4),
            weight=0,
    ):
        """
        Initialize the attribute to describe a ranged weapon
        """

        if properties is None:
            properties = []

        self.name = name
        self.melee = melee
        self.ranged = ranged
        self.simple = simple
        self.martial = martial
        self.cost = cost
        self.damage = damage
        self.damage_type = damage_type
        self.weight = weight
        self.properties = properties


class AdventuringGear:
    """
    Represents adventuring gear, according to the Player's Handbook
    """

    def __init__(
            self,
            name,
            cost,
            weight=0,
            units=1,
            size=None
    ):
        """
        Initializes the attributes of an adventuring gear
        """
        self.name = name
        self.cost = cost
        self.weight = weight
        self.units = units
        self.size = size


class Tool(AdventuringGear):
    def __init__(
            self,
            name,
            cost,
            weight=0,
            units=1,
            size=None,
    ):
        super().__init__(name, cost, weight, units, size)


class MountsAndVehicles(AdventuringGear):
    def __init__(
            self,
            name,
            cost,
            speed,
            carrying_capacity=None
    ):
        super().__init__(
            name=name,
            cost=cost,
            weight=0,
            units=1,
            size=None
        )
        self.speed = speed
        self.carrying_capacity = carrying_capacity


class Trinket(AdventuringGear):
    def __init__(
            self,
            name
    ):
        super().__init__(
            name=name,
            cost=0,
            weight=0,
            units=1,
            size=None
        )


class Race:
    """ Generic form containing all relevant information about a race
    Aims to be used to creating the specific races from the Player's Handbook
    """

    def __init__(
            self,
            name,
            ability_increase,
            size,
            speed,
            languages,
            age,
            alignment,
            height,
            hit_point_increase=0,
            advantages=None,
            disadvantages=None,
            resistances=None,
            armor_proficiency=None,
            weapon_proficiency=None,
            tools_proficiency=None,
            number_tools=0,
            tools_options=None,
            skills_proficiency=None,
            double_proficiency=None,
            features=None,
            magical_ability=None,
    ):
        if advantages is None:
            advantages = []

        if disadvantages is None:
            disadvantages = []

        if resistances is None:
            resistances = []

        if armor_proficiency is None:
            armor_proficiency = []

        if weapon_proficiency is None:
            weapon_proficiency = []

        if tools_proficiency is None:
            tools_proficiency = []

        if skills_proficiency is None:
            skills_proficiency = []

        if double_proficiency is None:
            double_proficiency = []

        if tools_options is None:
            tools_options = []

        if features is None:
            features = []

        if magical_ability is None:
            magical_ability = MagicAbilities()

        self.name = name
        self.ability_increase = ability_increase
        self.size = size
        self.speed = speed
        self.languages = languages
        self.advantages = advantages
        self.disadvantages = disadvantages
        self.resistances = resistances
        self.armor_proficiency = armor_proficiency
        self.weapon_proficiency = weapon_proficiency
        self.tools_proficiency = tools_proficiency
        self.number_tools = number_tools
        self.tools_options = tools_options
        self.skills_proficiency = skills_proficiency
        self.double_proficiency = double_proficiency
        self.hit_point_increase = hit_point_increase
        self.features = features
        self.age = age
        self.alignment = alignment
        self.height = height
        self.magical_ability = magical_ability


class MagicAbilities:
    def __init__(
            self,
            has_magic=None,
            magical_ability=None,
            cantrips_by_level=None,
            spells_by_level=None,
            spells_known=0,
            cantrips_known=0,
            highest_spell_level=0,
            spells=None,
            cantrips=None,
            spell_slots_by_level=None,
            spell_slots=None,
            slots_spent=None,
            spell_save_dc=0,
            spell_attack_modifier=0,
            prepare_spells=False,
            def_num_prep_spells=None,
            number_prepared_spells=None,
            prepared_spells=None,
            spell_list=None,
    ):
        if has_magic is not None:
            if spells is None:
                spells = {}

            if cantrips is None:
                cantrips = []

            if cantrips_by_level is None:
                cantrips_by_level = {}
                for level in range(1, 20 + 1):
                    cantrips_by_level[level] = 0

            if spells_by_level is None:
                spells_by_level = {}
                for level in range(1, 20 + 1):
                    spells_by_level[level] = 0

            if spell_slots_by_level is None:
                spell_slots_by_level = {}

                for character_level in range(1, 20 + 1):
                    slots = {}

                    for level in range(1, 1 + highest_spell_level):
                        slots[level] = 0

                    spell_slots_by_level[character_level] = slots

            if spell_slots is None:
                spell_slots = spell_slots_by_level[1]

            if slots_spent is None:
                slots_spent = {}
                for level in range(1, 1 + highest_spell_level):
                    slots_spent[level] = 0

            if prepare_spells:
                if number_prepared_spells is None:
                    number_prepared_spells = 0

                if prepared_spells is None:
                    prepared_spells = []

        self.has_magic = has_magic
        self.magical_ability = magical_ability
        self.cantrips_by_level = cantrips_by_level
        self.spells_by_level = spells_by_level
        self.spells_known = spells_known
        self.cantrips_known = cantrips_known
        self.highest_spell_level = highest_spell_level
        self.spells = spells
        self.cantrips = cantrips
        self.spell_slots_by_level = spell_slots_by_level
        self.spell_slots = spell_slots
        self.slots_spent = slots_spent
        self.spell_save_dc = spell_save_dc
        self.spell_attack_modifier = spell_attack_modifier
        self.prepare_spells = prepare_spells
        self.def_num_prep_spells = def_num_prep_spells
        self.number_prepared_spells = number_prepared_spells
        self.prepared_spells = prepared_spells
        self.spell_list = spell_list

    def set_spells(self, new_spells):
        for level, spells in new_spells.items():
            try:
                if isinstance(spells, list):
                    for spell in spells:
                        if spell not in self.spells[level]:
                            self.spells[level].append(spell)
                elif spells not in self.spells[level]:
                    self.spells[level].append(spells)
            except KeyError:
                if isinstance(spells, list):
                    self.spells[level] = spells
                else:
                    self.spells[level] = [spells]

        if not new_spells:
            self.spells = {}

    def set_cantrips(self, cantrips):
        if isinstance(cantrips, list):
            for cantrip in cantrips:
                if cantrip not in self.cantrips:
                    self.cantrips.append(cantrip)
        else:
            if cantrips not in self.cantrips:
                self.cantrips.append(cantrips)

        if not cantrips:
            self.cantrips.clear()


class Class:
    """ Generic form containing all relevant information about a class
    Aims to be used to create the specific classes from the Player's Handbook
    """
    proficiency_by_level = {
        1: 2, 2: 2, 3: 2, 4: 2, 5: 3, 6: 3, 7: 3, 8: 3, 9: 4, 10: 4, 11: 4,
        12: 4, 13: 5, 14: 5, 15: 5, 16: 5, 17: 6, 18: 6, 19: 6, 20: 6,
    }

    def __init__(
            self,
            name,
            hit_die,
            specialization_level,
            level,
            proficiency,
            saving_throw_proficiency,
            number_skills,
            possible_skills,
            magical_ability,
            number_tools=0,
            tools_options=None,
            skills_proficiency=None,
            all_features=None,
            armor_proficiency=None,
            weapon_proficiency=None,
            tools_proficiency=None,
            equipment_options=None,
            equipment=None,
            specialization=None,
            specializations_features=None,
            starting_wealth=0,
            wealth=0,
    ):
        if tools_options is None:
            tools_options = []

        if skills_proficiency is None:
            skills_proficiency = []

        if all_features is None:
            all_features = {}

        if armor_proficiency is None:
            armor_proficiency = []

        if weapon_proficiency is None:
            weapon_proficiency = []

        if tools_proficiency is None:
            tools_proficiency = []

        if equipment_options is None:
            equipment_options = []

        if specializations_features is None:
            specializations_features = {}

        if equipment is None:
            equipment = []

        features = all_features[1]
        specialization = self.specialization_check(
            level=1,
            specialization_level=specialization_level,
            specializations_features=specializations_features,
            specialization=specialization
        )
        specialization_features = self.select_specialization_features(
            level=1,
            specialization_level=specialization_level,
            specializations_features=specializations_features,
            specialization=specialization
        )
        features = self.unite_specialization_features(
            level=1,
            specialization_features=specialization_features,
            features=features
        )

        self.name = name
        self.hit_die = hit_die
        self.specialization_level = specialization_level
        self.level = level
        self.all_features = all_features
        self.features = features
        self.proficiency = proficiency
        self.saving_throw_proficiency = saving_throw_proficiency
        self.number_skills = number_skills
        self.possible_skills = possible_skills
        self.skills_proficiency = skills_proficiency
        self.armor_proficiency = armor_proficiency
        self.weapon_proficiency = weapon_proficiency
        self.tools_proficiency = tools_proficiency
        self.tools_options = tools_options
        self.number_tools = number_tools
        self.equipment_options = equipment_options
        self.equipment = equipment
        self.specialization = specialization
        self.specialization_features = specialization_features
        self.specializations_features = specializations_features
        self.magical_ability = magical_ability
        self.starting_wealth = starting_wealth
        self.wealth = wealth

    @staticmethod
    def select_features(
            level,
            all_features,
    ):
        """ Loop through all the dictionary containing all the class features
        and append to a list the features until the current level, assigning
        this list to the variable of features.
        """
        features = []

        for i in range(1, level + 1):
            if all_features[i]:
                features += all_features[i]

        return features

    @staticmethod
    def specialization_check(
            level,
            specialization_level,
            specializations_features,
            specialization,
    ):
        """ Given the list of possible specializations and the selected
        specialization this function checks if the variable is according to the
        list and, if not, gives the possibility for the player to do his choice
        again.
        """

        if level >= specialization_level and \
                specialization not in specializations_features:

            end = False

            specialization_choices = []

            for key in specializations_features.keys():
                specialization_choices.append(key)

            if specialization not in specialization_choices:
                if specialization not in [False, None]:
                    print('\nSpecialization error!')
                    print('This name does not exist. Please check spelling\n')

            while not end:
                print('Specializations available for your class:')

                choices = {}
                number = 1
                for specialization in specialization_choices:
                    print(f'({number:02d}) {specialization.title()}')
                    choices[str(number)] = specialization
                    number += 1

                specialization = input('Type your choice: ')
                specialization = specialization.upper()

                if specialization in specialization_choices:
                    end = True
                elif specialization in choices:
                    specialization = choices[specialization]
                    end = True
                else:
                    print('\nThis name does not exist. '
                          'Please check spelling\n')

        if level < specialization_level:
            specialization = False

        return specialization

    def select_specialization_features(
            self,
            level,
            specialization_level,
            specializations_features,
            specialization
    ):
        """
        Given the chose specialization and a dictionary in which the keys
        are the name of the specializations of the class and the values its
        corresponding features, select, if the specialization is valid, the
        according features.
        :param level:
        :param specialization_level:
        :param specializations_features:
        :param specialization:
        :return:
        """

        specialization = self.specialization_check(
            level=level,
            specialization_level=specialization_level,
            specializations_features=specializations_features,
            specialization=specialization,
        )

        specialization_features = []

        if specialization:
            specialization_features = specializations_features[specialization]

        return specialization_features

    @staticmethod
    def unite_specialization_features(
            level,
            specialization_features,
            features
    ):
        for i in range(1, level+1):
            if i in specialization_features:
                features.append(specialization_features[i])

        return features


class Barbarian(Class):
    """The Barbarian class from the Player's Handbook"""
    def __init__(
            self,
            level,
            equipment_options,
            equipment,
            starting_wealth,
    ):
        super().__init__(
            name='BARBARIAN',
            hit_die=Dice(1, 12),
            specialization_level=3,
            level=level,
            all_features={
                1: ['RAGE', 'UNARMORED DEFENSE'],
                2: ['RECKLESS ATTACK', 'DANGER SENSE'],
                3: ['PRIMAL PATH'],
                4: [],
                5: ['EXTRA ATTACK', 'FAST MOVEMENT'],
                6: [],
                7: ['FERAL INSTINCT'],
                8: [],
                9: ['BRUTAL CRITICAL (1 DIE)'],
                10: [],
                11: ['RELENTLESS RAGE'],
                12: [],
                13: ['BRUTAL CRITICAL (2 DICE)'],
                14: [],
                15: ['PERSISTENT RAGE'],
                16: [],
                17: ['BRUTAL CRITICAL (3 DICE)'],
                18: ['INDOMITABLE MIGHT'],
                19: [],
                20: ['PRIMAL CHAMPION']
            },
            proficiency=super().proficiency_by_level[1],
            saving_throw_proficiency=['STR', 'CON', ],
            number_skills=2,
            possible_skills=[
                'ANIMAL HANDLING', 'ATHLETICS', 'INTIMIDATION',
                'NATURE', 'PERCEPTION', 'SURVIVAL'
            ],
            armor_proficiency=['LIGHT', 'MEDIUM', 'SHIELD', ],
            weapon_proficiency=['SIMPLE', 'MARTIAL', ],
            equipment_options=equipment_options,
            equipment=equipment,
            specializations_features={
                'PATH OF THE BERSERKER': {
                    3: ['FRENZY'],
                    6: ['MINDLESS RAGE'],
                    10: ['INTIMIDATING PRESENCE'],
                    14: ['RETALIATION'],
                },
                'PATH OF THE TOTEM WARRIOR': {
                    3: [
                        'SPIRIT SEEKER',
                        {'TOTEM SPIRIT': ['BEAR', 'EAGLE', 'WOLF']},
                    ],
                    6: [{'ASPECT OF THE BEAST': ['BEAR', 'EAGLE', 'WOLF']}],
                    10: ['SPIRIT WALKER'],
                    14: [{'TOTEMIC ATTUNEMENT': ['BEAR', 'EAGLE', 'WOLF']}],
                },
            },
            starting_wealth=starting_wealth,
            magical_ability=MagicAbilities()
        )


class Bard(Class):
    """The Bard class, according to the Player's Handbook"""
    all_features = {
        1: ['SPELLCASTING', 'BARDIC INSPIRATION (D6)'],
        2: ['JACK OF ALL TRADES', 'SONG OF REST (D6)'],
        3: ['BARD COLLEGE', 'EXPERTISE'],
        4: [],
        5: ['BARDIC INSPIRATION (D8)', 'FONT OF INSPIRATION'],
        6: ['COUNTERCHARM', 'SPECIALIZATION FEATURE'],
        7: [],
        8: [],
        9: ['SONG OF REST (D8)'],
        10: ['BARDIC INSPIRATION (D10)', 'EXPERTISE', 'MAGICAL SECRETS'],
        11: [],
        12: [],
        13: ['SONG OF REST (D10)'],
        14: ['MAGICAL SECRETS', 'SPECIALIZATION FEATURE'],
        15: ['BARDIC INSPIRATION (D12)'],
        16: [],
        17: ['SONG OF REST (D12)'],
        18: ['MAGICAL SECRETS'],
        19: [],
        20: ['SUPERIOR INSPIRATION'],
    }
    spells_known = {
        1: 4, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1,
        9: 1, 10: 2, 11: 1, 12: 0, 13: 1, 14: 2,
        15: 1, 16: 0, 17: 1, 18: 2, 19: 0, 20: 0,
    }
    cantrips_known = {
        1: 2, 2: 0, 3: 0, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 1,
        11: 0, 12: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0
    }
    spells_slots = {
        1: {1: 2, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        2: {1: 3, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        3: {1: 4, 2: 2, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        4: {1: 4, 2: 3, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        5: {1: 4, 2: 3, 3: 2, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        6: {1: 4, 2: 3, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        7: {1: 4, 2: 3, 3: 3, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        8: {1: 4, 2: 3, 3: 3, 4: 2, 5: 1, 6: 0, 7: 0, 8: 0, 9: 0},
        9: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 0, 7: 0, 8: 0, 9: 0},
        10: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 0, 7: 0, 8: 0, 9: 0},
        11: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 0, 9: 0},
        12: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 0, 9: 0},
        13: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 0, 9: 0},
        14: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 0, 9: 0},
        15: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 0},
        16: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 0},
        17: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1},
        18: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 1, 7: 1, 8: 1, 9: 1},
        19: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 1, 8: 1, 9: 1},
        20: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 2, 8: 1, 9: 1},
    }
    specialization_level = 3
    specializations_features = {
        'COLLEGE OF LORE': {
            3: [
                'BONUS PROFICIENCIES',
                'CUTTING WORDS',
            ],
            6: [
                'ADDITIONAL MAGICAL SECRETS',
            ],
            14: [
                'PEERLESS SKILL',
            ],
        },
        'COLLEGE OF VALOR': {
            3: [
                'BONUS PROFICIENCIES',
                'COMBAT INSPIRATION',
            ],
            6: [
                'EXTRA ATTACK',
            ],
            14: [
                'BATTLE MAGIC',
            ]
        }

    }

    def __init__(
            self,
            abilities,
            level,
            equipment_options,
            equipment,
            starting_wealth
    ):
        proficiency = super().proficiency_by_level[1]

        super().__init__(
            name='BARD',
            hit_die=Dice(1, 8),
            specialization_level=self.specialization_level,
            level=level,
            all_features=self.all_features,
            proficiency=proficiency,
            saving_throw_proficiency=['DEX', 'CHA'],
            number_skills=3,
            possible_skills=[
                'ATHLETICS', 'ACROBATICS', 'SLEIGHT OF HAND', 'STEALTH',
                'ARCANA', 'HISTORY', 'INVESTIGATION', 'NATURE', 'RELIGION',
                'ANIMAL HANDLING', 'INSIGHT', 'MEDICINE', 'PERCEPTION',
                'SURVIVAL', 'DECEPTION', 'INTIMIDATION', 'PERFORMANCE',
                'PERSUASION',
            ],
            armor_proficiency=['LIGHT'],
            weapon_proficiency=[
                'SIMPLE', 'HAND CROSSBOW', 'LONGSWORD', 'RAPIER',
                'SHORTSWORDS',
            ],
            equipment_options=equipment_options,
            equipment=equipment,
            specializations_features=self.specializations_features,
            starting_wealth=starting_wealth,
            number_tools=3,
            tools_options=[
                'BAGPIPES', 'DRUM', 'DULCIMER', 'FLUTE', 'LUTE',
                'LYRE', 'HORN', 'PAN FLUTE', 'SHAWM', 'VIOL'
            ],
            magical_ability=MagicAbilities(
                has_magic=True,
                magical_ability='CHA',
                spells_known=self.spells_known[1],
                cantrips_known=self.cantrips_known[1],
                highest_spell_level=9,
                spells=None,
                cantrips=None,
                spell_slots_by_level=self.spells_slots,
                spell_slots=self.spells_slots[1],
                slots_spent=None,
                spell_save_dc=8+proficiency+abilities.score('CHA'),
                spell_attack_modifier=proficiency+abilities.score('CHA'),
                spell_list='BARD',
            )
        )


class Cleric(Class):
    all_features = {
        1: ['SPELLCASTING', 'DIVINE DOMAIN'],
        2: ['CHANNEL DIVINITY (1/REST)'],
        3: [],
        4: [],
        5: ['DESTROY UNDEAD (CR 1/2)'],
        6: ['CHANNEL DIVINITY (2/REST)'],
        7: [],
        8: ['DESTROY UNDEAD (CR 1)'],
        9: [],
        10: ['DIVINE INTERVENTION'],
        11: ['DESTROY UNDEAD (CR 2)'],
        12: [],
        13: [],
        14: ['DESTROY UNDEAD (CR 3)'],
        15: [],
        16: [],
        17: ['DESTROY UNDEAD (CR 4)'],
        18: ['CHANNEL DIVINITY (3/REST)'],
        19: [],
        20: ['DIVINE INTERVENTION IMPROVEMENT']
    }
    specializations_features = {
        'KNOWLEDGE DOMAIN': {
            1: ['BLESSINGS OF KNOWLEDGE'],
            2: ['CHANNEL DIVINITY: KNOWLEDGE OF THE AGES'],
            6: ['CHANNEL DIVINITY: READ THOUGHTS'],
            8: ['POTENT SPELLCASTING'],
            17: ['VISIONS OF THE PAST']
        },
        'LIFE DOMAIN': {
            1: ['BONUS PROFICIENCY', 'DISCIPLE OF LIFE'],
            2: ['CHANNEL DIVINITY: PRESERVE LIFE'],
            6: ['BLESSED HEALER'],
            8: ['DIVINE STRIKE'],
            17: ['SUPREME HEALING']
        },
        'LIGHT DOMAIN': {
            1: ['BONUS CANTRIP', 'WARDING FLARE'],
            2: ['CHANNEL DIVINITY: RADIANCE OF THE DAWN'],
            6: ['IMPROVED FLARE'],
            8: ['POTENT SPELLCASTING'],
            17: ['CORONA OF LIGHT']
        },
        'NATURE DOMAIN': {
            1: ['ACOLYTE OF NATURE', 'BONUS PROFICIENCY'],
            2: ['CHANNEL DIVINITY: CHARM ANIMALS AND PLANTS'],
            6: ['DAMPEN ELEMENTS'],
            8: ['DIVINE STRIKE'],
            17: ['MASTER OF NATURE']
        },
        'TEMPEST DOMAIN': {
            1: ['BONUS PROFICIENCIES', 'WRATH OF THE STORM'],
            2: ['CHANNEL DIVINITY: DESTRUCTIVE WRATH'],
            6: ['THUNDERBOLT STRIKE'],
            8: ['DIVINE STRIKE'],
            17: ['STORMBORN']
        },
        'TRICKERY DOMAIN': {
            1: ['BLESSING OF THE TRICKSTER'],
            2: ['CHANNEL DIVINITY: INVOKE DUPLICITY'],
            6: ['CHANNEL DIVINITY: CLOAK OF SHADOWS'],
            8: ['DIVINE STRIKE'],
            17: ['IMPROVED DUPLICITY'],
        },
        'WAR DOMAIN': {
            1: ['BONUS PROFICIENCIES', 'WAR PRIEST'],
            2: ['CHANNEL DIVINITY: GUIDED STRIKE'],
            6: ['CHANNEL DIVINITY: WAR GOD\'S BLESSING'],
            8: ['DIVINE STRIKE'],
            17: ['AVATAR OF BATTLE']
        }
    }
    cantrips_known = {
        1: 3, 2: 0, 3: 0, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 1, 11: 0,
        12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0
    }
    spells_slots = {
        1: {1: 2, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        2: {1: 3, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        3: {1: 4, 2: 2, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        4: {1: 4, 2: 3, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        5: {1: 4, 2: 3, 3: 2, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        6: {1: 4, 2: 3, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        7: {1: 4, 2: 3, 3: 3, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        8: {1: 4, 2: 3, 3: 3, 4: 2, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        9: {1: 4, 2: 3, 3: 3, 4: 3, 5: 1, 6: 0, 7: 0, 8: 0, 9: 0},
        10: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 0, 7: 0, 8: 0, 9: 0},
        11: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 0, 9: 0},
        12: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 0, 9: 0},
        13: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 0, 9: 0},
        14: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 0, 9: 0},
        15: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 0},
        16: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 0},
        17: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1},
        18: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 1, 7: 1, 8: 1, 9: 1},
        19: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 1, 8: 1, 9: 1},
        20: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 2, 8: 1, 9: 1}
    }
    specialization_level = 1

    @staticmethod
    def def_num_prep_spells(score, level):
        number = score + level

        if number > 1:
            return number
        else:
            return 1

    def __init__(
            self,
            abilities,
            level,
            equipment_options,
            equipment,
            starting_wealth,
    ):
        proficiency = super().proficiency_by_level[1]

        super().__init__(
            name='CLERIC',
            hit_die=Dice(maximum=8),
            specialization_level=self.specialization_level,
            level=level,
            all_features=self.all_features,
            proficiency=proficiency,
            saving_throw_proficiency=['WIS', 'CHA'],
            number_skills=2,
            possible_skills=[
                'HISTORY', 'INSIGHT', 'MEDICINE', 'PERSUASION', 'RELIGION'
            ],
            armor_proficiency=['LIGHT', 'MEDIUM', 'SHIELDS'],
            weapon_proficiency=['SIMPLE'],
            equipment_options=equipment_options,
            equipment=equipment,
            specializations_features=self.specializations_features,
            starting_wealth=starting_wealth,
            magical_ability=MagicAbilities(
                has_magic=True,
                magical_ability='WIS',
                spells_known=-1,
                highest_spell_level=9,
                cantrips_by_level=self.cantrips_known,
                cantrips_known=self.cantrips_known[1],
                spell_slots_by_level=self.spells_slots,
                spell_slots=self.spells_slots[1],
                spell_save_dc=8+proficiency+abilities.score('WIS'),
                prepare_spells=True,
                def_num_prep_spells=self.def_num_prep_spells,
                number_prepared_spells=self.def_num_prep_spells(
                    score=abilities.score('WIS'),
                    level=1
                ),
                spell_attack_modifier=proficiency+abilities.score('WIS'),
                spell_list='CLERIC',
            )
        )


class Druid(Class):
    specialization_level = 2
    specializations_features = {
        'CIRCLE OF THE LAND': {
            2: ['BONUS CANTRIP', 'NATURAL RECOVERY'],
            3: {'CIRCLE SPELLS': [
                'ARTIC',
                'COAST',
                'DESERT',
                'FOREST',
                'GRASSLAND',
                'MOUNTAIN',
                'SWAMP',
                'UNDERDARK'
            ]
            },
            6: ['LAND\'S STRIDE'],
            10: ['NATURE\'S WARD'],
            14: ['NATURE\'S SANCTUARY']
        },
        'CIRCLE OF THE MOON': {
            2: ['COMBAT WILD SHAPE', 'CIRCLE FORMS'],
            6: ['PRIMAL STRIKE'],
            10: ['ELEMENTAL WILD SHAPE'],
            14: ['THOUSAND FORMS']
        }
    }
    all_features = {
        1: ['DRUIDIC', 'SPELLCASTING'],
        2: ['WILD SHAPE'],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],
        11: [],
        12: [],
        13: [],
        14: [],
        15: [],
        16: [],
        17: [],
        18: ['TIMELESS BODY', 'BEAST SPELLS'],
        19: [],
        20: ['ARCHDRUID']
    }
    cantrips_known = {
        1: 2, 2: 0, 3: 0, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 1,
        11: 0, 12: 0, 13: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0
    }
    spells_slots = {
        1: {1: 2, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        2: {1: 3, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        3: {1: 4, 2: 2, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        4: {1: 4, 2: 3, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        5: {1: 4, 2: 3, 3: 2, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        6: {1: 4, 2: 3, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        7: {1: 4, 2: 3, 3: 3, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        8: {1: 4, 2: 3, 3: 3, 4: 2, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        9: {1: 4, 2: 3, 3: 3, 4: 3, 5: 1, 6: 0, 7: 0, 8: 0, 9: 0},
        10: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 0, 7: 0, 8: 0, 9: 0},
        11: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 0, 9: 0},
        12: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 0, 9: 0},
        13: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 0, 9: 0},
        14: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 0, 9: 0},
        15: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 0},
        16: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 0},
        17: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1},
        18: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 1, 7: 1, 8: 1, 9: 1},
        19: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 1, 8: 1, 9: 1},
        20: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 2, 8: 1, 9: 1},
    }

    @staticmethod
    def def_num_prep_spells(score, level):
        number = score + level
        if number > 1:
            return number
        else:
            return 1

    def __init__(
            self,
            abilities,
            level,
            equipment_options,
            equipment,
            starting_wealth
    ):
        proficiency = super().proficiency_by_level[1]

        super().__init__(
            name='DRUID',
            hit_die=Dice(maximum=8),
            specialization_level=self.specialization_level,
            level=level,
            all_features=self.all_features,
            proficiency=proficiency,
            saving_throw_proficiency=['INT', 'WIS'],
            number_skills=2,
            possible_skills=[
                'ARCANA', 'ANIMAL HANDLING', 'INSIGHT', 'MEDICINE', 'NATURE',
                'PERCEPTION', 'RELIGION', 'SURVIVAL'
            ],
            armor_proficiency=['LIGHT', 'MEDIUM', 'SHIELD'],
            weapon_proficiency=[
                'CLUB', 'DAGGER', 'DART', 'JAVELIN', 'MACE', 'QUARTERSTAFF',
                'SCIMITAR', 'SICKLE', 'SLING', 'SPEAR'
            ],
            tools_proficiency=['HERBALISM KIT'],
            equipment_options=equipment_options,
            equipment=equipment,
            specialization=None,
            specializations_features=self.specializations_features,
            starting_wealth=starting_wealth,
            magical_ability=MagicAbilities(
                has_magic=True,
                magical_ability='WIS',
                spells_known=-1,
                cantrips_known=self.cantrips_known[1],
                highest_spell_level=9,
                spell_slots_by_level=self.spells_slots,
                spell_slots=self.spells_slots[1],
                spell_save_dc=8 + proficiency + abilities.score('WIS'),
                prepare_spells=True,
                def_num_prep_spells=self.def_num_prep_spells,
                number_prepared_spells=self.def_num_prep_spells(
                    abilities.score('WIS'), 1
                ),
                spell_attack_modifier=proficiency+abilities.score('WIS'),
                spell_list='DRUID'
            )
        )


class Fighter(Class):
    specialization_level = 3
    all_features = {
        1: ['FIGHTING STYLE', 'SECOND WIND'],
        2: ['ACTION SURGE (ONE USE)'],
        3: [],
        4: [],
        5: ['EXTRA ATTACK'],
        6: [],
        7: [],
        8: [],
        9: ['INDOMITABLE (ONE USE)'],
        10: [],
        11: ['EXTRA ATTACK (2)'],
        12: [],
        13: ['INDOMITABLE (TWO USES)'],
        14: [],
        15: [],
        16: [],
        17: ['ACTION SURGE (TWO USES)', 'INDOMITABLE (THREE USES)'],
        18: [],
        19: [],
        20: ['EXTRA ATTACK (3)']
    }
    cantrips_known = {
        1: 0, 2: 0, 3: 3, 4: 1, 5: 0, 6: 0, 7: 1, 8: 1, 9: 0, 10: 1, 11: 1,
        12: 0, 13: 1, 14: 1, 15: 0, 16: 1, 17: 0, 18: 0, 19: 1, 20: 1
    }
    spells_known = {
        1: 0, 2: 0, 3: 2, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 1, 11: 0,
        12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0
    }
    specializations_features = {
        'CHAMPION': {
            3: ['IMPROVED CRITICAL'],
            7: ['REMARKABLE ATHLETE'],
            10: ['ADDITIONAL FIGHTING STYLE'],
            15: ['SUPERIOR CRITICAL'],
            18: ['SURVIVOR'],
        },
        'BATTLE MASTER': {
            3: [{'COMBAT SUPERIORITY': [
                'MANEUVERS',
                'SUPERIORITY DICE',
                'SAVING THROWS'
            ]
            },
                'STUDENT OF WAR'
            ],
            7: ['KNOW YOUR ENEMY'],
            10: ['IMPROVED COMBAT SUPERIORITY (D10)'],
            15: ['RELENTLESS'],
            18: ['IMPROVED COMBAT SUPERIORITY (D12)']
        },
        'ELDRITCH KNIGHT': {
            3: ['SPELLCASTING', 'WEAPON BOND'],
            7: ['WAR MAGIC'],
            10: ['ELDRITCH STRIKE'],
            15: ['ARCANE CHARGE'],
            18: ['IMPROVED WAR MAGIC']
        }
    }
    spells_slots = {
        1: {1: 0, 2: 0, 3: 0, 4: 0},
        2: {1: 0, 2: 0, 3: 0, 4: 0},
        3: {1: 2, 2: 0, 3: 0, 4: 0},
        4: {1: 3, 2: 0, 3: 0, 4: 0},
        5: {1: 3, 2: 0, 3: 0, 4: 0},
        6: {1: 3, 2: 0, 3: 0, 4: 0},
        7: {1: 4, 2: 2, 3: 0, 4: 0},
        8: {1: 4, 2: 2, 3: 0, 4: 0},
        9: {1: 4, 2: 2, 3: 0, 4: 0},
        10: {1: 4, 2: 3, 3: 0, 4: 0},
        11: {1: 4, 2: 3, 3: 0, 4: 0},
        12: {1: 4, 2: 3, 3: 0, 4: 0},
        13: {1: 4, 2: 3, 3: 2, 4: 0},
        14: {1: 4, 2: 3, 3: 2, 4: 0},
        15: {1: 4, 2: 3, 3: 2, 4: 0},
        16: {1: 4, 2: 3, 3: 3, 4: 0},
        17: {1: 4, 2: 3, 3: 3, 4: 0},
        18: {1: 4, 2: 3, 3: 3, 4: 0},
        19: {1: 4, 2: 3, 3: 3, 4: 1},
        20: {1: 4, 2: 3, 3: 3, 4: 1}
    }

    def __init__(
            self,
            abilities,
            level,
            equipment_options,
            starting_wealth
    ):
        proficiency = super().proficiency_by_level[1]

        super().__init__(
            name='FIGHTER',
            hit_die=Dice(10, abilities.score('CON')),
            specialization_level=self.specialization_level,
            level=level,
            all_features=self.all_features,
            proficiency=proficiency,
            saving_throw_proficiency=['STR', 'CON'],
            number_skills=2,
            possible_skills=[
                'ACROBATICS', 'ANIMAL HANDLING', 'ATHLETICS', 'HISTORY',
                'INSIGHT', 'INTIMIDATION', 'PERCEPTION', 'SURVIVAL'
            ],
            armor_proficiency=['LIGHT', 'MEDIUM', 'HEAVY', 'SHIELDS'],
            weapon_proficiency=['SIMPLE', 'MARTIAL'],
            equipment_options=equipment_options,
            specialization=None,
            specializations_features=self.specializations_features,
            starting_wealth=starting_wealth,
            magical_ability=MagicAbilities(
                has_magic=False,
                magical_ability='INT',
                spells_known=self.spells_known[1],
                cantrips_known=self.cantrips_known[1],
                highest_spell_level=4,
                spell_slots_by_level=self.spells_slots,
                spell_slots=self.spells_slots[1],
                spell_save_dc=8+proficiency+abilities.score('INT'),
                spell_attack_modifier=proficiency+abilities.score('INT'),
                spell_list='WIZARD',
            )
        )


class Monk(Class):
    specialization_level = 3
    all_features = {
        1: ['UNARMORED DEFENSE', 'MARTIAL ARTS'],
        2: ['KI', 'UNARMORED MOVEMENT'],
        3: ['MONASTIC TRADITION', 'DEFLECT MISSILES'],
        4: ['SLOW FALL'],
        5: ['EXTRA ATTACK', 'STUNNING STRIKE'],
        6: ['KI-EMPOWERED STRIKES'],
        7: ['EVASION', 'STILLNESS OF MIND'],
        8: [],
        9: ['UNARMORED MOVEMENT IMPROVEMENT'],
        10: ['PURITY OF BODY'],
        11: [],
        12: [],
        13: ['TONGUE OF THE SUN AND MOON'],
        14: ['DIAMOND SOUL'],
        15: ['TIMELESS BODY'],
        16: [],
        17: [],
        18: ['EMPTY BODY'],
        19: [],
        20: ['PERFECT SELF']
    }
    specializations_features = {
        'WAY OF THE OPEN HAND': {
            3: ['OPEN HAND TECHNIQUE'],
            6: ['WHOLENESS OF BODY'],
            11: ['TRANQUILITY'],
            17: ['QUIVERING PALM']
        },
        'WAY OF SHADOW': {
            3: ['SHADOW ARTS'],
            6: ['SHADOW STEP'],
            11: ['CLOAK OF SHADOWS'],
            17: ['OPPORTUNIST']
        },
        'WAY OF THE FOUR ELEMENTS': {
            3: ['DISCIPLE OF THE ELEMENTS'],
            6: ['ADDITIONAL ELEMENTAL DISCIPLINE'],
            11: ['ADDITIONAL ELEMENTAL DISCIPLINE'],
            17: ['ADDITIONAL ELEMENTAL DISCIPLINE']
        }
    }

    def __init__(
            self,
            level,
            equipment_options,
            equipment,
            starting_wealth
    ):
        proficiency = super().proficiency_by_level[1]

        super().__init__(
            name='MONK',
            hit_die=Dice(maximum=8),
            specialization_level=self.specialization_level,
            level=level,
            all_features=self.all_features,
            proficiency=proficiency,
            saving_throw_proficiency=['STR', 'DEX'],
            number_skills=2,
            possible_skills=[
                'ACROBATICS', 'ATHLETICS', 'HISTORY',
                'INSIGHT', 'RELIGION', 'STEALTH'
            ],
            weapon_proficiency=['SIMPLE', 'SHORTSWORDS'],
            number_tools=1,
            tools_options=[
                "ALCHEMIST'S SUPPLIES", "BREWER'S SUPPLIES", "CARPENTER'S "
                "TOOLS", "CALLIGRAPHER'S SUPPLIES", "CARTOGRAPHER'S TOOLS",
                "COBBLER'S TOOLS", "COOK'S UTENSILS", "GLASSBOWER'S TOOLS",
                "JEWELER'S TOOLS", "LEATHERWORKER'S TOOLS", "MASON'S TOOLS",
                "PAINTER'S SUPPLIES", "POTTER'S TOOLS", "SMITH'S TOOLS",
                "TINKER'S TOOLS", "WEAVER'S TOOLS", "WOODCARVER'S TOOLS",
                'BAGPIPES', 'DRUM', 'DULCIMER', 'FLUTE', 'LUTE', 'LYRE', 'HORN',
                'PAN FLUTE', 'SHAWM', 'VIOL',
            ],
            equipment_options=equipment_options,
            equipment=equipment,
            specialization=None,
            specializations_features=self.specializations_features,
            starting_wealth=starting_wealth,
            magical_ability=MagicAbilities()
        )


class Paladin(Class):
    all_features = {
        1: ['DIVINE SENSE', 'LAY ON HANDS'],
        2: ['FIGHTING STYLE', 'SPELLCASTING', 'DIVINE SMITE'],
        3: ['DIVINE HEALTH', 'SACRED OATH'],
        4: [],
        5: ['EXTRA ATTACK'],
        6: ['AURA OF PROTECTION'],
        7: [],
        8: [],
        9: [],
        10: ['AURA OF COURAGE'],
        11: ['IMPROVED DIVINE SMITE'],
        12: [],
        13: [],
        14: ['CLEANSING TOUCH'],
        15: [],
        16: [],
        17: [],
        18: ['AURA IMPROVEMENTS'],
        19: [],
        20: []
    }
    specialization_level = 3
    specializations_features = {
        'OATH OF DEVOTION': {
            3: [{'CHANNEL DIVINITY': [
                'SACRED WEAPON',
                'TURN THE UNHOLY'
            ]}],
            7: ['AURA OF DEVOTION'],
            15: ['PURITY OF SPIRIT'],
            20: ['HOLY NIMBUS']
        },
        'OATH OF THE ANCIENTS': {
            3: [{'CHANNEL DIVINITY': [
                'NATURE\'S WRATH',
                'TURN THE FAITHLESS'
            ]}],
            7: ['AURA OF WARDING'],
            15: ['UNDYING SENTINEL'],
            20: ['ELDER CHAMPION']
        },
        'OATH OF VENGEANCE': {
            3: [{'CHANNEL DIVINITY': [
                'ABJURE ENEMY',
                'VOW OF ENMITY'
            ]}],
            7: ['RELENTLESS AVENGER'],
            15: ['SOUL OF VENGEANCE'],
            20: ['AVENGING ANGEL']
        }
    }
    spells_slots = {
        1: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
        2: {1: 2, 2: 0, 3: 0, 4: 0, 5: 0},
        3: {1: 3, 2: 0, 3: 0, 4: 0, 5: 0},
        4: {1: 3, 2: 0, 3: 0, 4: 0, 5: 0},
        5: {1: 4, 2: 2, 3: 0, 4: 0, 5: 0},
        6: {1: 4, 2: 2, 3: 0, 4: 0, 5: 0},
        7: {1: 4, 2: 3, 3: 0, 4: 0, 5: 0},
        8: {1: 4, 2: 3, 3: 0, 4: 0, 5: 0},
        9: {1: 4, 2: 3, 3: 2, 4: 0, 5: 0},
        10: {1: 4, 2: 3, 3: 2, 4: 0, 5: 0},
        11: {1: 4, 2: 3, 3: 3, 4: 0, 5: 0},
        12: {1: 4, 2: 3, 3: 3, 4: 0, 5: 0},
        13: {1: 4, 2: 3, 3: 3, 4: 1, 5: 0},
        14: {1: 4, 2: 3, 3: 3, 4: 1, 5: 0},
        15: {1: 4, 2: 3, 3: 3, 4: 2, 5: 0},
        16: {1: 4, 2: 3, 3: 3, 4: 2, 5: 0},
        17: {1: 4, 2: 3, 3: 3, 4: 3, 5: 1},
        18: {1: 4, 2: 3, 3: 3, 4: 3, 5: 1},
        19: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2},
        20: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2}
    }

    @staticmethod
    def def_num_prep_spells(score, level):
        number = floor(level/2) + score

        if number > 1:
            return number
        else:
            return 1

    def __init__(
            self,
            abilities,
            level,
            equipment_options,
            equipment,
            starting_wealth
    ):
        proficiency = super().proficiency_by_level[1]

        super().__init__(
            name='PALADIN',
            hit_die=Dice(maximum=10),
            specialization_level=self.specialization_level,
            level=level,
            all_features=self.all_features,
            proficiency=proficiency,
            saving_throw_proficiency=['WIS', 'CHA'],
            number_skills=2,
            possible_skills=[
                'ATHLETICS', 'INSIGHT', 'INTIMIDATION',
                'MEDICINE', 'PERSUASION', 'RELIGION'
            ],
            armor_proficiency=['LIGHT', 'MEDIUM', 'HEAVY', 'SHIELD'],
            weapon_proficiency=['SIMPLE', 'MARTIAL'],
            equipment_options=equipment_options,
            equipment=equipment,
            specialization=None,
            specializations_features=self.specializations_features,
            starting_wealth=starting_wealth,
            magical_ability=MagicAbilities(
                has_magic=True,
                magical_ability='CHA',
                spells_known=-1,
                highest_spell_level=5,
                spell_save_dc=8+proficiency+abilities.score('CHA'),
                prepare_spells=True,
                def_num_prep_spells=self.def_num_prep_spells,
                number_prepared_spells=self.def_num_prep_spells(
                    score=abilities.score('CHA'),
                    level=level
                ),
                spell_attack_modifier=proficiency+abilities.score('CHA'),
                spell_list='PALADIN',
            )
        )


class Ranger(Class):
    specialization_level = 3
    all_features = {
        1: ['FAVORED ENEMY', 'NATURAL EXPLORER'],
        2: ['FIGHTING STYLE', 'SPELLCASTING'],
        3: ['RANGER ARCHETYPE', 'PRIMEVAL AWARENESS'],
        4: [],
        5: ['EXTRA ATTACK'],
        6: ['FAVORED ENEMY AND NATURAL EXPLORER IMPROVEMENTS'],
        7: [],
        8: ['LAND\'S STRIDE'],
        9: [],
        10: ['NATURAL EXPLORER IMPROVEMENT', 'HIDE IN PLAIN SIGHT'],
        11: [],
        12: [],
        13: [],
        14: ['FAVORED ENEMY IMPROVEMENT', 'VANISH'],
        15: [],
        16: [],
        17: [],
        18: ['FERAL SENSES'],
        19: [],
        20: ['FOE SLAYER']
    }
    spells_known = {
        1: 0, 2: 2, 3: 1, 4: 0, 5: 1, 6: 0, 7: 1, 8: 0, 9: 1, 10: 0, 11: 1,
        12: 0, 13: 1, 14: 0, 15: 1, 16: 0, 17: 1, 18: 0, 19: 1, 20: 0
    }
    spells_slots = {
        1: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
        2: {1: 2, 2: 0, 3: 0, 4: 0, 5: 0},
        3: {1: 3, 2: 0, 3: 0, 4: 0, 5: 0},
        4: {1: 3, 2: 0, 3: 0, 4: 0, 5: 0},
        5: {1: 4, 2: 2, 3: 0, 4: 0, 5: 0},
        6: {1: 4, 2: 2, 3: 0, 4: 0, 5: 0},
        7: {1: 4, 2: 3, 3: 0, 4: 0, 5: 0},
        8: {1: 4, 2: 3, 3: 0, 4: 0, 5: 0},
        9: {1: 4, 2: 3, 3: 2, 4: 0, 5: 0},
        10: {1: 4, 2: 3, 3: 2, 4: 0, 5: 0},
        11: {1: 4, 2: 3, 3: 3, 4: 0, 5: 0},
        12: {1: 4, 2: 3, 3: 3, 4: 0, 5: 0},
        13: {1: 4, 2: 3, 3: 3, 4: 1, 5: 0},
        14: {1: 4, 2: 3, 3: 3, 4: 1, 5: 0},
        15: {1: 4, 2: 3, 3: 3, 4: 2, 5: 0},
        16: {1: 4, 2: 3, 3: 3, 4: 2, 5: 0},
        17: {1: 4, 2: 3, 3: 3, 4: 3, 5: 1},
        18: {1: 4, 2: 3, 3: 3, 4: 3, 5: 1},
        19: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2},
        20: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2}
    }
    specializations_features = {
        'HUNTER': {
            3: [{'HUNTER\'S PREY': [
                'COLOSSUS SLAYER',
                'GIANT KILLER',
                'HORDE BREAKER',
            ]}],
            7: [{'DEFENSIVE\'S TACTICS': [
                'ESCAPE THE HORDE',
                'MULTIATTACK DEFENSE',
                'STEEL WILL',
            ]}],
            11: [{'MULTIATTACK': [
                'VOLLEY',
                'WHIRLWIND ATTACK',
            ]}],
            15: [{'SUPERIOR HUNTER\'S DEFENSE': [
                'EVASION',
                'STAND AGAINST THE TIDE',
                'UNCANNY DODGE'
            ]}],
        },
        'BEST MASTER': {
            3: ['RANGER\'S COMPANION'],
            7: ['EXCEPTIONAL TRAINING'],
            11: ['BESTIAL FURY'],
            15: ['SHARE SPELLS'],
        }
    }

    def __init__(
            self,
            abilities,
            level,
            equipment_options,
            equipment,
            starting_wealth
    ):
        proficiency = super().proficiency_by_level[1]

        super().__init__(
            name='RANGER',
            hit_die=Dice(maximum=10),
            specialization_level=self.specialization_level,
            level=level,
            all_features=self.all_features,
            proficiency=proficiency,
            saving_throw_proficiency=['STR', 'DEX'],
            number_skills=3,
            possible_skills=[
                'ANIMAL HANDLING', 'ATHLETICS', 'INSIGHT', 'INVESTIGATION',
                'NATURE', 'PERCEPTION', 'STEALTH', 'SURVIVAL'
            ],
            armor_proficiency=['LIGHT', 'MEDIUM', 'SHIELD'],
            weapon_proficiency=['SIMPLE', 'MARTIAL'],
            equipment_options=equipment_options,
            equipment=equipment,
            specialization=None,
            specializations_features=self.specializations_features,
            starting_wealth=starting_wealth,
            magical_ability=MagicAbilities(
                has_magic=False,
                magical_ability='WIS',
                spells_known=self.spells_known[1],
                highest_spell_level=5,
                spell_slots=self.spells_slots,
                spell_save_dc=8+proficiency+abilities.score('WIS'),
                spell_attack_modifier=proficiency+abilities.score('WIS'),
                spell_list='RANGER',

            )
        )


class Rogue(Class):
    specialization_level = 3
    all_features = {
        1: ['EXPERTISE', 'SNEAK ATTACK', 'THIEVES\' CANT'],
        2: ['CUNNING ACTION'],
        3: ['ROGUISH ARCHETYPE'],
        4: [],
        5: ['UNCANNY DODGE'],
        6: ['EXPERTISE'],
        7: ['EVASION'],
        8: [],
        9: [],
        10: [],
        11: ['RELIABLE TALENT'],
        12: [],
        13: [],
        14: ['BLINDSENSE'],
        15: ['SLIPPERY MIND'],
        16: [],
        17: [],
        18: ['ELUSIVE'],
        19: [],
        20: ['STROKE OF LUCK']
    }
    specializations_features = {
        'THIEF': {
            3: ['FAST HANDS', 'SECOND-STORY WORK'],
            9: ['SUPREME SNEAK'],
            13: ['USE MAGIC DEVICE'],
            17: ['THIEF\'S REFLEXES']
        },
        'ASSASSIN': {
            3: ['BONUS PROFICIENCIES', 'ASSASSINATE'],
            9: ['INFILTRATION EXPERTISE'],
            13: ['IMPOSTOR'],
            17: ['DEATH STRIKE'],
        },
        'ARCANE TRICKSTER': {
            3: ['SPELLCASTING', 'MAGE HAND LEGERDEMAIN'],
            9: ['MAGICAL AMBUSH'],
            13: ['VERSATILE TRICKSTER'],
            17: ['SPELL THIEF']
        }
    }
    cantrips_known = {
        1: 0, 2: 0, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 1, 11: 0,
        12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0
    }
    spells_known = {
        1: 0, 2: 0, 3: 3, 4: 1, 5: 0, 6: 0, 7: 1, 8: 1, 9: 0, 10: 1, 11: 1,
        12: 0, 13: 1, 14: 1, 15: 0, 16: 1, 17: 0, 18: 0, 19: 1, 20: 1
    }
    spells_slots = {
        1: {1: 0, 2: 0, 3: 0, 4: 0},
        2: {1: 0, 2: 0, 3: 0, 4: 0},
        3: {1: 2, 2: 0, 3: 0, 4: 0},
        4: {1: 3, 2: 0, 3: 0, 4: 0},
        5: {1: 3, 2: 0, 3: 0, 4: 0},
        6: {1: 3, 2: 0, 3: 0, 4: 0},
        7: {1: 4, 2: 2, 3: 0, 4: 0},
        8: {1: 4, 2: 2, 3: 0, 4: 0},
        9: {1: 4, 2: 2, 3: 0, 4: 0},
        10: {1: 4, 2: 3, 3: 0, 4: 0},
        11: {1: 4, 2: 3, 3: 0, 4: 0},
        12: {1: 4, 2: 3, 3: 0, 4: 0},
        13: {1: 4, 2: 3, 3: 2, 4: 0},
        14: {1: 4, 2: 3, 3: 2, 4: 0},
        15: {1: 4, 2: 3, 3: 2, 4: 0},
        16: {1: 4, 2: 3, 3: 3, 4: 0},
        17: {1: 4, 2: 3, 3: 3, 4: 0},
        18: {1: 4, 2: 3, 3: 3, 4: 0},
        19: {1: 4, 2: 3, 3: 3, 4: 1},
        20: {1: 4, 2: 3, 3: 3, 4: 1}
    }

    def __init__(
            self,
            abilities,
            level,
            equipment_options,
            equipment,
            starting_wealth
    ):
        proficiency = super().proficiency_by_level[level]

        super().__init__(
            name='ROGUE',
            hit_die=Dice(maximum=8),
            specialization_level=self.specialization_level,
            level=level,
            all_features=self.all_features,
            proficiency=proficiency,
            saving_throw_proficiency=['DEX', 'INT'],
            number_skills=4,
            possible_skills=[
                'ACROBATICS', 'ATHLETICS', 'DECEPTION', 'INSIGHT',
                'INTIMIDATION', 'INVESTIGATION', 'PERCEPTION', 'PERFORMANCE',
                'PERSUASION', 'SLEIGHT OF HAND', 'STEALTH'
            ],
            armor_proficiency=['LIGHT'],
            weapon_proficiency=[
                'SIMPLE',
                'HAND CROSSBOW',
                'LONGSWORD',
                'RAPIER',
                'SHORTSWORD'
            ],
            tools_proficiency=['THIEVES\' TOOLS'],
            equipment_options=equipment_options,
            equipment=equipment,
            specialization=None,
            specializations_features=self.specializations_features,
            starting_wealth=starting_wealth,
            magical_ability=MagicAbilities(
                has_magic=False,
                magical_ability='INT',
                spells_known=self.spells_known[1],
                cantrips_known=self.cantrips_known[1],
                highest_spell_level=4,
                cantrips=['MAGE HAND', ],
                spell_slots_by_level=self.spells_slots,
                spell_slots=self.spells_slots[1],
                spell_save_dc=8+proficiency+abilities.score('INT'),
                spell_attack_modifier=proficiency+abilities.score('INT'),
                spell_list='WIZARD'
            )
        )


class Sorcerer(Class):
    all_features = {
        1: ['SPELLCASTING', 'SORCEROUS ORIGIN'],
        2: ['FONT OF MAGIC'],
        3: ['METAMAGIC'],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: ['METAMAGIC'],
        11: [],
        12: [],
        13: [],
        14: [],
        15: [],
        16: [],
        17: ['METAMAGIC'],
        18: [],
        19: [],
        20: ['SORCEROUS RESTORATION']
    }
    cantrips_known = {
        1: 4, 2: 0, 3: 0, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 1, 11: 0,
        12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0
    }
    spells_known = {
        1: 2, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1,
        11: 1, 12: 0, 13: 1, 14: 0, 15: 1, 16: 0, 17: 1, 18: 0, 19: 0, 20: 0
    }
    spells_slots = {
        1: {1: 2, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        2: {1: 3, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        3: {1: 4, 2: 3, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        4: {1: 4, 2: 3, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        5: {1: 4, 2: 3, 3: 2, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        6: {1: 4, 2: 3, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        7: {1: 4, 2: 3, 3: 3, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        8: {1: 4, 2: 3, 3: 3, 4: 2, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        9: {1: 4, 2: 3, 3: 3, 4: 3, 5: 1, 6: 0, 7: 0, 8: 0, 9: 0},
        10: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 0, 7: 0, 8: 0, 9: 0},
        11: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 0, 9: 0},
        12: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 0, 9: 0},
        13: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 0, 9: 0},
        14: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 0, 9: 0},
        15: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 0},
        16: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 0},
        17: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1},
        18: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 1, 7: 1, 8: 1, 9: 1},
        19: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 1, 8: 1, 9: 1},
        20: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 2, 8: 1, 9: 1}
    }
    specializations_features = {
        'DRACONIC BLOODLINE': {
            1: [
                {'DRAGON ANCESTOR': [
                    'BLACK - ACID',
                    'BLUE - LIGHTNING',
                    'BRASS - FIRE',
                    'BRONZE - LIGHTNING',
                    'COPPER - ACID',
                    'GOLD - FIRE',
                    'GREEN - POISON',
                    'RED - FIRE',
                    'SILVER - COLD',
                    'WHITE - COLD',
                ]},
                'DRACONIC RESILIENCE'],
            6: ['ELEMENTAL AFFINITY'],
            14: ['DRAGON WINGS'],
            18: ['DRACONIC PRESENCE']
        },
        'WILD MAGIC': {
            1: ['WILD MAGIC SURGE', 'TIDES OF CHAOS'],
            6: ['BEND LUCK'],
            14: ['CONTROLLED CHAOS'],
            18: ['SPELL BOMBARDMENT']
        }
    }

    def __init__(
            self,
            abilities,
            level,
            equipment,
            equipment_options,
            starting_wealth
    ):
        specialization_level = 1
        proficiency = super().proficiency_by_level[level]

        super().__init__(
            name='SORCERER',
            hit_die=Dice(maximum=6),
            specialization_level=specialization_level,
            level=level,
            all_features=self.all_features,
            proficiency=proficiency,
            saving_throw_proficiency=['CON', 'CHA'],
            number_skills=2,
            possible_skills=[
                'ARCANA', 'DECEPTION', 'INSIGHT', 'INTIMIDATION', 'PERSUASION',
                'RELIGION'
            ],
            weapon_proficiency=[
                'DAGGER', 'DART', 'SLING', 'QUARTERSTAFF', 'LIGHT CROSSBOW'
            ],
            equipment_options=equipment_options,
            equipment=equipment,
            specialization=None,
            specializations_features=self.specializations_features,
            starting_wealth=starting_wealth,
            magical_ability=MagicAbilities(
                has_magic=True,
                magical_ability='CHA',
                spells_known=self.spells_known[1],
                cantrips_known=self.cantrips_known[1],
                highest_spell_level=9,
                spell_slots_by_level=self.spells_slots,
                spell_slots=self.spells_slots[1],
                spell_save_dc=8+proficiency+abilities.score('CHA'),
                spell_attack_modifier=proficiency+abilities.score('CHA'),
                spell_list='SORCERER'
            )
        )


class Warlock(Class):
    all_features = {
        1: ['OTHERWORLDLY PATRON', 'PACT MAGIC'],
        2: ['ELDRITCH INVOCATIONS'],
        3: ['PACT BOON'],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],
        11: ['MYSTIC ARCANUM (6TH LEVEL)'],
        12: [],
        13: ['MYSTIC ARCANUM (7TH LEVEL)'],
        14: [],
        15: ['MYSTIC ARCANUM (8TH LEVEL)'],
        16: [],
        17: ['MYSTIC ARCANUM (9TH LEVEL)'],
        18: [],
        19: [],
        20: ['ELDRITCH MASTER']
    }
    cantrips_known = {
        1: 2, 2: 0, 3: 0, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 1, 11: 0,
        12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0
    }
    spells_known = {
        1: 2, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 0,
        11: 1, 12: 0, 13: 1, 14: 0, 15: 1, 16: 0, 17: 1, 18: 0, 19: 1, 20: 0,
    }
    spells_slots = {
        1: {1: 1, 2: 0, 3: 0, 4: 0, 5: 0},
        2: {1: 2, 2: 0, 3: 0, 4: 0, 5: 0},
        3: {1: 0, 2: 2, 3: 0, 4: 0, 5: 0},
        4: {1: 0, 2: 2, 3: 0, 4: 0, 5: 0},
        5: {1: 0, 2: 0, 3: 2, 4: 0, 5: 0},
        6: {1: 0, 2: 0, 3: 2, 4: 0, 5: 0},
        7: {1: 0, 2: 0, 3: 0, 4: 2, 5: 0},
        8: {1: 0, 2: 0, 3: 0, 4: 2, 5: 0},
        9: {1: 0, 2: 0, 3: 0, 4: 0, 5: 2},
        10: {1: 0, 2: 0, 3: 0, 4: 0, 5: 2},
        11: {1: 0, 2: 0, 3: 0, 4: 0, 5: 3},
        12: {1: 0, 2: 0, 3: 0, 4: 0, 5: 3},
        13: {1: 0, 2: 0, 3: 0, 4: 0, 5: 3},
        14: {1: 0, 2: 0, 3: 0, 4: 0, 5: 3},
        15: {1: 0, 2: 0, 3: 0, 4: 0, 5: 3},
        16: {1: 0, 2: 0, 3: 0, 4: 0, 5: 3},
        17: {1: 0, 2: 0, 3: 0, 4: 0, 5: 4},
        18: {1: 0, 2: 0, 3: 0, 4: 0, 5: 4},
        19: {1: 0, 2: 0, 3: 0, 4: 0, 5: 4},
        20: {1: 0, 2: 0, 3: 0, 4: 0, 5: 4},
    }
    specializations_features = {
        'ARCHFEY': {
            1: ['FEY PRESENCE'],
            6: ['MISTY ESCAPE'],
            10: ['BEGUILING DEFENSES'],
            14: ['DARK DELIRIUM']
        },
        'THE FIEND': {
            1: ['DARK ONE\'S BLESSING'],
            6: ['DARK ONE\'S OWN LUCK'],
            10: ['FIENDISH RESILIENCE'],
            14: ['HURL THROUGH HELL']
        },
        'THE GREAT OLD ONE': {
            1: ['AWAKENED MIND'],
            6: ['ENTROPIC WARD'],
            10: ['THOUGHT SHIELD'],
            14: ['CREATE THRALL'],
        }
    }

    def __init__(
            self,
            abilities,
            level,
            equipment,
            equipment_options,
            starting_wealth
    ):
        proficiency = super().proficiency_by_level[level]

        super().__init__(
            name='WARLOCK',
            hit_die=Dice(maximum=8),
            all_features=self.all_features,
            specialization_level=1,
            level=level,
            proficiency=proficiency,
            saving_throw_proficiency=['WIS', 'CHA'],
            number_skills=2,
            possible_skills=[
                'ARCANA', 'DECEPTION', 'HISTORY', 'INTIMIDATION',
                'INVESTIGATION', 'NATURE', 'RELIGION'
            ],
            armor_proficiency=['LIGHT'],
            weapon_proficiency=['SIMPLE'],
            equipment=equipment,
            equipment_options=equipment_options,
            specialization=None,
            specializations_features=self.specializations_features,
            starting_wealth=starting_wealth,
            magical_ability=MagicAbilities(
                has_magic=True,
                magical_ability='CHA',
                spells_known=self.spells_known[1],
                cantrips_known=self.cantrips_known[1],
                highest_spell_level=5,
                spell_slots_by_level=self.spells_slots,
                spell_slots=self.spells_slots[1],
                spell_save_dc=8+proficiency+abilities.score('CHA'),
                spell_attack_modifier=proficiency+abilities.score('CHA'),
                spell_list='WARLOCK'
            )
        )


class Wizard(Class):
    all_features = {
        1: ['SPELLCASTING', 'ARCANE RECOVERY'],
        2: ['ARCANE TRADITION'],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],
        11: [],
        12: [],
        13: [],
        14: [],
        15: [],
        16: [],
        17: [],
        18: ['SPELL MASTERY'],
        19: [],
        20: ['SIGNATURE SPELL'],
    }
    cantrips_known = {
        1: 3, 2: 0, 3: 0, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 1, 11: 0,
        12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0
    }
    spells_known = {
        1: 6, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 2, 11: 2,
        12: 2, 13: 2, 14: 2, 15: 2, 16: 2, 17: 2, 18: 2, 19: 2, 20: 2
    }
    spells_slots = {
        1: {1: 2, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        2: {1: 3, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        3: {1: 4, 2: 2, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        4: {1: 4, 2: 3, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        5: {1: 4, 2: 3, 3: 2, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        6: {1: 4, 2: 3, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        7: {1: 4, 2: 3, 3: 3, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        8: {1: 4, 2: 3, 3: 3, 4: 2, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        9: {1: 4, 2: 3, 3: 3, 4: 3, 5: 1, 6: 0, 7: 0, 8: 0, 9: 0},
        10: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 0, 7: 0, 8: 0, 9: 0},
        11: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 0, 9: 0},
        12: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 0, 9: 0},
        13: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 0, 9: 0},
        14: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 0, 9: 0},
        15: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 0},
        16: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 0},
        17: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1},
        18: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 1, 7: 1, 8: 1, 9: 1},
        19: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 1, 8: 1, 9: 1},
        20: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 2, 8: 1, 9: 1},
    }
    specializations_features = {
        'SCHOOL OF ABJURATION': {
            2: ['ABJURATION SAVANT', 'ARCANE WARD'],
            6: ['PROJECTED WARD'],
            10: ['IMPROVED ABJURATION'],
            14: ['SPELL RESISTANCE']
        },
        'SCHOOL OF CONJURATION': {
            2: ['CONJURATION SAVANT', 'MINOR CONJURATION'],
            6: ['BENIGN TRANSPORTATION'],
            10: ['FOCUSED CONJURATION'],
            14: ['DURABLE SUMMONS'],
        },
        'SCHOOL OF DIVINATION': {
            2: ['DIVINATION SAVANT', 'PORTENT'],
            6: ['EXPERT DIVINATION'],
            10: ['THE THIRD EYE'],
            14: ['GREATER PORTENT']
        },
        'SCHOOL OF ENCHANTMENT': {
            2: ['ENCHANTMENT SAVANT', 'HYPNOTIC GAZE'],
            6: ['INSTINCTIVE CHARM'],
            10: ['SPLIT ENCHANTMENT'],
            14: ['ALTER MEMORIES']
        },
        'SCHOOL OF EVOCATION': {
            2: ['EVOCATION SAVANT', 'SCULPT SPELLS'],
            6: ['POTENT CANTRIP'],
            10: ['EMPOWERED EVOCATION'],
            14: ['OVERCHANNEL']
        },
        'SCHOOL OF ILLUSION': {
            2: ['ILLUSION SAVANT', 'IMPROVED MINOR ILLUSION'],
            6: ['MALLEABLE ILLUSIONS'],
            10: ['ILLUSORY SELF'],
            14: ['ILLUSORY REALITY']
        },
        'SCHOOL OF NECROMANCY': {
            2: ['NECROMANCY SAVANT', 'GRIM HARVEST'],
            6: ['UNDEAD THRALLS'],
            10: ['INURED TO UNDEATH'],
            14: ['COMMAND UNDEAD'],
        },
        'SCHOOL OF TRANSMUTATION': {
            2: ['TRANSMUTATION SAVANT', 'MINOR ALCHEMY'],
            6: ['TRANSMUTER\'S STONE'],
            10: ['SHAPECHANGER'],
            14: ['MASTER TRANSMUTER']
        }
    }

    @staticmethod
    def def_num_prep_spells(score, level):
        number = score + level

        if number > 1:
            return number
        else:
            return 1

    def __init__(
            self,
            abilities,
            level,
            equipment,
            equipment_options,
            starting_wealth
    ):
        proficiency = super().proficiency_by_level[level]

        super().__init__(
            name='WIZARD',
            hit_die=Dice(maximum=6),
            all_features=self.all_features,
            specialization_level=2,
            level=level,
            proficiency=proficiency,
            saving_throw_proficiency=['INT', 'WIS'],
            number_skills=2,
            possible_skills=[
                'ARCANA', 'HISTORY', 'INSIGHT', 'INVESTIGATION', 'MEDICINE',
                'RELIGION'
            ],
            weapon_proficiency=[
                'DAGGER',
                'DART',
                'SLINGS',
                'QUARTERSTAFF',
                'LIGHT CROSSBOW'
            ],
            equipment_options=equipment_options,
            equipment=equipment,
            specialization=None,
            specializations_features=self.specializations_features,
            starting_wealth=starting_wealth,
            magical_ability=MagicAbilities(
                has_magic=True,
                magical_ability='INT',
                spells_by_level=self.spells_known,
                cantrips_by_level=self.cantrips_known,
                spells_known=self.spells_known[1],
                cantrips_known=self.cantrips_known[1],
                highest_spell_level=9,
                spell_slots_by_level=self.spells_slots,
                spell_slots=self.spells_slots[1],
                spell_save_dc=8+proficiency+abilities.score('INT'),
                spell_attack_modifier=proficiency+abilities.score('INT'),
                prepare_spells=True,
                def_num_prep_spells=self.def_num_prep_spells,
                number_prepared_spells=self.def_num_prep_spells(
                    score=abilities.score('INT'),
                    level=level
                ),
                spell_list='WIZARD',
            )
            )


class Background:
    def __init__(
            self,
            name,
            skills,
            equipment,
            feature,
            possible_traits,
            possible_ideals,
            possible_bonds,
            possible_flaws,
            feature_options=None,
            number_tools=0,
            tools_options=None,
            personality_trait=None,
            ideal=None,
            bond=None,
            flaw=None,
            wealth=0,
            variant=False,
            equipment_options=None,
            languages=None,
            tools_proficiency=None,
            background_speciality=None,
            possible_specialities=None
    ):
        if languages is None:
            languages = 0

        if tools_proficiency is None:
            tools_proficiency = []

        if possible_specialities is None:
            possible_specialities = []

        if equipment_options is None:
            equipment_options = []

        if tools_options is None:
            tools_options = []

        if feature_options is None:
            feature_options = []

        self.name = name
        self.skills = skills
        self.languages = languages
        self.equipment = equipment
        self.equipment_options = equipment_options
        self.background_speciality = background_speciality
        self.feature = feature
        self.feature_options = feature_options
        self.personality_trait = personality_trait
        self.ideal = ideal
        self.bond = bond
        self.flaw = flaw
        self.variant = variant
        self.wealth = wealth
        self.tools_proficiency = tools_proficiency
        self.number_tools = number_tools
        self.tools_options = tools_options
        self.possible_specialities = possible_specialities
        self.possible_traits = possible_traits
        self.possible_ideals = possible_ideals
        self.possible_bonds = possible_bonds
        self.possible_flaws = possible_flaws


class Acolyte(Background):
    def __init__(
            self,
            equipment,
            equipment_options,
    ):
        possible_traits = [
            'I idolize a particular hero of my faith and constantly '
            'refer to that person\'s deeds and example',
            'I can find common ground between the fiercest enemies, '
            'empathizing with them and always working toward peace',
            'I see omens in every event and action. The gods try to '
            'speak to us, we just need to listen',
            'Nothing can shake my optimistic attitude',
            'I quote (or misquote) sacred texts and proverbs in almost '
            'every situation',
            'I am tolerant (or intolerant) of other faiths and respect '
            '(or condemn) the worship of other gods.',
            'I\'ve enjoyed fine food, drink, and high society among my '
            'temple\'s elite. Rough living grates on me.',
            "I've spent so long in the temple that I've little practical "
            "experience dealing with people in the outside world.",
        ]
        possible_ideals = [
            [
                (
                    'Tradition. The ancient traditions of worship and '
                    'sacrifice must be preserved and upheld.'
                ),
                'LAWFUL'
            ],
            [
                (
                    'Charity. I always try to help those in need, no matter '
                    'what the personal cost.'
                ),
                'GOOD'
            ],
            [
                (
                    'Change. We must help bring about the changes the gods '
                    'are constantly working in the world'
                ),
                'CHAOTIC'
            ],
            [
                (
                    'Power. I hope to one day rise to the top of my faith\'s '
                    'religious hierarchy.'
                ),
                'LAWFUL'
            ],
            [
                (
                    'Faith. I trust that my deity will guide my actions. I '
                    'have faith that if I work hard, things will go well.'
                ),
                'LAWFUL'
            ],
            [
                (
                    'Aspiration. I seek to prove myself worthy of my god\'s '
                    'favor by matching my actions against his or her teachings'
                ),
                'ANY'
            ],
        ]
        possible_bonds = [
            (
                'I would die to recover an ancient relic of my faith that '
                'was lost long ago.'
            ),
            (
                'I will someday get revenge on the corrupt temple hierarchy '
                'who branded me a heretic.'
            ),
            (
                'I owe my life to the priest who took me in when my parents '
                'died.'
            ),
            'Everything I do is for the common people.',
            'I will do anything to protect the temple where I served.',
            'I seek to preserve a sacred text that my enemies consider '
            'heretical and seek to destroy',
        ]
        possible_flaws = [
            'I judge harshly, and myself even more severely',
            (
                'I put too much trust in those who wield power within my '
                'temple\'s hierarchy.'
            ),
            (
                'My piety sometimes leads me to blindly trust those that '
                'profess faith in my god.'
            ),
            'I am inflexible in my thinking.',
            'I am suspicious of strangers and expect the worst of them.',
            'Once I pick a goal, I become obsessed with it to be detriment '
            'of everything else in my life.',
        ]

        super().__init__(
            name='ACOLYTE',
            skills=['INSIGHT', 'RELIGION'],
            equipment=equipment,
            equipment_options=equipment_options,
            feature=['SHELTER OF THE FAITHFUL'],
            wealth=15,
            languages=1,
            possible_traits=possible_traits,
            possible_ideals=possible_ideals,
            possible_bonds=possible_bonds,
            possible_flaws=possible_flaws,
        )


class Charlatan(Background):
    def __init__(
            self,
            equipment,
            equipment_options,
    ):
        possible_specialities = [
            'I cheat at games of chance',
            'I shave coins or forge documents',
            'I insinuate myself intro people\'s lives to prey on their '
            'weakness and secure their fortunes',
            'I put on new identities like clothes',
            'I run sleight-of-hand cons on street corners.',
            'I convince people that worthless junk is worth their '
            'hard-earned money'
        ]
        possible_traits = [
            'I fall in and out of love easily, and am always pursuing someone',
            'I have a joke for every occasion, especially occasions where '
            'humor is inappropriate',
            'Flattery is my preferred trick for getting what I want',
            'I\'m a born gambler who can\'t resist taking a risk for a '
            'potential payoff',
            'I lie about almost everything, even when there\'s no good '
            'reason to',
            'Sarcasm and insults are my weapon of choice',
            'I keep multiple holy symbols on me and invoke whatever deity '
            'might come in useful at any given moment.',
            'I pocket anything I see that might have some value.'
        ]
        possible_ideals = [
            [
                'Independence. I am a free spirit-no one tells me what to do',
                'CHAOTIC'
            ],
            [
                (
                    'Fairness. I never target people who can\'t afford to '
                    'lose a few coins'
                ),
                'LAWFUL'
            ],
            [
                (
                    'Charity. I distribute the money I acquire to the people '
                    'who really need it.'
                ),
                'GOOD'
            ],
            ['Creativity. I never run the same con twice', 'CHAOTIC'],
            [
                (
                    'Friendship. Material goods come and go. Bonds of '
                    'friendship last forever.'
                ),
                'GOOD'
            ],
            [
                'Aspiration. I\'m determined to make something of myself',
                'ANY'
            ]
        ]
        possible_bonds = [
            'I fleeced the wrong person and must work to ensure that this '
            'individual never crosses paths with me or those I care about',
            'I owe everything to my mentor - a horrible person who\'s '
            'probably rotting in jail somewhere',
            "Somewhere out there, I have a child who doesn't know me. "
            'I\'m making the world better for him or her',
            'I come from a noble family, and one day I\'ll reclaim my '
            'lands and title from those who stole them from me',
            'A powerful person killed someone I love. Some day soon, '
            'I\'ll have my revenge',
            "I swindled and ruined a person who didn't deserve it. I seek "
            'to atone for my misdeeds but might never be able to forgive '
            'myself.'
        ]
        possible_flaws = [
            'I can\'t resist a pretty face.',
            'I\'m always in debt. I spend my ill-gotten gains on decadent '
            'luxuries faster than I bring them in.',
            'I\'m convinced that no one could ever fool '
            'me the way I fool others.',
            'I\'m too greedy for my own good. I can\'t resist taking a risk '
            'if there\'s money involved.',
            "I can't resist swindling people who are more powerful than me",
            "I hate to admit it and will hate myself for it, but I'll run "
            "and preserve my own hide if the going gets tough."
        ]

        super().__init__(
            name='CHARLATAN',
            skills=['DECEPTION', 'SLEIGHT OF HAND'],
            equipment=equipment,
            equipment_options=equipment_options,
            feature=['FALSE IDENTITY'],
            wealth=15,
            tools_proficiency=['DISGUISE KIT', 'FORGERY KIT'],
            possible_specialities=possible_specialities,
            possible_traits=possible_traits,
            possible_ideals=possible_ideals,
            possible_bonds=possible_bonds,
            possible_flaws=possible_flaws,
        )


class Criminal(Background):
    def __init__(
            self,
            equipment,
            variant,
    ):
        if variant:
            name = 'SPY'
        else:
            name = 'CRIMINAL'

        possible_specialities = [
            'BLACKMAILER',
            'BURGLAR',
            'ENFORCER',
            'FENCE',
            'HIGHWAY ROBBER',
            'HIRED KILLER',
            'PICKPOCKET',
            'SMUGGLER'
        ]
        possible_traits = [
            'I always have a plan for what to do when things go wrong',
            'I am always calm, no matter what the situation. I never '
            'raised my voice or let my emotions control me',
            'The first thing I do in a new place is note the locations of '
            'everything valuable - or where suck things could be hidden',
            'I would rather make a new friend than a new enemy',
            'I am incredibly slow to trust. Those who seem the fairest '
            'often have the most to hide',
            'I don\'t pay attention to the risks in a situation. '
            'Never tell me the odds',
            'The best way to get me to do something '
            'is to tell me I can\'t do it',
            'I blow up at the slightest insult'
        ]
        possible_ideals = [
            ['Honor. I don\'t steal from others in the trade', 'LAWFUL'],
            [
                'Freedom. Chains are meant to be broken, '
                'as are those who would forge them.',
                'CHAOTIC'
            ],
            [
                'Charity. I steal from the wealthy so that '
                'I can help people in need',
                'GOOD'
            ],
            ['Greed. I will do whatever it takes to become wealthy', 'EVIL'],
            [
                'People. I\'m loyal to my friends, not to any ideals, and '
                'everyone else can take a trip down the Styx for all I care.',
                'NEUTRAL'
            ],
            ['Redemption. There\'s a spark of good in everyone.', 'GOOD']
        ]
        possible_bonds = [
            'I\'m trying to pay off an old debt '
            'I owe to a generous benefactor.',
            'My ill-gotten gains go to support my family.',
            'Something important was taken from me, '
            'and I aim to steal it back.',
            'I will become the greatest thief that ever lived.',
            'I\'m guilty of a terrible crime. '
            'I hope I can redeem myself for it.',
            'Someone I loved died because of a mistake I made. '
            'That will never happen again.'
        ]
        possible_flaws = [
            'When I see something valuable, I can\'t think about anything '
            'but how to steal it.',
            'When faced with a choice between money and my friends, '
            'I usually choose the money.',
            'If there\'s a plan, I\'ll forget it. If I don\'t forget it, '
            'I\'ll ignore it.',
            'I have a “tell” that reveals when I\'m lying.',
            'I turn tail and run when things look bad.',
            'An innocent person is in prison for a crime that I committed. '
            'I\'m okay with that.'
        ]
        tools_options = [
            'DICE SET', 'DRAGONCHESS SET',
            'PLAYING CARD SET', 'THREE-DRAGON ANTE SET'
        ]

        super().__init__(
            name=name,
            skills=['DECEPTION', 'STEALTH'],
            equipment=equipment,
            feature=['CRIMINAL CONTACT'],
            wealth=15,
            variant=variant,
            number_tools=1,
            tools_options=tools_options,
            tools_proficiency=['THIEVES\' TOOLS'],
            possible_specialities=possible_specialities,
            possible_traits=possible_traits,
            possible_ideals=possible_ideals,
            possible_bonds=possible_bonds,
            possible_flaws=possible_flaws,
        )


class Entertainer(Background):
    def __init__(
            self,
            equipment,
            equipment_options,
            variant,
    ):
        if variant:
            name = 'GLADIATOR'
        else:
            name = 'ENTERTAINER'

        possible_specialities = [
            'ACTOR',
            'DANCER',
            'FIRE-EATER',
            'JESTER',
            'JUGGLER',
            'INSTRUMENTALIST',
            'POET',
            'SINGER',
            'STORYTELLER',
            'TUMBLER'
        ]
        possible_traits = [
            'I know a story relevant to almost every situation.',
            'Whenever I come to a new place, I collect local rumors and '
            'spread gossip.',
            'I\'m a hopeless romantic, always searching for that '
            '"special someone."',
            'Nobody stays angry at me or around me for long, since '
            'I can defuse any amount of tension.',
            'I love a good insult, even one directed at me.',
            'I get bitter if I\'m not the center of attention.',
            'I\'ll settle for nothing less than perfection.',
            'I change my mood or my mind as quickly as I change key in a '
            'song.',
        ]
        possible_ideals = [
            [
                'Beauty. When I perform, I make the world better than it was.',
                'GOOD'
            ],
            [
                'Tradition. The stories, legends, and songs of the past must '
                'never be forgotten, for they teach us who we are',
                'LAWFUL'
            ],
            [
                'Creativity. The world is in need of new ideas and bold '
                'action',
                'CHAOTIC'
            ],
            ['Greed. I\'m only in it for the money and fame.', 'EVIL'],
            [
                'People. I like seeing the smiles on people\'s faces when I '
                'perform. That\'s all that matters.',
                'NEUTRAL'
            ],
            [
                'Honesty. Art should reflect the soul; it should come from '
                'within and reveal who we really are.',
                'ANY'
            ]
        ]
        possible_bonds = [
            'My instrument is my most treasured possession, and it '
            'reminds me of someone I love.',
            'Someone stole my precious instrument, and someday I\'ll get '
            'it back',
            'I want to be famous, whatever it takes.',
            'I idolize a hero of the old tales and measure my deeds '
            'against that person\'s.',
            'I will do anything to prove myself superior to my hated rival',
            'I would do anything for the other members of my old troupe'
        ]
        possible_flaws = [
            'I\'ll do anything to win fame and renown.',
            'I\'m a sucker for a pretty face',
            'A scandal prevents me from ever going home again. That kind '
            'of troubles seems to follow me around.',
            'I once satirized a noble who still wants my head. It was a '
            'mistake that I will likely repeat.',
            'I have trouble keeping my true feelings hidden. My sharp '
            'tongue lands me in trouble',
            'Despite my best efforts, I am unreliable to my friends.'
        ]

        super().__init__(
            name=name,
            skills=['ACROBATICS', 'PERFORMANCE'],
            equipment=equipment,
            equipment_options=equipment_options,
            feature=['BY POPULAR DEMAND'],
            wealth=15,
            variant=variant,
            tools_proficiency=['DISGUISE KIT'],
            number_tools=1,
            tools_options=[
                'BAGPIPES', 'DRUM', 'DULCIMER', 'FLUTE', 'LUTE', 'LYRE', 'HORN',
                'PAN FLUTE', 'SHAWM', 'VIOL',
            ],
            possible_specialities=possible_specialities,
            possible_traits=possible_traits,
            possible_ideals=possible_ideals,
            possible_bonds=possible_bonds,
            possible_flaws=possible_flaws,
        )


class FolkHero(Background):
    def __init__(
            self,
            equipment,
            equipment_options,
    ):
        possible_specialities = [
            'I stood up to a tyrant\'s agents',
            'I saved people during a natural disaster',
            'I stood alone against a terrible monster',
            'I stole from a corrupt merchant to help the poor',
            'I led a militia to fight off an invading army',
            'I broke into a tyrant\'s castle and stole weapons to arm the '
            'people',
            'I trained the peasantry to use farm implements as weapons '
            'against a tyrant\'s soldiers',
            'A lord rescinded an unpopular decree after I led a symbolic '
            'act of protect against it',
            'A celestial, a fey, or similar creature gave me a blessing '
            'or revealed my secret origin.',
            'Recruited into a lord\'s army, I rose to leadership and '
            'was commended for my heroism'
        ]
        possible_traits = [
            'I judge people by their actions, not their words.',
            'If someone is in trouble, I\'m always ready to lend help.',
            'When I set my mind to something, I follow through no matter '
            'what gets in my way.',
            'I have a strong sense of fair play and always try to find '
            'the most equitable solution to arguments.',
            'I\'m confident in my own abilities and do what I can to '
            'instill confidence in others.',
            'Thinking is for other people. I prefer action.',
            'I misuse long words in an attempt to sound smarter.',
            'I get bored easily. When am I going to get on with my destiny?'
        ]
        possible_ideals = [
            [
                'Respect. People deserve to be treated with dignity and '
                'respect.',
                'GOOD'
            ],
            [
                'Fairness. No one should get preferential treatment before '
                'the law, and no one is above the law.',
                'LAWFUL'
            ],
            [
                'Freedom. Tyrants must not be allowed to oppress the people',
                'CHAOTIC'
            ],
            [
                'Might. If I become strong, I can take what I want - what '
                'I deserve.',
                'EVIL'
            ],
            [
                'Sincerity. There\'s no good in pretending to be something '
                'I\'m not.',
                'NEUTRAL'
            ],
            [
                'Destiny. Nothing and no one can steer me away from my higher '
                'calling',
                'ANY'
            ]
        ]
        possible_bonds = [
            'I have a family, but I have no idea where they are. One day, '
            'I hope to see them again.',
            'I worked the land, I love the land, and I will protect the '
            'land',
            'A proud noble once gave me a horrible beating, and I will '
            'take my revenge on any bully I encounter',
            'My tools are symbols of my past life, and I carry them so '
            'that I will never forget my roots.',
            'I protect those who cannot protect themselves.',
            'I wish my childhood sweetheart had come with me to pursue '
            'my destiny.'
        ]
        possible_flaws = [
            'The tyrant who rules my land will stop at nothing '
            'to see me killed',
            'I\'m convinced of the significance of my destiny, and blind '
            'to my shortcomings and the risk of failure',
            'The people who knew me when I was young know my shameful '
            'secret, so I can never go home again',
            'I have a weakness for the vices of the city, especially '
            'hard drink',
            'Secretly, I believe that things would be better if I were a '
            'tyrant lording over the land',
            'I have trouble trusting in my allies'
        ]

        super().__init__(
            name='FOLK HERO',
            skills=['ANIMAL HANDLING', 'SURVIVAL'],
            equipment=equipment,
            equipment_options=equipment_options,
            feature=['RUSTIC HOSPITALITY'],
            wealth=10,
            tools_proficiency=['VEHICLES (LAND)'],
            number_tools=1,
            tools_options=[
                "ALCHEMIST'S SUPPLIES", "BREWER'S SUPPLIES", "CALLIGRAPHER'S "
                "SUPPLIES", "CARPENTER'S TOOLS", "CARTOGRAPHER'S TOOLS",
                "COBBLER'S TOOLS", "COOK'S UTENSILS", "GLASSBLOWER'S TOOLS",
                "JEWELER'S TOOLS", "LEATHERWORKER'S TOOLS", "MASON'S TOOLS",
                "PAINTER'S SUPPLIES", "POTTER'S TOOLS", "SMITH'S TOOLS",
                "TINKER'S TOOLS", "WEAVER'S TOOLS", "WOODCARVER'S TOOLS"
            ],
            possible_specialities=possible_specialities,
            possible_traits=possible_traits,
            possible_ideals=possible_ideals,
            possible_bonds=possible_bonds,
            possible_flaws=possible_flaws,
        )


class GuildArtisan(Background):
    def __init__(
            self,
            equipment_options,
            equipment,
            variant,
    ):
        if variant:
            name = 'GUILD MERCHANT'
        else:
            name = 'GUILD ARTISAN'

        possible_specialities = [
            'Alchemists and apothecaries,',
            'Armorers, locksmiths, and finesmiths',
            'Brewers, distillers, and vintners',
            'Calligraphers, scribes, and scriveners',
            'Carpenters, roofers, and plasterers',
            'Cartographers, surveyors, and chart - makers',
            'Cobblers and shoemakers',
            'Cooks and bakers',
            'Glassblowers and glaziers',
            'Jewelers and gemcutters',
            'Leatherworkers, skinners, and tanners',
            'Masons and stonecutters',
            'Painters, limners, and sign - makers',
            'Potters and tile - makers',
            'Shipwrights and sailmakers',
            'Smiths and metal - forgers',
            'Tinkers, pewterers, and casters',
            'Wagon - makers and wheelwrights',
            'Weavers and dyers',
            'Woodcarvers, coopers, and bowyers',
        ]
        possible_traits = [
            'I believe that anything worth doing is worth doing right. I '
            'can\tt help it— I\tm a perfectionist.',
            'I\'m a snob who looks down on those who can\'t appreciate '
            'fine art.',
            'I always want to know how things work and what makes people '
            'tick.',
            'I\'m full of witty aphorisms and have a proverb for '
            'every occasion.',
            'I\'m rude to people who lack my commitment to hard work and '
            'fair play.',
            'I like to talk at length about my profession.',
            'I don\'t part with my money easily and will haggle tirelessly '
            'to get the best deal possible.',
            'I\'m well known for my work, and I want to make sure everyone '
            'appreciates it. I\'m always taken aback when people haven\'t '
            'heard of me.'
        ]
        possible_ideals = [
            [
                'Community. It is the duty of all civilized people to '
                'strengthen the bonds of community and the security of '
                'civilization.',
                'LAWFUL'
            ],
            [
                'Generosity. My talents were given to me so that I could use '
                'them to benefit the world.',
                'GOOD'
            ],
            [
                'Freedom. Everyone should be free to pursue his or her own '
                'livelihood.',
                'CHAOTIC'
            ],
            ['Greed. I\'m only in it for the money.', 'EVIL'],
            [
                'People. I\'m committed to the people I care about, not to '
                'ideals.',
                'NEUTRAL'
            ],
            [
                'Aspiration. I work hard to be the best there is at my craft.',
                'ANY'
            ]
        ]
        possible_bonds = [
            'The workshop where I learned my trade is the most important '
            'place in the world to me',
            'I created a great work for someone, and then found them '
            'unworthy to receive it. I\'m still looking for someone worthy',
            'I owe my guild a great debt for forging me into the person I '
            'am today',
            'I pursue wealth to secure someone\'s love',
            'One day I will return to my guild and prove that I am the '
            'greatest artisan of them all',
            'I will get revenge on the evil forces that destroyed my place '
            'of business and ruined my livelihood',
        ]
        possible_flaws = [
            'I\'ll do anything to get my hands on something rare or '
            'priceless.',
            'I\'m quick to assume that someone is trying to cheat me.',
            'No one must ever learn that I once stole money from guild '
            'coffers',
            'I\'m never satisfied with what I have - I always want more',
            'I would kill to acquire a noble title.',
            'I\'m horribly jealous of anyone who can outshine my '
            'handiwork. Everywhere I go, I\'m surrounded by rivals'
        ]
        tools_options = [
            "ALCHEMIST'S SUPPLIES",
            "BREWER'S SUPPLIES",
            "CALLIGRAPHER'S SUPPLIES",
            "CARPENTER'S TOOLS",
            "CARTOGRAPHER'S TOOLS",
            "COBBLER'S TOOLS",
            "COOK'S UTENSILS",
            "GLASSBOWER'S TOOLS",
            "JEWELER'S TOOLS",
            "LEATHERWORKER'S TOOLS",
            "MASON'S TOOLS",
            "PAINTER'S SUPPLIES",
            "POTTER'S TOOLS",
            "SMITH'S TOOLS",
            "TINKER'S TOOLS",
            "WEAVER'S TOOLS",
            "WOODCARVER'S TOOLS"
        ]

        super().__init__(
            name=name,
            skills=['INSIGHT', 'PERSUASION'],
            equipment=equipment,
            equipment_options=equipment_options,
            feature=['GUILD MEMBERSHIP'],
            wealth=15,
            variant=variant,
            languages=1,
            number_tools=1,
            tools_options=tools_options,
            possible_specialities=possible_specialities,
            possible_traits=possible_traits,
            possible_ideals=possible_ideals,
            possible_bonds=possible_bonds,
            possible_flaws=possible_flaws,
        )


class Hermit(Background):
    def __init__(
            self,
            equipment,
    ):
        possible_specialities = [
            'I war searching for spiritual enlightenment.',
            'I was partaking of communal living in accordance with the '
            'dictates of a religious order',
            "I was exiled for a crime I didn't commit",
            'I retreated from society after a life-altering event',
            'I needed a quiet place to work on my art, literature, music, '
            'or manifesto',
            'I needed to commune with nature, far from civilization',
            'I was the caretaker of an ancient ruin or relic',
            'I was a pilgrim in search of a person, place, or relic of '
            'spiritual significance',
        ]
        possible_traits = [
            'I\'ve been isolated for so long that I rarely speak, '
            'preferring gestures and the occasional grunt',
            'I am utterly serene, even in the face of disaster',
            'The leader of my community had something wise to say on every '
            'topic, and I am eager to share that wisdom.',
            'I feel tremendous empathy for all who suffer.',
            'I\'m oblivious to etiquette and social expectations',
            'I connect everything that happens to me to a grand, '
            'cosmic plan',
            'I often get lost in my own thoughts and contemplation, '
            'becoming oblivious to my surroundings',
            'I am working on a grand philosophical theory and love sharing '
            'my ideas',
        ]
        possible_ideals = [
            [
                (
                    'Greater good. My gifts are meant to be shared with all, '
                    'not used for my own benefit'
                ),
                'GOOD'
            ],
            [
                (
                    'Logic. Emotions must not cloud our sense of what is '
                    'right and true, or our logical thinking'
                ),
                'LAWFUL'
            ],
            [
                (
                    'Free Thinking. Inquiry and curiosity are the pillars of '
                    'progress'
                ),
                'CHAOTIC'
            ],
            [
                (
                    'Power. Solitude and contemplation are paths toward '
                    'mystical or magical power'
                ),
                'EVIL'
            ],
            [
                (
                    'Live and Let Live. Meddling in the affairs of others only '
                    'causes trouble'
                ),
                'NEUTRAL'
            ],
            [
                (
                    'Self-Knowledge. If you know yourself, there\'s nothing '
                    'left to know'
                ),
                'ANY'
            ]
        ]
        possible_bonds = [
            'Nothing is more important than the other members of my '
            'hermitage, order, or association.',
            'I entered seclusion to hide from the ones who might still be '
            'hunting me. I must someday confront them.',
            'I\'m still seeking the enlightenment I pursued in my '
            'seclusion, and it still eludes me.',
            'I entered seclusion because I loved someone I could not have.',
            'Should my discovery come to light, it could bring ruin to the '
            'world.',
            'My isolation gave me great insight into a great evil that '
            'only I can destroy.'
        ]
        possible_flaws = [
            'Now that I\'ve returned to the world, I enjoy its delights a '
            'little too much',
            'I harbor dark, bloodthirsty thoughts that my isolation and '
            'meditation failed to quell.',
            'I am dogmatic in my thoughts and philosophy.',
            'I let my need to win arguments overshadow friendships and '
            'harmony',
            'I\'d risk too much to uncover a lost bit of knowledge',
            'I like keeping secrets and won\'t share them with anyone.'
        ]

        super().__init__(
            name='HERMIT',
            skills=['MEDICINE', 'RELIGION'],
            equipment=equipment,
            feature=['DISCOVERY'],
            wealth=5,
            languages=1,
            tools_proficiency=['HERBALISM KIT'],
            possible_specialities=possible_specialities,
            possible_traits=possible_traits,
            possible_ideals=possible_ideals,
            possible_bonds=possible_bonds,
            possible_flaws=possible_flaws,
        )


class Noble(Background):
    def __init__(
            self,
            equipment,
            variant,
    ):
        if variant:
            name = 'KNIGHT'
            feature = ['RETAINERS']
        else:
            name = 'NOBLE'
            feature = ['POSITION OF PRIVILEGE']

        personalities_options = [
            'My eloquent flattery makes everyone I talk to feel like the'
            ' most wonderful and important person in the world.',
            'The common folk love me for my kindness and generosity.',
            'No one could doubt by looking at my regal bearing that I am a '
            'cut above the unwashed masses.',
            'I take great pains to always look my best and follow the '
            'latest fashions.',
            'I don\'t like to get my hands dirty, and I won\'t be caught '
            'dead in unsuitable accommodations.',
            'Despite my noble birth, I do not place myself above other '
            'folk. We all have the same blood.',
            'My favor, once lost, is lost forever',
            'If you do me an injury, I will crush you, ruin your name, and '
            'salt your fields.'
        ]
        ideals_options = [
            [
                (
                    'Respect. Respect is due to me because of my position, '
                    'but all people regardless of station deserve to be '
                    'treated with dignity.'
                ),
                'GOOD'
            ],
            [
                (
                    "Responsibility. It's my duty to respect the authority of "
                    "those above me, just as those below me must respect mine."
                ),
                'LAWFUL'
            ],
            [
                (
                    'Independence. I must prove that I can handle myself '
                    'without the coddling of my family.'
                ),
                'CHAOTIC'
            ],
            [
                (
                    'Power. If I can attain more power, no one will tell me '
                    'what to do.'
                ), 'EVIL'
            ],
            [
                'Family. Blood runs thicker than water.', 'ANY'
            ],
            [
                (
                    'Noble Obligation. It is my duty to protect and care '
                    'for the people beneath me.'
                ),
                'GOOD'
            ],
        ]
        bonds_options = [
            'I will face any challenge to win the approval of my family.',
            'My house\'s alliance with another noble family must be '
            'sustained at all costs.',
            'Nothing is more important than the other members of my family',
            'I am in love w/ the heir of a family that my family despises',
            'My loyalty to my sovereign is unwavering',
            'The common folk must see me as a hero of the people.',
        ]
        flaws_options = [
            'I secretly believe that everyone is beneath me.',
            'I hide a truly scandalous secret that could ruin my family '
            'forever.',
            'I too often hear veiled insults and threats in every word '
            'addressed to me, and I\'m quick to anger',
            'I have an insatiable desire for carnal pleasures',
            'In fact, the world does revolve around me.',
            'By my words and actions, I often bring shame to my family'
        ]
        tools_options = [
            "DICE SET",
            "DRAGONCHESS SET",
            "PLAYING CARD SET",
            "THREE-DRAGON ANTE SET"
        ]

        super().__init__(
            name=name,
            skills=['HISTORY', 'PERSUASION'],
            possible_traits=personalities_options,
            possible_ideals=ideals_options,
            possible_bonds=bonds_options,
            possible_flaws=flaws_options,
            equipment=equipment,
            feature=feature,
            wealth=25,
            variant=variant,
            languages=1,
            number_tools=1,
            tools_options=tools_options
        )


class Outlander(Background):
    def __init__(
            self,
            equipment,
    ):
        possible_specialities = [
            'Forester',
            'Trapper',
            'Homesteader',
            'Guide',
            'Exile or outcast',
            'Bounty hunter',
            'Pilgrim',
            'Tribal nomad',
            'Hunter-gatherer',
            'Tribal marauder'
        ]
        possible_traits = [
            'I\'m driven by a wanderlust that led me away from home',
            'I watch over my friends as if they were a litter of newborn '
            'pups',
            'I once ran twenty-five miles without stopping to warn to my '
            'clan of an approaching orc horde. I\'d do it again if I had to',
            'I have a lesson for every situation, drawn from observing '
            'nature.',
            'I place no stock in wealthy or well-mannered folk. Money and '
            'manners won\'t save you from a hungry owlbear.',
            'I\'m always picking things up, absently fiddling with them, '
            'and sometimes accidentally breaking them.',
            'I feel far more comfortable around animals than people',
            'I was, in fact, raised by wolves.'
        ]
        possible_ideals = [
            [
                (
                    "Change. Life's like the seasons, in constant change, and "
                    'we must change with it.'
                ),
                'CHAOTIC'
            ],
            [
                (
                    'Greater Good. It is each person\'s responsibility to make '
                    'the most happiness for the whole tribe.'
                ),
                'GOOD'
            ],
            [
                'Honor. If I dishonor myself, I dishonor my whole clan',
                'LAWFUL'
            ],
            [
                'Might. The strongest are meant to rule', 'EVIL'
            ],
            [
                'Nature. The natural world is more important than all the '
                'constructs of civilization.', 'NEUTRAL'
            ],
            [
                'Glory. I must earn glory in battle, for myself and my clan',
                'ANY'
            ]
        ]
        possible_bonds = [
            'My family, clan, or tribe is the most important thing in my '
            'life, even when they are far from me.',
            'An injury to the unspoiled wilderness of my home is an injury '
            'to me.',
            'I will bring terrible wrath down on the evildoers who ['
            'destroyed my homeland.',
            'I am the last of my tribe, and it is up to me to ensure their '
            'names enter legend.',
            'I suffer awful visions of a coming disaster and will do '
            'anything to prevent it.',
            'It is my duty to provide children to sustain my tribe.'
        ]
        possible_flaws = [
            'I am too enamored of ale, wine, and other intoxicants.',
            'There\'s no room for caution in a life lived to the fullest.',
            'I remember every insult I\'ve received and nurse a silent '
            'resentment toward anyone who\'s ever wronged me.',
            'I am slow to trust members of other races, tribes, and '
            'societies',
            'Violence is my answer to almost any challenge.',
            'Don\'t expect me to save those who can\'t save themselves. It '
            'is nature\'s way that the strong thrive and the weak perish.'
        ]
        tools_options = [
            'BAGPIPES', 'DRUM', 'DULCIMER', 'FLUTE', 'LUTE',
            'LYRE', 'HORN', 'PAN FLUTE', 'SHAWM', 'VIOL'
        ]

        super().__init__(
            name='OUTLANDER',
            skills=['ATHLETICS', 'SURVIVAL'],
            equipment=equipment,
            feature=['WANDERER'],
            wealth=10,
            languages=1,
            number_tools=1,
            tools_options=tools_options,
            possible_specialities=possible_specialities,
            possible_traits=possible_traits,
            possible_ideals=possible_ideals,
            possible_bonds=possible_bonds,
            possible_flaws=possible_flaws,
        )


class Sage(Background):
    def __init__(
            self,
            equipment,
    ):
        possible_specialities = [
            'Alchemist',
            'Astronomer',
            'Discredited academic',
            'Librarian',
            'Professor',
            'Researcher',
            'Wizard\'s Apprentice',
            'Scribe'
        ]
        possible_traits = [
            'I use polysyllabic words that convey the impression of great '
            'erudition',
            'I\'ve read every book in the world\'s greatest libraries - or '
            'I like to boast that I have',
            "I'm used to helping out those who aren't as smart as I am, "
            'and I patiently explain anything and everything to others',
            'There\'s nothing I like more than a good mystery',
            'I\'m willing to listen to every side of an argument before I '
            'make my own judgement',
            'I... speak... slowly... when talking... to idiots... which... '
            'almost... everyone... is... compared... to me',
            'I am horribly awkward in social situations',
            'I\'m convinced that people are always trying to steal '
            'my secrets'
        ]
        possible_ideals = [
            [
                'Knowledge. The path to power and self-improvement is through '
                'knowledge.',
                'NEUTRAL'
            ],
            [
                'Beauty. What is beautiful points us beyond itself toward '
                'what is true.',
                'GOOD'
            ],
            [
                'Logic. Emotion must not cloud logical thinking',
                'LAWFUL'
            ],
            [
                'No Limits. Nothing should fetter the infinite possibility '
                'inherent in all existence.',
                'CHAOTIC'
            ],
            [
                'Power. Knowledge is the path to power and domination.',
                'EVIL'
            ],
            [
                'Self-Improvement. The goal of a life of study is the '
                'betterment of oneself.',
                'ANY'
            ]
        ]
        possible_bonds = [
            'It is my duty to protect my students.',
            'I have an ancient text that holds terrible secrets that must '
            'not fall into the wrong hands.',
            'I work to preserve a library, university, scriptorium, or '
            'monastery.',
            'My life\'s work is a series of tomes related to a specific '
            'field of lore.',
            'I\'ve been searching my whole life for the answer to a '
            'certain question.',
            'I sold my soul for knowledge. I hope to do great deeds and '
            'win it back.'
        ]
        possible_flaws = [
            'I am easily distracted by the promise of information.',
            'Most people scream and run when they see a demon. I stop and '
            'take notes on its anatomy.',
            'Unlocking an ancient mystery is worth the price of a '
            'civilization.',
            'I overlook obvious solutions in favor of complicated ones',
            'I speak without really thinking through my words, invariably '
            'insulting others.',
            'I can\'t keep a secret to save my life, or anyone else\'s.'
        ]

        super().__init__(
            name='SAGE',
            skills=['ARCANA'],
            equipment=equipment,
            feature=['RESEARCHER'],
            wealth=10,
            languages=2,
            possible_specialities=possible_specialities,
            possible_traits=possible_traits,
            possible_ideals=possible_ideals,
            possible_bonds=possible_bonds,
            possible_flaws=possible_flaws,
        )


class Sailor(Background):
    def __init__(
            self,
            equipment,
            variant,
    ):
        if variant:
            name = 'PIRATE'
            feature_options = ['SHIP\'S PASSAGE', 'BAD REPUTATION']
            feature = None
        else:
            name = 'SAILOR'
            feature = ['SHIP\'S PASSAGE']
            feature_options = None

        possible_traits = [
            'My friends know they can rely on me, no matter what.',
            'I work hard so that I can play hard when the work is done.',
            'I enjoy sailing into new ports and making new friends over a '
            'flagon of ale',
            'I stretch the truth for the sake of a good story.',
            'To me, a tavern brawl is a nice way to get to know a new city',
            'I never pass up a friendly wager.',
            'My language is as foul as an otyugh nest.',
            'I like a job well done, especially if I can convince someone '
            'else to do it.'
        ]
        possible_ideals = [
            [
                'Respect. The thing that keeps a ship together is mutual '
                'respect between captain and crew.',
                'GOOD'
            ],
            [
                'Fairness. We all do the work, so we all share in the rewards',
                'LAWFUL'
            ],
            [
                'Freedom. The sea is freedom— the freedom to go anywhere and '
                'do anything.',
                'CHAOTIC'
            ],
            [
                'Mastery. I\'m a predator, and the other ships on the sea are '
                'my prey.',
                'EVIL'
            ],
            [
                'People. I\'m committed to my crewmates, not to ideals.',
                'NEUTRAL'
            ],
            [
                'Aspiration. Someday I\'ll own my own ship and chart my own '
                'destiny.',
                'ANY'
            ]
        ]
        possible_bonds = [
            'I\'m loyal to my captain first, everything else second.',
            'The ship is most important—crewmates and captains come and go',
            'I\'ll always remember my first ship.',
            'In a harbor town, I have a paramour whose eyes nearly stole '
            'me from the sea.',
            'I was cheated out of my fair share of the profits, and I '
            'want to get my due.',
            'Ruthless pirates murdered my captain and crewmates, plundered '
            'our ship, and left me to die. Vengeance will be mine.'
        ]
        possible_flaws = [
            'I follow orders, even if I think they\'re wrong.',
            'I\'ll say anything to avoid having to do extra work.',
            'Once someone questions my courage, I never back down no '
            'matter how dangerous the situation.',
            'Once I start drinking, it\'s hard for me to stop.',
            'I can\'t help but pocket loose coins and other trinkets I come '
            'across.',
            'My pride will probably lead to my destruction.'
        ]
        tools_proficiency = ["NAVIGATOR'S TOOLS", "VEHICLES (WATER)"]

        super().__init__(
            name=name,
            skills=['ATHLETICS', 'PERCEPTION'],
            equipment=equipment,
            feature=feature,
            feature_options=feature_options,
            wealth=10,
            variant=variant,
            tools_proficiency=tools_proficiency,
            possible_traits=possible_traits,
            possible_ideals=possible_ideals,
            possible_bonds=possible_bonds,
            possible_flaws=possible_flaws,
        )


class Soldier(Background):
    def __init__(
            self,
            equipment,
    ):
        possible_specialities = [
            'Officer',
            'Scout',
            'Infantry',
            'Cavalry',
            'Healer',
            'Quartermaster',
            'Standard bearer',
            'Support staff'
        ]
        possible_traits = [
            'I\'m always polite and respectful.',
            'I\'m haunted by memories of war. I can\'t get the images of '
            'violence out of my mind',
            'I\'ve lost too many friends, and I\'m slow to make new ones.',
            'I\'m full of inspiring and cautionary tales from my military '
            'experience relevant to almost every combat situation.',
            'I can stare down a hell hound without flinching.',
            'I enjoy being strong and like breaking things.',
            'I have a crude sense of humor.',
            'I face problems head-on. A simple, direct solution is the '
            'best path to success.'
        ]
        possible_ideals = [
            [
                'Greater Good. Our lot is to lay down our lives in defense of '
                'others.',
                'GOOD'
            ],
            [
                'Responsibility. I do what I must and obey just authority.',
                'LAWFUL'
            ],
            [
                'Independence. When people follow orders blindly, they embrace '
                'a kind of tyranny.',
                'CHAOTIC'
            ],
            [
                'Might. In life as in war, the stronger force wins.',
                'EVIL'
            ],
            [
                "Live and Let Live. Ideals aren't worth killing over or going "
                'to war for.',
                'NEUTRAL'
            ],
            [
                'Nation. My city, nation, or people are all that matter.',
                'ANY'
            ]
        ]
        possible_bonds = [
            'I would still lay down my life for the people I served with.',
            'Someone saved my life on the battlefield. To this day, I will '
            'never leave a friend behind.',
            'My honor is my life.',
            'I\'ll never forget the crushing defeat my company suffered or '
            'the enemies who dealt it.',
            'Those who fight beside me are those worth dying for.',
            'I fight for those who cannot fight for themselves.'
        ]
        possible_flaws = [
            'The monstrous enemy we faced in battle still leaves me '
            'quivering with fear.',
            'I have little respect for anyone who is not a proven warrior.',
            'I made a terrible mistake in battle cost many lives — and I '
            'would do anything to keep that mistake secret.',
            'My hatred of my enemies is blind and unreasoning.',
            'I obey the law, even if the law causes misery.',
            'I\'d rather eat my armor than admit when I\'m wrong.'
        ]
        tools_options = [
            'DICE SET', 'DRAGONCHESS SET', 'PLAYING CARD SET',
            'THREE-DRAGON ANTE SET'
        ]

        super().__init__(
            name='SOLDIER',
            skills=['ATHLETICS', 'INTIMIDATION'],
            equipment=equipment,
            feature=['MILITARY RANK'],
            wealth=10,
            tools_proficiency=['VEHICLES (LAND)'],
            number_tools=1,
            tools_options=tools_options,
            possible_traits=possible_traits,
            possible_ideals=possible_ideals,
            possible_bonds=possible_bonds,
            possible_flaws=possible_flaws,
            possible_specialities=possible_specialities,
        )


class Urchin(Background):
    def __init__(
            self,
            equipment,
    ):
        possible_traits = [
            'I hide scraps of food and trinkets away in my pockets.',
            'I ask a lot of questions.',
            'I like to squeeze into small places where no one else can '
            'get to me.',
            'I sleep with my back to a wall or tree, with everything I own '
            'wrapped in a bundle in my arms.',
            'I eat like a pig and have bad manners.',
            'I think anyone who\'s nice to me is hiding evil intent.',
            'I don\'t like to bathe.',
            'I bluntly say what other people are hinting at or hiding.'
        ]
        possible_ideals = [
            [
                'Respect. All people, rich or poor, deserve respect.',
                'GOOD'
            ],
            [
                'Community. We have to take care of each other, because no '
                'one else is going to do it.',
                'LAWFUL'
            ],
            [
                'Change. The low are lifted up, and the high and mighty are '
                'brought down. Change is the nature of things.',
                'CHAOTIC'
            ],
            [
                'Retribution. The rich need to be shown what life and death '
                'are like in the gutters.',
                'EVIL'
            ],
            [
                'People. I help the people who help me— that\'s what keeps us '
                'alive.',
                'NEUTRAL'
            ],
            [
                'Aspiration. I\'m going to prove that I\'m worthy of a '
                'better life.',
                'ANY'
            ]
        ]
        possible_bonds = [
            'My town or city is my home, and I\'ll fight to defend it.',
            'I sponsor an orphanage to keep others from enduring what I '
            'was forced to endure.',
            'I owe my survival to another urchin who taught me to live on '
            'the streets.',
            'I owe a debt I can never repay to the person who took pity '
            'on me.',
            'I escaped my life of poverty by robbing an important person, '
            'and I\'m wanted for it.',
            'No one else should have to endure the hardships I\'ve been '
            'through.'
        ]
        possible_flaws = [
            'If I\'m outnumbered, I will run away from a fight.',
            'Gold seems like a lot of money to me, and I\'ll do just about '
            'anything for more of it.',
            'I will never fully trust anyone other than myself.',
            'I\'d rather kill someone in their sleep then fight fair.',
            'It\'s not stealing if I need it more than someone else.',
            'People who can\'t take care of themselves get what they '
            'deserve.'
        ]

        super().__init__(
            name='URCHIN',
            skills=['SLEIGHT OF HAND', 'STEALTH'],
            equipment=equipment,
            feature=['CITY SECRETS'],
            wealth=10,
            tools_proficiency=['DISGUISE KIT', 'THIEVES\' TOOLS'],
            possible_traits=possible_traits,
            possible_ideals=possible_ideals,
            possible_bonds=possible_bonds,
            possible_flaws=possible_flaws,
        )


class Spell:
    def __init__(
            self,
            name,
            casting_time,
            spell_range,
            components,
            duration,
            effect,
            level,
            school,
            ritual=False,
            concentration=False,
            material_components=None,
    ):
        self.name = name
        self.casting_time = casting_time
        self.range = spell_range
        self.components = components
        self.duration = duration
        self.effect = effect
        self.level = level
        self.school = school
        self.times_cast = 0
        self.ritual = ritual
        self.concentration = concentration
        self.material_components = material_components

    def cast(self, character, spell_slot=0):
        self.effect(character, spell_slot)


class Character:
    xp_by_level = {
        1: 0,
        2: 300,
        3: 900,
        4: 2700,
        5: 6500,
        6: 14000,
        7: 23000,
        8: 34000,
        9: 48000,
        10: 64000,
        11: 85000,
        12: 100000,
        13: 120000,
        14: 140000,
        15: 165000,
        16: 195000,
        17: 225000,
        18: 265000,
        19: 305000,
        20: 355000
    }

    def __init__(
            self,
            race,
            background,
            classe,
            abilities,
            alignment,
            personal_info,
            proficiencies,
            languages,
            equipments
    ):
        self.general_info = {
            'NAME': personal_info["CHARACTER'S NAME"],
            'CLASS': classe.name,
            'LEVEL': 1,
            'BACKGROUND': background.name,
            'PLAYER': personal_info["PLAYER'S NAME"],
            'RACE': race.name,
            'ALIGNMENT': alignment,
            'XP': 0,
        }
        self.specialization = {
            'NAME': classe.specialization,
            'LEVEL': classe.specialization_level,
            'ALL FEATURES': classe.specializations_features
        }
        self.abilities = abilities
        self.proficiencies = proficiencies
        self.languages = languages
        self.general_stats = {
            'AC': 10 + abilities.score('DEX'),
            'INITIATIVE':
                abilities.score('DEX')
                + (proficiencies['VALUE'] if 'DEX' in
                    proficiencies['SAVING THROWS'] else 0),
            'SPEED': race.speed,
            'MAXIMUM HP': classe.hit_die.max + abilities.score('CON'),
            'CURRENT HP': classe.hit_die.max + abilities.score('CON'),
            'TEMPORARY HP': 0,
            'HIT DICE': classe.hit_die,
            'USED HIT DICE': 0
        }
        self.equipments = equipments
        self.wealth = background.wealth if classe.wealth == -1 \
            else classe.wealth
        self.psychology = {
            'BACKGROUND SPECIALITY': background.background_speciality,
            'PERSONALITY TRAIT': background.personality_trait,
            'IDEAL': background.ideal,
            'BOND': background.bond,
            'FLAW': background.flaw
        }
        self.backup = {
            'RACE': race,
            'CLASS': classe,
            'BACKGROUND': background
        }
        self.class_all_features = classe.all_features

        self.single_features = \
            race.features \
            + classe.features \
            + background.feature
        self.features = {
            'RACE': race.features,
            'CLASS': classe.features,
            'BACKGROUND': background.feature,
            'SPECIALIZATION': classe.specialization_features,
            'ADVANTAGES': race.advantages,
            'DISADVANTAGES': race.disadvantages,
            'RESISTANCES': race.resistances
        }
        self.personal_info = personal_info

        if classe.magical_ability.has_magic is not None \
                and race.magical_ability.has_magic is not None:
            sum_cantrips_by_level = {}
            sum_spells_by_level = {}

            for level in range(1, 20 + 1):
                sum_cantrips_by_level[level] = \
                    classe.magical_ability.cantrips_by_level[level] \
                    + race.magical_ability.cantrips_by_level[level]

                sum_spells_by_level[level] = \
                    classe.magical_ability.spells_by_level[level] \
                    + race.magical_ability.spells_by_level[level]

            if classe.magical_ability.highest_spell_level \
                    > race.magical_ability.highest_spell_level:
                highest_spell_level = classe.magical_ability.highest_spell_level
            else:
                highest_spell_level = race.magical_ability.highest_spell_level

            self.magical_ability = MagicAbilities(
                has_magic=classe.magical_ability.has_magic
                or race.magical_ability.has_magic,
                magical_ability={
                    race.name: classe.magical_ability.magical_ability,
                    classe.name: classe.magical_ability.magical_ability,
                },
                cantrips_by_level=sum_cantrips_by_level,
                spells_by_level=sum_spells_by_level,
                cantrips_known=sum_cantrips_by_level[1],
                spells_known=sum_spells_by_level[1],
                highest_spell_level=highest_spell_level,
                cantrips=race.magical_ability.cantrips,
                spells=race.magical_ability.spells,
                spell_slots_by_level=classe.magical_ability.
                spell_slots_by_level,
                spell_slots=classe.magical_ability.spell_slots,
                spell_save_dc=classe.magical_ability.spell_save_dc,
                spell_attack_modifier=classe.magical_ability.
                spell_attack_modifier,
                prepare_spells=classe.magical_ability.prepare_spells,
                prepared_spells=classe.magical_ability.prepared_spells,
                spell_list=classe.magical_ability.spell_list,
                number_prepared_spells=classe.magical_ability.
                number_prepared_spells
            )
        elif classe.magical_ability.has_magic is not None:
            self.magical_ability = classe.magical_ability
        elif race.magical_ability.has_magic is not None:
            self.magical_ability = race.magical_ability
            self.magical_ability.spell_save_dc = 8 \
                + proficiencies['VALUE'] \
                + abilities.score(self.magical_ability.magical_ability)
        else:
            self.magical_ability = MagicAbilities()

        self.sessions = 0

        # Store the functions from the Class class to the character Class
        self.select_features = classe.select_features
        self.specialization_check = classe.specialization_check
        self.select_specialization_features = classe.\
            select_specialization_features
        self.unite_specialization_features = classe.\
            unite_specialization_features

        self.dead = False
        self.checks_succeeded = 0
        self.checks_failed = 0
        self.real_level = classe.level
        self.general_info['XP'] = self.xp_by_level[self.real_level]
