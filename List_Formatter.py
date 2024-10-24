from Accessories.romanNumeralConverter import RomanNum


class ListFormatter:
    def __init__(self, data_list, tab_space=4):
        self.data_list = data_list
        self.tab_space = tab_space
        self.main_counter = 1  # For numbering main categories
        self.roman_counter = 0  # For numbering subcategories at depth 1

        self.key_symbols = ['☞', '□', '⁜', '⟐', '∎', '◎', '⌘', '▣', '✠', '▩', '☆']
        self.value_symbols = ['*', '⟡', '⊹', '◌', '⨳', '⪼', '֎', '⊛', '◈', '❖', '✿']

    def format_list(self):
        self.process_list(self.data_list)

    def process_list(self, data, depth=0):
        if isinstance(data, dict):
            for key, value in data.items():
                if depth == 0:
                    self.print_main_category(key)
                    self.roman_counter = 1
                else:
                    self.print_key(key, depth)
                    if depth == 1:  # Increment Roman numeral counter for depth 1
                        self.roman_counter += 1
                self.process_list(value, depth + 1)
        elif isinstance(data, list):
            for index, item in enumerate(data, 1):
                self.process_list(item, depth)
        else:
            self.print_value(data, depth)

    def print_main_category(self, key):
        print(f"{self.main_counter}. {key}:")
        self.main_counter += 1

    def print_key(self, key, depth):
        indent = ' ' * self.tab_space * depth
        if depth == 1:
            roman_num = RomanNum(self.roman_counter)
            print(f"{indent}{roman_num}. {key}:")
        else:
            symbol = self.get_key_symbol(depth)
            print(f"{indent}{symbol} {key}:")

    def print_value(self, value, depth):
        indent = ' ' * self.tab_space * (depth + 1)
        symbol = self.get_value_symbol(depth)
        print(f"{indent}{symbol} {value}")

    def get_key_symbol(self, depth):
        return self.key_symbols[depth % len(self.key_symbols)]

    def get_value_symbol(self, depth):
        return self.value_symbols[depth % len(self.value_symbols)]


# Sample data
my_list = [
    {'Fruits': ['Apple', 'Orange', 'Mango']},
    {'Vegetables': ['Carrot', 'Beetroot', 'Cabbage', 'Snakegourd', 'Bitter gourd', 'Brinjal']},
    {'Yams': ['Manioc', 'Potato', 'Sweet Potato']},
    {'Beans': ['Chickpeas', 'Green Gram', 'Mung Beans', 'Soybean', 'Peanut']},
    {'Flowers': ['Rose', 'Carnation', 'Lotus', 'Lily']},
    {'Animals': [
        {'Farm Animals': ['Horse', 'Dog', 'Cow', 'Goat', 'Sheep']},
        {'Grassland Animals': ['Lion', 'Elephant', 'Cheetah']},
        {'Rainforest Animals': ['Anteater', 'Black Panther', 'Jaguar']},
        {'Mountain Animals': ['Civet', 'Cougar', 'Brown Bear']},
        {'Wild Animals': [
            {'Carnivorous': ['Leopard', 'Tiger', 'Alligator', 'Fox']},
            {'Herbivorous': ['Bison', 'Deer', 'Elk',
                             {'test': ['test 1', 'test 2', 'test 3',
                                       {'test2': ['test 21', 'test 22', 'test 23',
                                                  {'test3': ['test 31', 'test 32', 'test 33',
                                                             {'test4': ['test 41', 'test 42', 'test 43']}]}]}]}]},
            {'Omnivorous': ['Bear', 'Camel']}
        ]}
    ]},
    {'Birds': ['Parrot', 'Sparrow', 'Swan',
               {'Grassland Birds': ['Falcon', 'Eagle', 'Hawk', 'Peacock']}
               ]},
    {'Fish': ['Dolphin', 'Catfish', 'Bream', 'Marlin',
              {'Freshwater Animals': ['Crayfish']},
              {'Saltwater Animals': ['Otter', 'Sea Lion', 'Penguin', 'Whale', 'Clams',
                                     {'test5': ['test 51', 'test 52', 'test 53']}]}
              ]},
    {'Reptiles': ['Python', 'Chameleon', 'Alligator', 'Cobra', 'Crocodile', 'Lizard']}
]

formatter = ListFormatter(my_list)
formatter.format_list()
