import random
import time


class blg:
    def __init__(self):
        self.number_choices = [0 for _ in range(30)]
        self.color_choices = {
            'B': 0,
            'R': 0,
            'G': 0,
        }
        self.colors = []
        for i in range(0, 30):
            if (i + 1) % 15 == 0:
                self.colors.append('Green')
                continue
            if (i + 1) % 2 != 0:
                self.colors.append('Black')
                continue
            else:
                self.colors.append('Red')
                continue

    def main_function(self):
        count = 15
        while count != 0:
            command = input()
            if not command.isdigit() or command not in ['R','G','B']:
                continue
            if command.isdigit():
                self.number_choices[int(command) -1] += 1
            else:
                self.color_choices[command] += 1

            count -= 1

        num = random.randint(0,29)
        color = self.colors[num]
        result = 0
        if color == 'Red':
            result += (self.color_choices[color[0]] * 2)
        if color == 'Black':
            result += (self.color_choices[color[0]] * 2)
        if color == 'Green':
            result += (self.color_choices[color[0]] * 15)

        result += (self.number_choices[num] * 15)

        return result




