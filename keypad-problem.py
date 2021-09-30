#!/usr/bin/env python3

import argparse
from os.path import basename

class Button():
    def __init__(self, row, col, reachable):
        self.row = row
        self.col = col
        self.reachable = reachable

keypad = [
    Button(3, 1, [4,6]), # 0
    Button(0, 0, [7,9]), # 1
    Button(0, 1, [4,8]), # 2
    Button(0, 2, [6,8]), # 3
    Button(1, 0, [3,9,0]), # 4
    Button(1, 1, []), # 5
    Button(1, 2, [1,7,0]), # 6
    Button(2, 0, [2,6]), # 7
    Button(2, 1, [1,3]), # 8
    Button(2, 2, [2,4]), # 9
]

def count(current_digit, digit):
    if current_digit == total_digits:
        return 1
    else:
        total = 0
        for number in keypad[digit].reachable: 
            total += count(current_digit+1, number)
    return total

def main(args):
    total = 0
    digits = 1
    global total_digits
    total_digits = args.digits

    for digit in range(1, 10): # Nine numbers on keypad, assume cannot start with 0
        print (digit)
        total += count(digits, digit)
    print(f"There are {total} combinations of {total_digits} numbers")
   

if __name__ == '__main__':
    parser = argparse.ArgumentParser(basename(__file__), __doc__,
                                     description="This absolutely incredible python script will change your life!",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter, )
    # Boolean flag example
    parser.add_argument('--verbose', action='store_true', help='Add more descriptive output')
    parser.add_argument('--debug', action='store_true', help='Enable debugging output')

    parser.add_argument('digits', type=int, default=8)

    args = parser.parse_args()
    global DEBUG
    DEBUG = args.debug

    main(args)
    parser.exit()
