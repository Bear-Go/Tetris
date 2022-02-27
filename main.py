import tkinter as tk
from window import TetrisWindow


def main():
    root = tk.Tk()
    game = TetrisWindow(master = root)
    root.title('Tetris')
    root.iconbitmap('./images/T.ico')
    game.mainloop()


if __name__ == '__main__':
    main()