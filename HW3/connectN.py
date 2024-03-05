from enum import Enum

'''
This is the start of the HW.
If there is any conflict between the doc string and the HW document,
please follow the instruction in the HW document.
Good Luck and have fun !
'''

class Notation(Enum):
    """Enumeration for representing different types of notations in the game.

    Attributes:
        EMPTY (int): Represents an empty cell on the board.
        PLAYER1 (int): Represents a cell occupied by Player 1.
        PLAYER2 (int): Represents a cell occupied by Player 2.
    """
    EMPTY = 0
    PLAYER1 = 1
    PLAYER2 = 2

class Player:
    """Represents a player in the game.

    Attributes:
        __playerName (str): The name of the player.
        __playerNotation (Notation): The notation (symbol) used by the player on the board.
        __curScore (int): The current score of the player.

    Args:
        playerName (str): The name of the player.
        playerNotation (Notation): The notation (symbol) used by the player.
        curScore (int): The initial score of the player.
    """
    def __init__(self, playerName, playerNotation, curScore):
        self.__PlayerName = playerName
        self.__PlayerNotation = playerNotation
        self.__curScore = curScore

    def display(self) -> str:
        """Displays the player's details including name, notation, and current score."""
        return f"Player Name: {self.__PlayerName}, Notation: {self.__PlayerNotation}, Current Score: {self.__curScore}"

    def addScoreByOne(self):
        """Increments the player's score by one."""
        self.__curScore += 1

    def getScore(self):
        """Returns the current score of the player."""
        return self.__curScore

    def getName(self):
        """Returns the name of the player."""
        return self.__PlayerName

    def getNotation(self):
        """Returns the notation used by the player."""
        return self.__PlayerNotation

class Board:
    """Represents the game board.

    Attributes:
        __rowNum (int): Number of rows in the board.
        __colNum (int): Number of columns in the board.
        __grid (list): 2D list representing the game board.

    Args:
        rowNum (int): Number of rows in the board.
        colNum (int): Number of columns in the board.
    """

    def __init__(self, rowNum, colNum) -> None:
        self.__rowNum = rowNum
        self.__colNum = colNum
        self.__grid = []
        self.initGrid()


    def initGrid(self):
        """Initializes the game board with empty cells."""
        self.__grid = [[Notation.EMPTY for _ in range(self.__colNum)] for _ in range(self.__rowNum)]

    def getColNum(self):
        """Returns the number of columns in the board."""
        return self.__colNum

    def placeMark(self, colNum, mark):
        """Attempts to place a mark on the board at the specified column.

        Args:
            colNum (int): The column number where the mark is to be placed.
            mark (Notation): The mark to be placed on the board.

        Returns:
            bool: True if the mark was successfully placed, False otherwise.
        """
        if colNum < 0 or colNum >= self.__colNum:
            print("Error: Invalid column number.")
            return False

        if self.__grid[0][colNum] != Notation.EMPTY:
            print("Error: Column is full.")
            return False

        if mark == Notation.EMPTY:
            print("Error: Invalid marker.")
            return False

        for i in range(self.__rowNum - 1, -1, -1):
            if self.__grid[i][colNum] == Notation.EMPTY:
                self.__grid[i][colNum] = mark
                return True

        return False
        

    def checkFull(self):
        """Checks if the board is completely filled.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        for i in range(self.__rowNum):
            for j in range(self.__colNum):
                if self.__grid[i][j] == Notation.EMPTY:
                    return False
        return True

    def display(self):
        """Displays the current state of the board."""
        boardStr = ""
        for i in range(self.__rowNum):
            for j in range(self.__colNum):
                if self.__grid[i][j] == Notation.EMPTY:
                    boardStr += "O"
                elif self.__grid[i][j] == Notation.PLAYER1:
                    boardStr += "R"
                elif self.__grid[i][j] == Notation.PLAYER2:
                    boardStr += "Y"
            boardStr += "\n"
        print("Current Board is \n" + boardStr)

    # Private methods for internal use
    def __checkWinHorizontal(self, target):
        for i in range(self.__rowNum):
            for j in range(self.__colNum - target + 1):
                if self.__grid[i][j] != Notation.EMPTY and all(self.__grid[i][j] == self.__grid[i][j+k] for k in range(target)):
                    return self.__grid[i][j]
        return None

    def __checkWinVertical(self, target):
        for i in range(self.__colNum):
            for j in range(self.__rowNum - target + 1):
                if self.__grid[j][i] != Notation.EMPTY and all(self.__grid[j][i] == self.__grid[j+k][i] for k in range(target)):
                    return self.__grid[j][i]
        return None

    def __checkWinOneDiag(self, target, rowNum, colNum):
        for i in range(rowNum - target + 1):
            for j in range(colNum - target + 1):
                if self.__grid[i][j] != Notation.EMPTY and all(self.__grid[i+k][j+k] == self.__grid[i][j] for k in range(target)):
                    return self.__grid[i][j]
        return None



    def __checkWinAntiOneDiag(self, target, rowNum, colNum):
        for i in range(target - 1, rowNum):
            for j in range(colNum - target + 1):
                if self.__grid[i][j] != Notation.EMPTY and all(self.__grid[i-k][j+k] == self.__grid[i][j] for k in range(target)):
                    return self.__grid[i][j]
        return None
    
    def __checkWinDiagonal(self, target):
        oneDiagWin = self.__checkWinOneDiag(target, self.__rowNum, self.__colNum)
        if oneDiagWin is not None:
            return oneDiagWin

        antiOneDiagWin = self.__checkWinAntiOneDiag(target, self.__rowNum, self.__colNum)
        if antiOneDiagWin is not None:
            return antiOneDiagWin

        return None

    def checkWin(self, target):
        """Checks if there is a winning condition on the board.

        Args:
            target (int): The number of consecutive marks needed for a win.

        Returns:
            Notation or None: The notation of the winning player, or None if there is no winner.
        """
        for check in [self.__checkWinHorizontal, self.__checkWinVertical, self.__checkWinDiagonal]:
            result = check(target)
            if result is not None:
                return result
        return None

class Game:
    """Represents the game logic and flow.

    Args:
        rowNum (int): Number of rows in the game board.
        colNum (int): Number of columns in the game board.
        connectN (int): Number of consecutive marks needed for a win.
        targetScore (int): The score a player needs to reach to win the game.
        playerName1 (str): Name of the first player.
        playerName2 (str): Name of the second player.
    """

    def __init__(self, rowNum, colNum, connectN, targetScore, playerName1, playerName2) -> None:
        self.__connectN = connectN
        self.__targetScore = targetScore
        self.__player1 = Player(playerName1, Notation.PLAYER1, 0)
        self.__player2 = Player(playerName2, Notation.PLAYER2, 0)
        self.__board = Board(rowNum, colNum)
        self.__board.initGrid()
        self.__playerList = [self.__player1, self.__player2]
        self.__curPlayer = self.__player1

    def __playBoard(self, curPlayer):
        """Handles the process of a player making a move on the board.

        Args:
            curPlayer (Player): The current player who is making the move.
        """
        isPlaced = False
        while not isPlaced:
            try:
                colNum = input(f"{curPlayer.getName()}, please enter the column number: ")
                # Check if the input is an integer and not a leading zero integer
                if colNum.isdigit() and not colNum.startswith('0'):
                    colNum = int(colNum)
                elif int(colNum) == 0:
                    colNum = int(colNum)
                else:
                    print("Error: Invalid input. Please enter a valid column number.")
                    continue
            except ValueError:
                print("Error: Invalid input. Please enter a valid column number.")
                continue

            if colNum < 0 or colNum >= self.__board.getColNum():
                print("Error: Invalid column number.")
                continue
            self.__board.placeMark(colNum, curPlayer.getNotation())
            isPlaced = True

    def __changeTurn(self):
        """Switches the turn to the other player."""
        if self.__curPlayer == self.__player1:
            self.__curPlayer = self.__player2
        else:
            self.__curPlayer = self.__player1

    def playRound(self):
        """Plays a single round of the game."""
        curWinnerNotation = None
        self.__board.initGrid()
        self.__curPlayer = self.__playerList[0]
        print("Starting a new round...")
        while curWinnerNotation is None:
            self.__curPlayer.display()
            self.__board.display()
            self.__playBoard(self.__curPlayer)
            if self.__board.checkWin(self.__connectN) is not None:
                print(f"{self.__curPlayer.getName()} wins!")
                self.__board.display() 
                curWinnerNotation = self.__curPlayer.getNotation()
                self.__curPlayer.addScoreByOne()
                break
            if self.__board.checkFull() and curWinnerNotation is None:
                print("The Board is Full!\nThe game is a tie!")
                break
            self.__changeTurn()


    def play(self):
        """Starts and manages the game play until a player wins."""
        while self.__player1.getScore() < self.__targetScore and self.__player2.getScore() < self.__targetScore:
            self.playRound()
            if self.__player1.getScore() == self.__targetScore or self.__player2.getScore() == self.__targetScore:
                print("Game Over!")
            print(self.__player1.display())
            print(self.__player2.display())

def main():
    """Main function to start the game."""
    game = Game(4, 4, 3, 2, 'P1', 'P2')
    game.play()

if __name__ == "__main__":
    main()
