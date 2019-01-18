# import an GUI package
from tkinter import *

import tkinter.messagebox as messagebox
import random

# create an class named Application, hold all Widget
playerChoiceList = []


class Application(Frame):
    # init all app
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    # hold all button and text
    def createWidgets(self):


        self.rockButton = Button(self, text='Rock', command=self.Rock)
        self.scissorsButton = Button(self, text='Scissors', command=self.scissors)
        self.PaperButton = Button(self, text='Paper', command=self.Paper)

        # button layout
        self.rockButton.pack()
        self.scissorsButton.pack()
        self.PaperButton.pack()



    # player choose rock
    def Rock(self):
        playerChoice = "Rock"
        playerChoiceList.append('0')
        self.computeWin(playerChoice)

    # player choose scissors
    def scissors(self):
        playerChoice = "scissors"
        self.computeWin(playerChoice)

    # player choose Paper
    def Paper(self):
        playerChoice = "Paper"
        self.computeWin(playerChoice)



    def computeWin(self,playerChoice):
        # for computer 0 = rock, 1 = scissors, 2 = Paper
        print("Your choice: " + playerChoice)

        # random a number
        computerChoice = random.randint(0, 2)

        # print a number
        if computerChoice == 0 :
            print("computer Rock")
        elif computerChoice == 1 :
            print("computer scissors")
        elif computerChoice == 2 :
            print("computer Paper")

        if ((playerChoice == "Rock")and(computerChoice == 0))or((playerChoice == "scissors") and (computerChoice == 1))or((playerChoice == "Paper") and (computerChoice == 2)):
            messagebox.showinfo('Win or Loss', 'Draw')

        if ((playerChoice == "Rock")and(computerChoice == 1))or((playerChoice == "scissors") and (computerChoice == 2))or((playerChoice == "Paper") and (computerChoice == 0)):
            messagebox.showinfo('Win or Loss', 'Win')

        if ((playerChoice == "Rock")and(computerChoice == 2))or((playerChoice == "scissors") and (computerChoice == 0))or((playerChoice == "Paper") and (computerChoice == 1)):
            messagebox.showinfo('Win or Loss', 'Loss')

app = Application()

# Set title
app.master.title('Guss can you win')
# main loop
app.mainloop()