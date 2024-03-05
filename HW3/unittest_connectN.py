import unittest
from connectN import Notation, Player, Board, Game

class TestConnectN(unittest.TestCase):

    def test_player_init(self):
        player = Player("Alice", Notation.PLAYER1, 1)
        self.assertEqual(player.getName(), "Alice")
        print(player.getNotation())
        self.assertEqual(player.getNotation().value, Notation.PLAYER1.value)


    def test_player_score(self):
        player = Player("Bob", Notation.PLAYER2, 2)
        self.assertEqual(player.getScore(), 2)  # Initial score
        player.addScoreByOne()
        self.assertEqual(player.getScore(), 3)  # Score after increment

    def test_player_notation(self):
        player = Player("Charlie", Notation.PLAYER2, 0)
        self.assertEqual(player.getNotation().value, 2)
    
    def test_board_init_and_display(self):
        board = Board(9,9)  # Assuming a standard connect 4 setup
        self.assertEqual(board.getColNum(), 9)

    def test_board_full(self):
        board = Board(9,9)
        for i in range(9):
            for j in range(9):
                board.placeMark(i, Notation.PLAYER1)
        self.assertTrue(board.checkFull())
    
    def test_board_win_horizontal(self):
        board = Board(4,4)
        board.placeMark(0, Notation.PLAYER1)
        board.placeMark(1, Notation.PLAYER1)
        self.assertTrue(board.checkWin(2))
    
    def test_board_win_vertical(self):
        board = Board(4,4)
        board.placeMark(0, Notation.PLAYER1)
        board.placeMark(0, Notation.PLAYER1)
        board.placeMark(0, Notation.PLAYER1)
        self.assertTrue(board.checkWin(3))
    
    def test_board_win_diagonal(self):
        board = Board(4,4)
        board.placeMark(0, Notation.PLAYER1)
        board.placeMark(1, Notation.PLAYER2)
        board.placeMark(1, Notation.PLAYER1)
        board.placeMark(2, Notation.PLAYER2)
        board.placeMark(2, Notation.PLAYER2)
        board.placeMark(2, Notation.PLAYER1)
        board.placeMark(3, Notation.PLAYER2)
        board.placeMark(3, Notation.PLAYER2)
        board.placeMark(3, Notation.PLAYER2)
        board.placeMark(3, Notation.PLAYER1)
        self.assertTrue(board.checkWin(4))
    
    def test_board_win_anti_diagonal(self):
        board = Board(4,4)
        board.placeMark(3, Notation.PLAYER1)
        board.placeMark(2, Notation.PLAYER2)
        board.placeMark(2, Notation.PLAYER1)
        board.placeMark(1, Notation.PLAYER2)
        board.placeMark(1, Notation.PLAYER2)
        board.placeMark(1, Notation.PLAYER1)
        board.placeMark(0, Notation.PLAYER2)
        board.placeMark(0, Notation.PLAYER2)
        board.placeMark(0, Notation.PLAYER2)
        board.placeMark(0, Notation.PLAYER1)
        self.assertTrue(board.checkWin(4))
    
    def test_display_board(self):
        board = Board(4,4)
        board.placeMark(0, Notation.PLAYER1)
        board.placeMark(1, Notation.PLAYER2)
        board.placeMark(2, Notation.PLAYER1)
        board.placeMark(3, Notation.PLAYER2)
        board.display()

if __name__ == '__main__':
    unittest.main()
