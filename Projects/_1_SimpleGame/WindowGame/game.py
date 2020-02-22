from PicPuzzle import PicPuzzle
import tkinter as tk 
import tkinter.font
from tkinter import messagebox



WIDTH = 400
HEIGHT = 400
OFFSETR = 200
OFFSETL = 200
LEVEL = 4
p = PicPuzzle(LEVEL)
m_arr = p.getPuzzle()



def main():

    # p.startConsole()
    root = tk.Tk()
    root.title("Pic Puzzle")
    root.geometry("+{0}+{1}".format(OFFSETR, OFFSETL))

    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack()

    frameBG = tk.Frame(root, bg='#1B2021')
    frameBG.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    frameBtns = tk.Frame(frameBG, bg='#1B2021')
    frameBtns.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)

    helv36 = tkinter.font.Font(family='Arial', size=int(100/LEVEL), weight='bold')

    print(m_arr)
    btns = [[None for _ in range(LEVEL)] for _ in range(LEVEL)]

    for i in range(LEVEL):
        for j in range(LEVEL):
            btns[i][j] = tk.Button(frameBtns, text=getNum(m_arr[j][i]), bg="#EEB868", fg="#1B2021",
                                   activebackground="#FFEED6", activeforeground="#11151C",
                                   font=helv36, command=lambda i=i, j=j: btn_clicked(btns, btns[i][j]))
            btns[i][j].place(relx=(i*1/LEVEL-0.05) + 0.05, rely=((j *1/LEVEL-0.05) + 0.05), relwidth=1/LEVEL, relheight=1/LEVEL)

    root.mainloop()


def btn_clicked(btns, pressed_btn):

    for i in range(LEVEL*LEVEL):
        #check num of pressed button
        
        if pressed_btn.cget("text") == "{0}".format(i):
            print("Button {0} pressed".format(i))

            p.checkWindow(i) 
            m_arr = p.getPuzzle()
            print(m_arr)
           
            # rename btn names to __m_arr names ^^
            renameBtns(btns,pressed_btn, m_arr)
            

            if p.game_end == True:
                MsgBox = tk.messagebox.askquestion(title='Game Finished', message='Restart Game With Yes, Exit with No', )
                if MsgBox == 'yes':
                    p.restartGame()
                    m_arr = p.getPuzzle()
                    p.checkWindow(i)
                    print(m_arr)
                    # rename btn names to __m_arr names ^^
                    renameBtns(btns, pressed_btn, m_arr)
                else:
                    exit()
                     
            
def renameBtns(btns,pressed_btn, arr):
    for i in range(LEVEL):
        for j in range(LEVEL):
            btns[i][j].config(text=getNum(arr[j][i]))



def getNum(x):
    if x == 0:
        return ""
    else:
        return str(x)

if __name__ == '__main__':
    main()
