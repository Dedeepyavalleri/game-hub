import random
import tkinter as tk
from tkinter import messagebox, simpledialog


# 1️⃣ Number Guessing Game
def number_guessing_game():
    a_no = random.randint(1, 100)
    chances = 7
    c_no = 0

    while c_no < chances:
        g_no = simpledialog.askinteger("Number Guessing", "Enter your guess (1-100):")
        if g_no is None:
            return
        c_no += 1

        if g_no == a_no:
            messagebox.showinfo("Result", "Hurray! You guessed the right number! 🎉")
            return
        elif c_no >= chances:
            messagebox.showinfo("Result", f"You lost! The correct number was {a_no}.")
        elif g_no > a_no:
            messagebox.showwarning("Hint", "Your guess is too high!")
        else:
            messagebox.showwarning("Hint", "Your guess is too low!")


# 2️⃣ Rock Paper Scissors
def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    rounds = simpledialog.askinteger("Rock Paper Scissors", "Enter number of rounds:")

    if rounds is None:
        return

    for i in range(1, rounds + 1):
        user_choice = simpledialog.askstring("Rock Paper Scissors", "Enter Rock, Paper, or Scissors:").lower()
        computer_choice = random.choice(choices)

        if user_choice not in choices:
            messagebox.showerror("Error", "Invalid input! Try again.")
            continue

        if user_choice == computer_choice:
            messagebox.showinfo("Round Result", f"Round {i}: It's a Tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
            user_score += 1
            messagebox.showinfo("Round Result", f"Round {i}: You Win! 🎉")
        else:
            computer_score += 1
            messagebox.showinfo("Round Result", f"Round {i}: Computer Wins!")

    # Final Score
    if user_score > computer_score:
        messagebox.showinfo("Game Over", "Congratulations! You won the game. 🎉")
    elif user_score < computer_score:
        messagebox.showinfo("Game Over", "You lost! Better luck next time.")
    else:
        messagebox.showinfo("Game Over", "It's a tie!")


# 3️⃣ Tic-Tac-Toe
def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"

    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  # Diagonals
    ]

    def display_board():
        return f"""
        {board[0]} | {board[1]} | {board[2]}
        ---------
        {board[3]} | {board[4]} | {board[5]}
        ---------
        {board[6]} | {board[7]} | {board[8]}
        """

    def check_winner():
        for a, b, c in winning_combinations:
            if board[a] == board[b] == board[c] and board[a] != " ":
                return board[a]  # Return "X" or "O"
        if " " not in board:
            return "Tie"
        return None

    def minimax(board, is_maximizing):
        winner = check_winner()
        if winner == "X":
            return -1
        elif winner == "O":
            return 1
        elif winner == "Tie":
            return 0

        if is_maximizing:
            best_score = -float("inf")
            for i in range(9):
                if board[i] == " ":
                    board[i] = "O"
                    score = minimax(board, False)
                    board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(9):
                if board[i] == " ":
                    board[i] = "X"
                    score = minimax(board, True)
                    board[i] = " "
                    best_score = min(score, best_score)
            return best_score

    def best_move():
        best_score = -float("inf")
        move = None
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                if score > best_score:
                    best_score = score
                    move = i
        return move

    while True:
        # Player Move
        move = simpledialog.askinteger("Tic-Tac-Toe", f"Your turn (X)!\n{display_board()}\nEnter position (1-9):")
        if move is None:
            return
        move -= 1

        if move < 0 or move >= 9 or board[move] != " ":
            messagebox.showwarning("Invalid Move", "Choose an empty position between 1-9.")
            continue

        board[move] = "X"
        winner = check_winner()
        if winner:
            break

        # AI Move
        move = best_move()
        if move is not None:
            board[move] = "O"

        winner = check_winner()
        if winner:
            break

    # Show Final Result
    if winner == "X":
        messagebox.showinfo("Game Over", "Congratulations! You Win 🎉")
    elif winner == "O":
        messagebox.showinfo("Game Over", "You Lost! AI Wins 🤖")
    else:
        messagebox.showinfo("Game Over", "It's a Tie! 😃")


# 4️⃣ Word Guessing (Hangman)
def word_guessing():
    words = ["python", "tkinter", "gamehub", "coding", "hangman", "computer"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        display_word = "".join([char if char in guessed_letters else "_" for char in word])

        guess = simpledialog.askstring("Word Guessing", f"Guess a letter:\n{display_word}").lower()
        if not guess or len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            continue

        if guess in guessed_letters:
            messagebox.showwarning("Warning", "You've already guessed that letter.")
            continue

        guessed_letters.append(guess)
        if guess not in word:
            attempts -= 1
            messagebox.showinfo("Wrong Guess", f"Wrong guess! Attempts left: {attempts}")

        if all(char in guessed_letters for char in word):
            messagebox.showinfo("Result", f"Congratulations! You guessed the word: {word} 🎉")
            return

    messagebox.showinfo("Result", f"You lost! The word was '{word}'.")


# 5️⃣ Hangman (Full Version)
def hangman():
    words = ["developer", "python", "algorithm", "function", "variable"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6
    hangman_stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """
    ]

    while attempts > 0:
        display_word = "".join([char if char in guessed_letters else "_" for char in word])
        guess = simpledialog.askstring("Hangman",
                                       f"{hangman_stages[6 - attempts]}\n\nGuess a letter:\n{display_word}").lower()

        if not guess or len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            continue

        if guess in guessed_letters:
            messagebox.showwarning("Warning", "You've already guessed that letter.")
            continue

        guessed_letters.append(guess)
        if guess not in word:
            attempts -= 1

        if all(char in guessed_letters for char in word):
            messagebox.showinfo("Result", f"Congratulations! You guessed the word: {word} 🎉")
            return

    messagebox.showinfo("Result", f"You lost! The word was '{word}'.")
