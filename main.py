import tkinter as tk
from games import number_guessing_game, rock_paper_scissors, tic_tac_toe, word_guessing, hangman

def open_game(game_function):
    game_function()

# Main Window
root = tk.Tk()
root.title("Game Hub")
root.geometry("300x450")
root.configure(bg="lightblue")

tk.Label(root, text="Game Hub 🎮", font=("Arial", 16, "bold"), bg="lightblue").pack(pady=20)

# Buttons to launch games
games = [
    ("Number Guessing", number_guessing_game),
    ("Rock Paper Scissors", rock_paper_scissors),
    ("Tic-Tac-Toe", tic_tac_toe),
    ("Word Guessing (Hangman)", word_guessing),
    ("Hangman (Full Version)", hangman),
]

for game_name, game_func in games:
    tk.Button(root, text=game_name, font=("Arial", 12), width=25, command=lambda f=game_func: open_game(f)).pack(pady=5)

root.mainloop()
