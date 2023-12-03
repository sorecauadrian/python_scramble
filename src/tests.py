import unittest
from src.scramble.scramble import Scramble


class Test(unittest.TestCase):
    def test_swap(self):
        scramble = Scramble()
        scramble.sentence = "djiboutian citizen"
        scramble.score = len(scramble)
        scramble.shuffled_sentence = "djiboutiac nitizen"

        try:
            scramble.swap(0, 1, 2, 1)
            assert False
        except Exception:
            assert True

        try:
            scramble.swap(0, 17, 1, 2)
            assert False
        except Exception:
            assert True

        self.assertEqual(scramble.swap(0, 0, 0, 0), scramble.shuffled_sentence)
        scramble.swap(1, 0, 1, 0)
        self.assertEqual(scramble.score, len(scramble) - 2)
        self.assertEqual(scramble.swap(0, 9, 1, 0), scramble.sentence)
        for _ in range(len(scramble) - 3):
            scramble.swap(0, 1, 1, 0)
        self.assertEqual(scramble.score, 0)

    def test_undo(self):
        scramble = Scramble()
        scramble.sentence = "djiboutian citizen"
        scramble.score = len(scramble)
        scramble.shuffled_sentence = "djiboutiac nitizen"

        scramble.swap(0, 9, 1, 0)
        scramble.swap(0, 9, 1, 0)
        scramble.undo()
        self.assertEqual(scramble.sentence, scramble.shuffled_sentence)
        self.assertEqual(scramble.score, len(scramble) - 2)

    def test_shuffle_sentence(self):
        scramble = Scramble()
        scramble.sentence = "djiboutian citizen"
        scramble.score = len(scramble)
        scramble.shuffled_sentence = scramble.shuffle_sentence()

        self.assertEqual(scramble.sentence == scramble.shuffled_sentence, False)
        scramble.swap(0, 0, 0, 0)
        self.assertEqual(scramble.sentence == scramble.shuffled_sentence, False)




