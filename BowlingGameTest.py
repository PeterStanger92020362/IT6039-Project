
# @project: Bowling Game

import unittest
from Bowling import BowlingGame


class BowlingGameTests(unittest.TestCase):

    # adding a test method to test all gutters
    def test_all_gutters(self):
        """
        @param self:
        @:parameter 20 times throw
        @:parameter 0 pins hit
        @:returns 0 score
        """
        game = BowlingGame()
        game.throw_many(20, 0)
        game.calculate_score()
        self.assertEqual(game.score, 0)

    # adding a test method to test a perfect game
    def test_perfect_game(self):
        """
        @param self:
        @:parameter 12 times throw
        @:parameter 10 pins hit
        @:returns 300 score
        """
        game = BowlingGame()
        game.throw_many(12, 10)
        game.calculate_score()
        self.assertEqual(game.score, 300)

    # adding a test method for throw all with 1 pin hit always
    def test_all_ones(self):
        """
        @param self:
        @:parameter 20 times throw
        @:parameter 1 pins hit
        @:returns 20 score
        """
        game = BowlingGame()
        game.throw_many(20, 1)
        game.calculate_score()
        self.assertEqual(game.score, 20)

    # adding a test method for what is meant to be a spare
    def test_for_spare(self):
        """
        @param self:
        @:parameter 4 times single throw spare
        @:parameter different number of pins hit
        @:returns 25 score
        """
        game = BowlingGame()
        game.throw_one(4)
        game.throw_one(6)
        game.throw_one(7)
        game.throw_one(1)
        game.throw_many(16,0)
        game.calculate_score()
        self.assertEqual(game.score, 25)

    # adding a test method for what is meant to be a spare
    def test_for_spare_no_bonus(self):
        """
        @param self:
        @:parameter 4 times single throw spare
        @:parameter different number of pins hit
        @:returns 17 score
        """
        game = BowlingGame()
        game.throw_one(4)
        game.throw_one(6)
        game.throw_one(0)
        game.throw_one(7)
        game.throw_many(16,0)
        game.calculate_score()
        self.assertEqual(game.score, 17)

    # adding test method to test with one strike
    def test_for_one_strike(self):
        """
        @param self:
        @:parameter 3 times throw including  one strike
        @:parameter different number of pins hit
        @:returns 26 score
        """
        game = BowlingGame()
        game.throw_one(10)
        game.throw_one(3)
        game.throw_one(5)
        game.throw_many(16, 0)
        game.calculate_score()
        self.assertEqual(game.score, 26)

    # adding test method to test 2 strikes
    def test_for_two_strikes(self):
        """
        @param self:
        @:parameter 4 times throw including  two strikes consecutively
        @:parameter different number of pins hit
        @:returns 46 score
        """
        game = BowlingGame()
        game.throw_one(10)
        game.throw_one(10)
        game.throw_one(4)
        game.throw_one(2)
        game.throw_many(14, 0)
        game.calculate_score()
        self.assertEqual(game.score, 46)

# calling all tests in this class to be executed
if __name__ == '__main__':
    unittest.main()
