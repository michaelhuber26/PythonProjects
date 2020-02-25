from WindowPicPuzzle import WindowPicPuzzle
from PicPuzzle import PicPuzzle
from datetime import datetime



def main():
    now = datetime.now()
    dt_string = now.strftime("--%d-%m-%Y--%H-%M-%S")  # --2009-12-31--23-59-59

    print('Enter LEVEL (1- 15)')
    level = input()

    level = int(level)
    
    

    print('Play in Console (Enter "1")')
    print('Play in Window  (Enter "2")')

    inputNum = input()
    inputNum = int(inputNum)

    if inputNum == 1:
        # cons Print (PicPuzzle printArr fixen)
        consPicPuzzle = PicPuzzle(level)
        consPicPuzzle.startConsole()

    elif inputNum == 2:
        winPicPuzzle = WindowPicPuzzle(level)
        winPicPuzzle.renameLogFile("Log-File" + dt_string + ".txt")
        winPicPuzzle.start()
    

    

if __name__ == '__main__':
    main()
