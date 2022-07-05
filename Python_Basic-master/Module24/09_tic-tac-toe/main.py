class Cell:
    def __init__(self, index):
        self.index = index
        self.status = True
        self.value = '-'


class Board:
    def __init__(self):
        self.board = [Cell(i) for i in range(0, 9)]


class Player:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def step(self, index, board):
        if board.board[index].status:
            board.board[index].value = self.value
            board.board[index].status = False
            if self.win(self.value, board):
                print(f'Win {self.name} player!!')
                return False
            else:
                return True
        else:
            raise IndexError(f'Cell {index} not empty')

    def win(self, val, board):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for i in win_coord:
            if board.board[i[0]].value == board.board[i[1]].value == board.board[i[2]].value == val:
                return True


class Game:
    def __init__(self):
        self.pl1 = Player(input('Enter first player name'), 'X')
        self.pl2 = Player(input('Enter second player name'), 'O')
        self.board = Board()
        for i in range(1, 10):
            if i % 2 == 1:
                x = self.pl1.step(int(input(f'{self.pl1.name} Enter Cell number')), self.board)
                if not x:
                    break
            else:
                x = self.pl2.step(int(input(f'{self.pl2.name} Enter Cell number')), self.board)
                if not x:
                    break
            self.printer(self.board.board)

    def printer(self, board):
        for i in board:
            print(f'{i.index}, {i.value}')


Game()


