# -*- coding:utf-8 -*-

import curses
from random import randrange, choice
from collections import defaultdict

letter_codes = [ord(ch) for ch in 'WSADQRwsadqr']
actions = ['Up', 'Down', 'Left', 'Right', 'Restart', 'Exit']

actions_dict = dict(zip(letter_codes, actions*2))

def get_user_action(keyboard):
    char = 'N'
    while char not in actions_dict:
        char = keyboard.getch()

    return actions_dict[char]


def transpose(field):
    return [list(row) for row in zip(*field)]


def invert(field):
    return [row[::-1] for row in field]

class GameField(object):
    def __init__(self, height=4, width=4, win=2048):
        self.height = height
        self.width = width
        self.win_value = win
        self.score = 0
        self.heighscore = 0
        self.reset()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0

        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()
        self.spawn()


    def move(self, direction):
        def move_row_lef(row):
            def tighten(row):
                new_row = [i for i in row if i != 0]
                new_row += [0 for i in range(len(row) - len(new_row))]
                return new_row

            def merge(row):
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(2 * row[i])
                        self.score += 2 * row[i]
                        pair = False
                    else:
                        if i + 1 < len(row) and row[i] == row[i + 1]:
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row)
                return new_row
            return tighten(merge(tighten(row)))

print(actions_dict)
print(letter_codes)
print(actions)