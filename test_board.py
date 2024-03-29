import unittest
from unittest.mock import patch
from board2 import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_clear_screen(self):
        with patch('builtins.print') as mock_print:
            self.board.clear_screen()
            mock_print.assert_called_with("\033[H\033[J", end="")

if __name__ == '__main__':
    unittest.main()