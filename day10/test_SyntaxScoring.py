import unittest
from DataReader import DataReader
from SyntaxScoring import SyntaxScoring

class TestSyntaxScoring(unittest.TestCase):

    def setUp(self) -> None:
        data_reader = DataReader("data_test")
        self.syntaxScoring = SyntaxScoring(data_reader)
        return super().setUp()

    def test_getWrongCharacter(self):
        self.assertEqual(self.syntaxScoring.get_wrong_character('{([(<{}[<>[]}>{[]{[(<()>'), '}')

    def test_partOne(self):
        self.assertEqual(self.syntaxScoring.part_one(), 26397)

    def test_getIncopmpleteLines(self):
        incomplete_lines = [
            ['[','(','{','(','<','(','(',')',')','[',']','>','[','[','{','[',']','{','<','(',')','<','>','>'],
            ['[','(','(',')','[','<','>',']',')',']','(','{','[','<','{','<','<','[',']','>','>','('],
            ['(','(','(','(','{','<','>','}','<','{','<','{','<','>','}','{','[',']','{','[',']','{','}'],
            ['{','<','[','[',']',']','>','}','<','{','[','{','[','{','[',']','{','(',')','[','[','[',']'],
            ['<','{','(','[','{','{','}','}','[','<','[','[','[','<','>','{','}',']',']',']','>','[',']',']']
        ]
        self.assertEqual(self.syntaxScoring.get_incomplete_lines(), incomplete_lines)

    def test_getCloseCharsList(self):
        line = ['[','(','{','(','<','(','(',')',')','[',']','>','[','[','{','[',']','{','<','(',')','<','>','>']
        self.assertEqual(self.syntaxScoring.get_close_chars_list(line), ['}','}',']',']',')','}',')',']'])

    def test_partTwo(self):
        self.assertEqual(self.syntaxScoring.part_two(), 288957)

if __name__ == '__main__':
    unittest.main()
