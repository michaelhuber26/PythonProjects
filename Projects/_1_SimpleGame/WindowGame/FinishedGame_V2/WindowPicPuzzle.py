from PicPuzzle import PicPuzzle
import tkinter as tk
import tkinter.font
import os
from tkinter import messagebox


class WindowPicPuzzle:

    def __init__(self, LEVEL):

        WIDTH = 400
        HEIGHT = 400
        OFFSETR = 200
        OFFSETL = 200
        self.LEVEL = LEVEL
        self.p = PicPuzzle(self.LEVEL)
        self.LOGFILENAME = "log.txt"
        m_arr = self.p.getPuzzle()

        self.p.writeLogFile(self.LOGFILENAME, str(m_arr), "w")
        # self.p.startConsole()
        self.root = tk.Tk()
        self.root.title("Pic Puzzle")
        self.root.geometry("+{0}+{1}".format(OFFSETR, OFFSETL))

        canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT)
        canvas.pack()

        frameBG = tk.Frame(self.root, bg='#1B2021')
        frameBG.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        frameBtns = tk.Frame(frameBG, bg='#1B2021')
        frameBtns.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)

        helv36 = tkinter.font.Font(
            family='Arial', size=int(100/self.LEVEL), weight='bold')

        print(m_arr)
        btns = [[None for _ in range(self.LEVEL)] for _ in range(self.LEVEL)]

        for i in range(self.LEVEL):
            for j in range(self.LEVEL):
                btns[i][j] = tk.Button(frameBtns, text=self.getNum(m_arr[j][i]), bg="#EEB868", fg="#1B2021",
                                    activebackground="#FFEED6", activeforeground="#11151C",
                                       font=helv36, command=lambda i=i, j=j: self.btn_clicked(btns, btns[i][j]))
                btns[i][j].place(relx=(i*1/self.LEVEL-0.05) + 0.05, rely=((j *
                                                                    1/self.LEVEL-0.05) + 0.05), relwidth=1/self.LEVEL, relheight=1/self.LEVEL)

        

    def btn_clicked(self, btns, pressed_btn):

        for i in range(self.LEVEL*self.LEVEL):
            # check num of pressed button

            if pressed_btn.cget("text") == "{0}".format(i):
                print("Button {0} pressed".format(i))

                self.p.checkWindow(i)
                m_arr = self.p.getPuzzle()
                print(m_arr)
                self.p.writeLogFile(self.LOGFILENAME, str(m_arr), "a")

                # rename btn names to __m_arr names ^^
                self.renameBtns(btns, pressed_btn, m_arr)

                if self.p.game_end == True:
                    MsgBox = tk.messagebox.askquestion(
                        title='Game Finished', message='Restart Game With Yes, Exit with No', )
                    if MsgBox == 'yes':
                        self.p.restartGame()
                        m_arr = self.p.getPuzzle()
                        self.p.checkWindow(i)
                        print(m_arr)
                        self.p.writeLogFile(self.LOGFILENAME, str(m_arr), "w")

                        # rename btn names to __m_arr names ^^
                        self.renameBtns(btns, pressed_btn, m_arr)
                    else:
                        exit()

    def renameBtns(self, btns, pressed_btn, arr):
        for i in range(self.LEVEL):
            for j in range(self.LEVEL):
                btns[i][j].config(text=self.getNum(arr[j][i]))


    def getNum(self, x):
        if x == 0:
            return ""
        else:
            return str(x)

    def renameLogFile(self, strName):
        os.remove(self.LOGFILENAME)
        self.LOGFILENAME = strName
        

    def start(self):
        self.root.mainloop()

