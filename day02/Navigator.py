import re

class Navigator:
    def __init__(self, data) -> None:
        self.instructions = data.splitlines()
        self.reset_position()
        pass

    def reset_position(self) -> None:
        self.position = {
            'horizontal': 0,
            'depth': 0,
            'aim': 0
        }

    def get_pattern(self):
        return re.compile("^(forward|down|up)\s([0-9]+)$")

    def part_one(self) -> int:
        pattern = self.get_pattern()
        self.reset_position()
        for instruction in self.instructions:
            decoded_inst = pattern.search(instruction)
            if decoded_inst:
                match decoded_inst.group(1):
                    case 'forward':
                        self.position['horizontal'] += int(decoded_inst.group(2))
                    case 'down':
                        self.position['depth'] += int(decoded_inst.group(2))
                    case 'up':
                        self.position['depth'] -= int(decoded_inst.group(2))
        return self.position['horizontal'] * self.position['depth']

    def part_two(self) -> int:
        pattern = self.get_pattern()
        self.reset_position()
        for instruction in self.instructions:
            decoded_inst = pattern.search(instruction)
            if decoded_inst:
                match decoded_inst.group(1):
                    case 'forward':
                        self.position['horizontal'] += int(decoded_inst.group(2))
                        self.position['depth'] += self.position['aim'] * int(decoded_inst.group(2))
                    case 'down':
                        self.position['aim'] += int(decoded_inst.group(2))
                    case 'up':
                        self.position['aim'] -= int(decoded_inst.group(2))
        return self.position['horizontal'] * self.position['depth']
