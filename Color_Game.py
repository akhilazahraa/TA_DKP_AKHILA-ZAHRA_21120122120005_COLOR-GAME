import tkinter
from tkinter import ttk
import random
import threading
import time

class ColorGame:
    def __init__(self):
        self.colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
        self.score = 0
        self.timeleft = 30
        self.mistakes = 0
        self.questions_played = 0
        
        self.root = tkinter.Tk()
        self.root.title("COLORGAME")
        self.root.geometry("1920x1080")
        self.root.configure(bg="#FCF4DD")

        self.instructions = tkinter.Label(self.root, text="Ketiklah warna kata, dan bukan teks kata!", font=('Bakso Sapi', 30), bg="#FCE1E4")
        self.instructions.pack(pady=20)

        self.scoreLabel = tkinter.Label(self.root, text="Tekan enter untuk mulai", font=('Bakso Sapi', 30), bg="#DDEDEA")
        self.scoreLabel.pack(pady=20)

        self.timeLabel = tkinter.Label(self.root, text="Time left: " + str(self.timeleft), font=('Bakso Sapi', 30), bg="#E8DFF5")
        self.timeLabel.pack(pady=20)

        self.label = tkinter.Label(self.root, font=('Bakso Sapi', 80))
        self.label.pack(pady=20)

        self.e = tkinter.Entry(self.root)
        self.root.bind('<Return>', self.startGame)
        self.e.pack(pady=20)

        self.e.focus_set()

    def startGame(self, event):
        if self.timeleft == 30:
            self.countdown()
        self.nextColour()

    def nextColour(self):
        if self.timeleft > 0:
            self.e.focus_set()
            if self.e.get().lower() == self.colours[1].lower():
                self.score += 1
            else:    
                self.mistakes += 1
            self.e.delete(0, tkinter.END)
            random.shuffle(self.colours)
            self.label.config(fg=str(self.colours[1]), text=str(self.colours[0]))
            self.scoreLabel.config(text="Score: " + str(self.score))
            self.questions_played +=1
            
    def countdown(self):
        if self.timeleft > 0:
            self.timeleft -= 1
            self.timeLabel.config(text="Time left: " + str(self.timeleft))
            self.timeLabel.after(1000, self.countdown)
        else:
            self.root.destroy()
            resultWindow = GameResult(self.score, self.mistakes, self.questions_played)
            resultWindow.mainloop()

class GameResult(tkinter.Tk):
    def __init__(self, score, mistakes, questions_played):
        super().__init__()
        self.title("Game Result")
        self.geometry("1920x1080")
        self.resultLabel = tkinter.Label(self, text="Final Score: " + str(score), font=('Bakso Sapi', 30), bg="#DDEDEA")
        self.resultLabel.pack(pady=20)
        self.mistakesLabel = tkinter.Label(self, text="Mistakes: " + str(mistakes), font=('Bakso Sapi', 30), bg="#DDEDEA")
        self.mistakesLabel.pack(pady=20)
        self.questionsLabel = tkinter.Label(self, text="Questions Played: " + str(questions_played), font=('Bakso Sapi', 30), bg="#DDEDEA")
        self.questionsLabel.pack(pady=20)
def play_game():
    loading_window = tkinter.Tk()
    loading_window.title("Loading")
    loading_window.geometry("1920x1080")
    loading_label = tkinter.Label(loading_window, text="Loading...:)", font=('Bakso Sapi', 40))
    loading_label.pack(pady=200)
    loading_window.update()
    
    time.sleep(2)

    game = ColorGame()
    game_thread = threading.Thread(target=game.root.mainloop)
    game_thread.start()

    loading_window.destroy()

    game_thread.join()

    resultWindow = GameResult(game.score, game.mistakes, game.questions_played)
    resultWindow.mainloop()

play_game()
