from tkinter import *
from tkinter.messagebox import *


class demo:
    def checkwin(self):
        if self.bt1["text"] == "O" and self.bt2["text"] == "O" and self.bt3["text"] == "O":

            self.bt1["bg"] = "rosy brown1"
            self.bt2["bg"] = "rosy brown1"
            self.bt3["bg"] = "rosy brown1"
            showinfo("TIC TAC TOE", "PLAYER 1 WINS")
            self.reset()


        elif self.bt4["text"] == "O" and self.bt5["text"] == "O" and self.bt6["text"] == "O":

            self.bt4["bg"] = "rosy brown1"
            self.bt5["bg"] = "rosy brown1"
            self.bt6["bg"] = "rosy brown1"
            showinfo("TIC TAC TOE", "PLAYER 1 WINS")
            self.reset()





        elif self.bt7["text"] == "O" and self.bt8["text"] == "O" and self.bt9["text"] == "O":

            self.bt7["bg"] = "rosy brown1"
            self.bt8["bg"] = "rosy brown1"
            self.bt9["bg"] = "rosy brown1"
            showinfo("TIC TAC TOE", "PLAYER 1 WINS")
            self.reset()


        elif self.bt1["text"] == "O" and self.bt4["text"] == "O" and self.bt7["text"] == "O":

            self.bt1["bg"] = "rosy brown1"
            self.bt4["bg"] = "rosy brown1"
            self.bt7["bg"] = "rosy brown1"
            showinfo("TIC TAC TOE", "PLAYER 1 WINS")
            self.reset()

        elif self.bt2["text"] == "O" and self.bt5["text"] == "O" and self.bt8["text"] == "O":

            self.bt2["bg"] = "rosy brown1"
            self.bt5["bg"] = "rosy brown1"
            self.bt8["bg"] = "rosy brown1"
            showinfo("TIC TAC TOE", "PLAYER 1 WINS")
            self.reset()


        elif self.bt3["text"] == "O" and self.bt6["text"] == "O" and self.bt9["text"] == "O":

            self.bt3["bg"] = "rosy brown1"
            self.bt6["bg"] = "rosy brown1"
            self.bt9["bg"] = "rosy brown1"
            showinfo("TIC TAC TOE", "PLAYER 1 WINS")

            self.reset()


        elif self.bt1["text"] == "O" and self.bt5["text"] == "O" and self.bt9["text"] == "O":

            self.bt1["bg"] = "rosy brown1"
            self.bt5["bg"] = "rosy brown1"
            self.bt9["bg"] = "rosy brown1"
            showinfo("TIC TAC TOE", "PLAYER 1 WINS")
            self.reset()

        elif self.bt3["text"] == "O" and self.bt5["text"] == "O" and self.bt7["text"] == "O":

            self.bt3["bg"] = "rosy brown1"
            self.bt5["bg"] = "rosy brown1"
            self.bt7["bg"] = "rosy brown1"

            showinfo("TIC TAC TOE", "PLAYER 1 WINS")
            self.reset()


        elif self.bt1["text"] == "X" and self.bt2["text"] == "X" and self.bt3["text"] == "X":

            self.bt1["bg"] = "rosy brown3"
            self.bt2["bg"] = "rosy brown3"
            self.bt3["bg"] = "rosy brown3"
            showinfo("TIC TAC TOE", "PLAYER 2 WINS")

            self.reset()


        elif self.bt4["text"] == "X" and self.bt5["text"] == "X" and self.bt6["text"] == "X":

            self.bt4["bg"] = "rosy brown3"
            self.bt5["bg"] = "rosy brown3"
            self.bt6["bg"] = "rosy brown3"
            showinfo("TIC TAC TOE", "PLAYER 2 WINS")

            self.reset()

        elif self.bt7["text"] == "X" and self.bt8["text"] == "X" and self.bt9["text"] == "X":

            self.bt7["bg"] = "rosy brown3"
            self.bt8["bg"] = "rosy brown3"
            self.bt9["bg"] = "rosy brown3"
            showinfo("TIC TAC TOE", "PLAYER 2 WINS")
            self.reset()

        elif self.bt1["text"] == "X" and self.bt4["text"] == "X" and self.bt7["text"] == "X":

            self.bt1["bg"] = "rosy brown3"
            self.bt4["bg"] = "rosy brown3"
            self.bt7["bg"] = "rosy brown3"
            showinfo("TIC TAC TOE", "PLAYER 2 WINS")

            self.reset()

        elif self.bt2["text"] == "X" and self.bt5["text"] == "X" and self.bt8["text"] == "X":

            self.bt2["bg"] = "rosy brown3"
            self.bt5["bg"] = "rosy brown3"
            self.bt8["bg"] = "rosy brown3"
            showinfo("TIC TAC TOE", "PLAYER 2 WINS")
            self.reset()

        elif self.bt3["text"] == "X" and self.bt6["text"] == "X" and self.bt9["text"] == "X":

            self.bt3["bg"] = "rosy brown3"
            self.bt6["bg"] = "rosy brown3"
            self.bt9["bg"] = "rosy brown3"
            showinfo("TIC TAC TOE", "PLAYER 2 WINS")
            self.reset()

        elif self.bt1["text"] == "X" and self.bt5["text"] == "X" and self.bt9["text"] == "X":

            self.bt1["bg"] = "rosy brown3"
            self.bt5["bg"] = "rosy brown3"
            self.bt9["bg"] = "rosy brown3"
            showinfo("TIC TAC TOE", "PLAYER 2 WINS")
            self.reset()


        elif self.bt3["text"] == "X" and self.bt5["text"] == "X" and self.bt7["text"] == "X":

            self.bt3["bg"] = "rosy brown3"
            self.bt5["bg"] = "rosy brown3"
            self.bt7["bg"] = "rosy brown3"

            showinfo("TIC TAC TOE", "PLAYER 2 WINS")
            self.reset()

    def reset(self):
        self.play = 0
        self.bt1["text"] = " "
        self.bt1["state"] = "normal"
        self.bt1["bg"] = "pink"

        self.bt2["text"] = " "
        self.bt2["state"] = "normal"
        self.bt2["bg"] = "pink"

        self.bt3["text"] = " "
        self.bt3["state"] = "normal"
        self.bt3["bg"] = "pink"

        self.bt4["text"] = " "
        self.bt4["state"] = "normal"
        self.bt4["bg"] = "pink"

        self.bt5["text"] = " "
        self.bt5["state"] = "normal"
        self.bt5["bg"] = "pink"

        self.bt6["text"] = " "
        self.bt6["state"] = "normal"
        self.bt6["bg"] = "pink"

        self.bt7["text"] = " "
        self.bt7["state"] = "normal"
        self.bt7["bg"] = "pink"

        self.bt8["text"] = " "
        self.bt8["state"] = "normal"
        self.bt8["bg"] = "pink"

        self.bt9["text"] = " "
        self.bt9["state"] = "normal"
        self.bt9["bg"] = "pink"

    def fire1(self):
        if self.play % 2 == 0:
            self.bt1["text"] = "O"
        else:
            self.bt1["text"] = "X"
        self.play = self.play + 1
        self.bt1["state"] = "disabled"
        self.checkwin()

    def fire2(self):
        if self.play % 2 == 0:
            self.bt2["text"] = "O"
        else:
            self.bt2["text"] = "X"
        self.play = self.play + 1
        self.bt2["state"] = "disabled"
        self.checkwin()

    def fire3(self):
        if self.play % 2 == 0:
            self.bt3["text"] = "O"
        else:
            self.bt3["text"] = "X"
        self.play = self.play + 1
        self.bt3["state"] = "disabled"
        self.checkwin()

    def fire4(self):
        if self.play % 2 == 0:
            self.bt4["text"] = "O"
        else:
            self.bt4["text"] = "X"
        self.play = self.play + 1
        self.bt4["state"] = "disabled"
        self.checkwin()

    def fire5(self):
        if self.play % 2 == 0:
            self.bt5["text"] = "O"
        else:
            self.bt5["text"] = "X"
        self.play = self.play + 1
        self.bt5["state"] = "disabled"
        self.checkwin()

    def fire6(self):
        if self.play % 2 == 0:
            self.bt6["text"] = "O"
        else:
            self.bt6["text"] = "X"
        self.play = self.play + 1
        self.bt6["state"] = "disabled"
        self.checkwin()

    def fire7(self):
        if self.play % 2 == 0:
            self.bt7["text"] = "O"
        else:
            self.bt7["text"] = "X"
        self.play = self.play + 1
        self.bt7["state"] = "disabled"
        self.checkwin()

    def fire8(self):
        if self.play % 2 == 0:
            self.bt8["text"] = "O"
        else:
            self.bt8["text"] = "X"
        self.play = self.play + 1
        self.bt8["state"] = "disabled"
        self.checkwin()

    def fire9(self):
        if self.play % 2 == 0:
            self.bt9["text"] = "O"
        else:
            self.bt9["text"] = "X"
        self.play = self.play + 1
        self.bt9["state"] = "disabled"
        self.checkwin()

    def __init__(self):
        self.play = 0
        self.root = Tk()

        self.root.configure(background="mint cream")

        self.root.geometry("800x800")

        self.bt1 = Button(self.root, text=" ", width=10, height=5, command=self.fire1, background="pink")
        self.bt2 = Button(self.root, text=" ", width=10, height=5, command=self.fire2, background="pink")
        self.bt3 = Button(self.root, text=" ", width=10, height=5, command=self.fire3, background="pink")

        self.bt4 = Button(self.root, text=" ", width=10, height=5, command=self.fire4, background="pink")
        self.bt5 = Button(self.root, text=" ", width=10, height=5, command=self.fire5, background="pink")
        self.bt6 = Button(self.root, text=" ", width=10, height=5, command=self.fire6, background="pink")

        self.bt7 = Button(self.root, text=" ", width=10, height=5, command=self.fire7, background="pink")
        self.bt8 = Button(self.root, text=" ", width=10, height=5, command=self.fire8, background="pink")
        self.bt9 = Button(self.root, text=" ", width=10, height=5, command=self.fire9, background="pink")
        self.bt10 = Button(self.root, text="RESET", command=self.reset, background="saddle brown")

        self.bt1.grid(row=0, column=0)
        self.bt2.grid(row=0, column=1)
        self.bt3.grid(row=0, column=2)

        self.bt4.grid(row=1, column=0)
        self.bt5.grid(row=1, column=1)
        self.bt6.grid(row=1, column=2)

        self.bt7.grid(row=2, column=0)
        self.bt8.grid(row=2, column=1)
        self.bt9.grid(row=2, column=2)
        self.bt10.grid(row=3, column=2)

        self.root.mainloop()


# ==============================================
obj = demo()


