import unittest
from DataReader import DataReader
from DumboOctopus import DumboOctopus

class TestDumboOctopus(unittest.TestCase):

    def setUp(self) -> None:
        data_reader = DataReader("data_test2")
        self.dumbo_octopus = DumboOctopus(data_reader)
        return super().setUp()

    def test_runStep1Time(self):
        map = "6594254334\n3856965822\n6375667284\n7252447257\n7468496589\n5278635756\n3287952832\n7993992245\n5957959665\n6394862637"
        map_processed = [[int(x) for x in list(line)] for line in map.splitlines()]
        self.assertEqual(self.dumbo_octopus.run_step(), map_processed)

    def test_runStep2Times(self):
        map = "8807476555\n5089087054\n8597889608\n8485769600\n8700908800\n6600088989\n6800005943\n0000007456\n9000000876\n8700006848"
        map_processed = [[int(x) for x in list(line)] for line in map.splitlines()]
        self.dumbo_octopus.run_step()
        self.assertEqual(self.dumbo_octopus.run_step(), map_processed)

    def test_runStep10Times(self):
        map = "0481112976\n0031112009\n0041112504\n0081111406\n0099111306\n0093511233\n0442361130\n5532252350\n0532250600\n0032240000"
        map_processed = [[int(x) for x in list(line)] for line in map.splitlines()]
        for i in range(9):
            self.dumbo_octopus.run_step()
        self.assertEqual(self.dumbo_octopus.run_step(), map_processed)

    def test_runStep90Times(self):
        map = "7433333522\n2643333522\n2264333458\n2226433337\n2222433338\n2287833333\n2854573333\n4854458333\n3387779333\n3333333333"
        map_processed = [[int(x) for x in list(line)] for line in map.splitlines()]
        for i in range(89):
            self.dumbo_octopus.run_step()
        self.assertEqual(self.dumbo_octopus.run_step(), map_processed)

    def test_runStep100Times(self):
        map = "0397666866\n0749766918\n0053976933\n0004297822\n0004229892\n0053222877\n0532222966\n9322228966\n7922286866\n6789998766"
        map_processed = [[int(x) for x in list(line)] for line in map.splitlines()]
        for i in range(99):
            self.dumbo_octopus.run_step()
        self.assertEqual(self.dumbo_octopus.run_step(), map_processed)

    def test_runStep193Times(self):
        map = "5877777777\n8877777777\n7777777777\n7777777777\n7777777777\n7777777777\n7777777777\n7777777777\n7777777777\n7777777777"
        map_processed = [[int(x) for x in list(line)] for line in map.splitlines()]
        for i in range(192):
            self.dumbo_octopus.run_step()
        self.assertEqual(self.dumbo_octopus.run_step(), map_processed)

    def test_runStep194Times(self):
        map = "6988888888\n9988888888\n8888888888\n8888888888\n8888888888\n8888888888\n8888888888\n8888888888\n8888888888\n8888888888"
        map_processed = [[int(x) for x in list(line)] for line in map.splitlines()]
        for i in range(193):
            self.dumbo_octopus.run_step()
        self.assertEqual(self.dumbo_octopus.run_step(), map_processed)

    def test_runStep195Times(self):
        map = "0000000000\n0000000000\n0000000000\n0000000000\n0000000000\n0000000000\n0000000000\n0000000000\n0000000000\n0000000000"
        map_processed = [[int(x) for x in list(line)] for line in map.splitlines()]
        for i in range(194):
            self.dumbo_octopus.run_step()
        self.assertEqual(self.dumbo_octopus.run_step(), map_processed)

    def test_getFlashesAfter1Time(self):
        self.dumbo_octopus.run_step()
        self.assertEqual(self.dumbo_octopus.get_flashes(), 0)

    def test_getFlashesAfter2Times(self):
        self.dumbo_octopus.run_step()
        self.dumbo_octopus.run_step()
        self.assertEqual(self.dumbo_octopus.get_flashes(), 35)

    def test_partOne(self):
        self.assertEqual(self.dumbo_octopus.part_one(), 1656)

    def test_partTwo(self):
        self.assertEqual(self.dumbo_octopus.part_two(), 195)

if __name__ == '__main__':
    unittest.main()
