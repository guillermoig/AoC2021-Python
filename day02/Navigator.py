import re

class Navigator:
    def __init__(self) -> None:
        self.set_instructions = dict({
            'forward': list([]),
            'down': list([]),
            'up': list([])
        })

    def get_set_instructions(self) -> dict:
        return self.set_instructions

    def set_course_instructions(self, instructions) -> None:
        for line in instructions.splitlines():
            instruction = re.search("^(forward|down|up)\s([0-9]+)$", line)
            self.set_instructions[instruction.group(1)].append(int(instruction.group(2)))

    def position_calculator(self) -> list:
        position = {
            'horizontal': sum(self.set_instructions['forward']),
            'depth': sum(self.set_instructions['down']) - sum(self.set_instructions['up'])
        }
        return position

    def get_position_multiplication(self) -> int:
        position = self.position_calculator()
        return position['horizontal'] * position['depth']
