import tkinter as tk
from game import Tetris
COLORS = ['silver', 'yellow', 'orange', 'blue', 'red', 'purple', 'green', 'cyan']


class TetrisWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.status_msg = None
        self.game_over_msg = None
        self.canvas = None
        self.rectangles = None
        self.tetris = Tetris()
        self.pack()
        self.create_widgets()
        self.update_clock()

    def update_clock(self):
        self.tetris.move(1, 0)
        self.update()
        self.master.after(int(1000 * (0.66 ** self.tetris.level)), self.update_clock)

    def create_widgets(self):
        PIECE_SIZE = 30
        self.canvas = tk.Canvas(self, height=PIECE_SIZE * self.tetris.FIELD_HEIGHT,
                                width=PIECE_SIZE * self.tetris.FIELD_WIDTH, bg="black", bd=0)
        self.canvas.bind('<Left>', lambda _: (self.tetris.move(0, -1), self.update()))
        self.canvas.bind('<Right>', lambda _: (self.tetris.move(0, 1), self.update()))
        self.canvas.bind('<Down>', lambda _: (self.tetris.move(1, 0), self.update()))
        self.canvas.bind('<Up>', lambda _: (self.tetris.rotate(), self.update()))
        self.canvas.focus_set()
        self.rectangles = [
            self.canvas.create_rectangle(c * PIECE_SIZE, r * PIECE_SIZE, (c + 1) * PIECE_SIZE, (r + 1) * PIECE_SIZE)
            for r in range(self.tetris.FIELD_HEIGHT) for c in range(self.tetris.FIELD_WIDTH)
        ]
        self.canvas.pack(side="left")
        self.status_msg = tk.Label(self, anchor='w', width=11, font=("Consoles", 24))
        self.status_msg.pack(side="top")
        self.game_over_msg = tk.Label(self, anchor='w', width=11, font=("Consoles", 24), fg='red')
        self.game_over_msg.pack(side="top")

    def update(self):
        for i, _id in enumerate(self.rectangles):
            color_num = self.tetris.get_color(i // self.tetris.FIELD_WIDTH, i % self.tetris.FIELD_WIDTH)
            self.canvas.itemconfig(_id, fill=COLORS[color_num])

        self.status_msg['text'] = "Score: {}\nLevel: {}".format(self.tetris.score, self.tetris.level)
        self.game_over_msg['text'] = "GAME OVER.\nPress UP\nto reset" if self.tetris.game_over else ""