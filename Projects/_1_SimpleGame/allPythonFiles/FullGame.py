import random
import numpy as np
import sys
import os

# Picture Puzzle

def main():
    game_end = False
    num2 = 0

    arr = np.array(random.sample(range(9), 9))

    fin = np.arange(9)
    fin = np.delete(fin, 0)
    fin = np.append(fin, 0)

    arr = np.array([1, 2, 3, 4, 5, 6, 7, 0, 8])  # for TESTING

    m_arr = np.reshape(arr, (-1, 3))
    fin = np.reshape(fin, (-1, 3))

    printArr(m_arr)

    while not game_end:

        num1 = getNum1()

        posm1 = np.where(m_arr == int(num1))
        posm2 = np.where(m_arr == int(num2))

        posm1r = int(posm1[0])
        posm1c = int(posm1[1])
        posm2r = int(posm2[0])
        posm2c = int(posm2[1])

        # get index of 2d array m_arr
        # check if swap is possible

        # if next to col and same row
        if(posm2c == posm1c + 1 or posm2c == posm1c - 1) and posm2r == posm1r:
            m_arr[posm1r][posm1c], m_arr[posm2r][posm2c] = m_arr[posm2r][posm2c], m_arr[posm1r][posm1c]

        # if next to row and same col
        elif (posm2r == posm1r + 1 or posm2r == posm1r - 1) and posm2c == posm1c:
            m_arr[posm1r][posm1c], m_arr[posm2r][posm2c] = m_arr[posm2r][posm2c], m_arr[posm1r][posm1c]

        else:
            print("\nThe two numbers are not next to each other ^^")

      
        printArr(m_arr)

        if np.array_equal(m_arr, fin):
            game_end = True      
            print("\nGame Finished! RIGHT ORDER ^^\n")


def getNum1():

    num1 = input("Enter num to switch with 0 ^^: ")

    while not num1.isnumeric():
        print("\n\tENTER A NUMBER (no letter!!) 1-8\n")
        num1 = input("Enter num to switch with 0 ^^: ")

    while int(num1) > 8:
        print("\n\tENTER A NUMBER BETWEEN 1 AND 8\n")
        num1 = input("Enter num to switch with 0 ^^: ")

    return num1


def printArr(arr):
    clear()
    sArr = ""
    
    arr = np.reshape(arr, (-1))
    for i in arr:
        sArr += str(i)
    sArr = sArr.replace("0", " ")
    
    print()
    for i in range(9):
        sysPrint(" " + sArr[i] + " ")

        if (i+1) % 3 == 0:
            sysPrint('\n')
    print()


def sysPrint(str):
    sys.stdout.write(str)
    sys.stdout.flush()


def clear(): 
    return os.system('cls')


if __name__ == '__main__':
    main()
