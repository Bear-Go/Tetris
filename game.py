class Tetris:
    def __init__(self):
        self.speed = 0
        self.score = 0
        self.x = 6
        self.y = 1
        self.board = [[0 for _ in range(15)] for _ in range(15)]

    def player(self, input_by_window=False, move=None):
        # 如果有上下左右按下，则根据当前位置，判断下一时刻位置
        if not input_by_window:
            move = int(input('move: '))
        if move == 2:
            self.x -= 1
        elif move == 4:
            self.x += 1

    def check(self):

        return 0

    def show(self):
        for i in range(15):
            print('|', end='')

            for j in range(15):
                if self.board[i][j] == 0:
                    print(' ', end='')
                elif self.board[i][j] == 1:
                    print('*', end='')
                elif self.board[i][j] == 2:
                    print('+', end='')

            print('|\n', end='')

        for i in range(15):
            print('-', end='')
        print('--\n', end='')

    def play(self):
        while True:
            self.show()
            self.player()
