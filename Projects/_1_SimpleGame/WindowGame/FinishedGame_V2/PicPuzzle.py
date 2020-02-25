import random
import numpy as np
import sys
import os
import tkinter as tk


class PicPuzzle:

    def __init__(self, level):

        self.LEVEL = level
        self.game_end = False
        self.num2 = 0
        self.resetArr()

        arr = np.array(random.sample(
            range(self.LEVEL*self.LEVEL), self.LEVEL*self.LEVEL))
        # arr = np.array([1, 2, 3, 4, 5, 6, 7, 0, 8])  # for TESTING
        #arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 15])  # for TESTING
        self.__m_arr = np.reshape(arr, (-1, self.LEVEL))

    def startConsole(self):
        #self.printArr(self.__m_arr)
        self.clear()
        print(self.__m_arr)
        self.game_end = False
        self.runConsole()

    def writeLogFile(self, fileName, strLog, strOperation):
        f = open(fileName, strOperation)
        f.write(strLog + "\n\n")
        f.close()

    def stop(self):
        print("\n\tbye\n")
        exit()

    def runConsole(self):

        while not self.game_end:

            self.num1 = self.getNum1()

            posm1 = np.where(self.__m_arr == self.num1)
            posm2 = np.where(self.__m_arr == self.num2)

            posm1r = int(posm1[0])
            posm1c = int(posm1[1])
            posm2r = int(posm2[0])
            posm2c = int(posm2[1])

            # get index of 2d array m_arr
            # check if swap is possible
            # if next to col and same row
            if(posm2c == posm1c + 1 or posm2c == posm1c - 1) and posm2r == posm1r:
                self.__m_arr[posm1r][posm1c], self.__m_arr[posm2r][posm2c] = self.__m_arr[posm2r][posm2c], self.__m_arr[posm1r][posm1c]

            # if next to row and same col
            elif (posm2r == posm1r + 1 or posm2r == posm1r - 1) and posm2c == posm1c:
                self.__m_arr[posm1r][posm1c], self.__m_arr[posm2r][posm2c] = self.__m_arr[posm2r][posm2c], self.__m_arr[posm1r][posm1c]

            else:
                print("\nThe two numbers are not next to each other ^^")

            #self.printArr(self.__m_arr)
            self.clear()
            print(self.__m_arr)

            if np.array_equal(self.__m_arr, self.__fin):
                self.game_end = True
                print("\nGame Finished! RIGHT ORDER ^^\n")

    def checkWindow(self, pressedBtnNum):

        self.num1 = pressedBtnNum

        posm1 = np.where(self.__m_arr == self.num1)
        posm2 = np.where(self.__m_arr == self.num2)

        posm1r = int(posm1[0])
        posm1c = int(posm1[1])
        posm2r = int(posm2[0])
        posm2c = int(posm2[1])

        if(posm2c == posm1c + 1 or posm2c == posm1c - 1) and posm2r == posm1r:
            self.__m_arr[posm1r][posm1c], self.__m_arr[posm2r][posm2c] = self.__m_arr[posm2r][posm2c], self.__m_arr[posm1r][posm1c]

        # if next to row and same col
        elif (posm2r == posm1r + 1 or posm2r == posm1r - 1) and posm2c == posm1c:
            self.__m_arr[posm1r][posm1c], self.__m_arr[posm2r][posm2c] = self.__m_arr[posm2r][posm2c], self.__m_arr[posm1r][posm1c]

        if np.array_equal(self.__m_arr, self.__fin):
            self.game_end = True
            print("\nGame Finished! RIGHT ORDER ^^\n")

    def changeLevel(self, i):
        self.LEVEL = i

    def restartGame(self):
        self.game_end = False
        print("\nRestart Game!\n")
        self.resetArr()

    def resetArr(self):

        arr = np.array(random.sample(
            range(self.LEVEL*self.LEVEL), self.LEVEL*self.LEVEL))

        self.__fin = np.arange(self.LEVEL*self.LEVEL)
        self.__fin = np.delete(self.__fin, 0)
        self.__fin = np.append(self.__fin, 0)

        self.__m_arr = np.reshape(arr, (-1, self.LEVEL))
        self.__fin = np.reshape(self.__fin, (-1, self.LEVEL))

    def getNum1(self):
        sNum = input("Enter num to switch with 0 ^^: ")

        if(sNum == "exit"):
            self.stop()

        while not sNum.isnumeric():
            print("\n\tENTER A NUMBER (no letter!!) 1-" +
                  str(self.LEVEL*self.LEVEL-1) + "\n")
            num1 = input("Enter num to switch with 0 ^^: ")

        num1 = int(sNum)

        while num1 > (self.LEVEL*self.LEVEL-1):
            print("\n\tENTER A NUMBER BETWEEN 1 AND " +
                  str(self.LEVEL*self.LEVEL-1) + "\n")
            num1 = input("Enter num to switch with 0 ^^: ")

        return num1

    def printArr(self, arr):
        self.clear()
        sArr = ""
        arr = np.reshape(arr, (-1))

        for i in arr:
            sArr += str(i)

        sArr = sArr.replace("0", " ")

        print()
        for i in range(self.LEVEL*self.LEVEL):
            self.sysPrint(" " + sArr[i] + " ")
            if (i+1) % self.LEVEL == 0:
                self.sysPrint('\n')
        print()

    def sysPrint(self, str):
        sys.stdout.write(str)
        sys.stdout.flush()

    def clear(self):
        return os.system('cls')

    def getPuzzle(self):
        return self.__m_arr
