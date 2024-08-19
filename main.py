import tkinter as tk
from View.GameGUI import GameGUI

def main():
    root = tk.Tk()
    game = GameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()