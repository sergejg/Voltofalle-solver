import numpy as np
import itertools as iter

from numpy.lib.arraysetops import unique
from numpy.lib.function_base import append


def getPossibleCombinations(numberOfZeros, sumOfNumbers):

    numberCombination = iter.combinations(
        [1]*(5-numberOfZeros)+[2]*(5-numberOfZeros)+[3]*(5-numberOfZeros), 5-numberOfZeros)
    numberCombinationList = list(dict.fromkeys(numberCombination))

    pickList = []
    for i in numberCombinationList:

        if (sum(i) == sumOfNumbers):
            pickList = pickList + [1]
        else:
            pickList = pickList + [0]

    filteredNumberCombinations = list(
        iter.compress(numberCombinationList, pickList))

    permTemp = []

    for i in filteredNumberCombinations:
        filteredNumberCombinationsList = list(i)+[0]*numberOfZeros
        permTemp = permTemp + \
            list(iter.permutations(filteredNumberCombinationsList))

    permutations = np.array(permTemp)

    unique, index = np.unique(permutations, axis=0, return_index=True)
    return unique


def inputText():
    inputText = ["SUMS for Rows", "number of BOMBS for Rows",
                 "SUMS for Columns", "number of BOMBS for Columns"]
    inputNumbers = np.empty((0, 5), int)
    '''for i in inputText:

        a = input("Type "+i+" seperated bei <space>:")
        print(a)
        l = a.split()
        print(l)
        inputNumbers = np.append(inputNumbers, np.array([[int(char) for char in l]]),
        axis=0)
        print(inputNumbers)

    print(inputNumbers)'''

    inputNumbers = np.array([[4, 5, 6, 4, 6],
                             [1, 2, 1, 1, 1],
                             [8, 3, 4, 4, 6],
                             [1, 2, 1, 1, 1]])
    inputNumbersForRows = np.transpose(inputNumbers[0:2, :])
    print("Rows:\n", inputNumbersForRows)
    inputNumbersForCols = np.transpose(inputNumbers[2:4, :])
    print("Cols:\n", inputNumbersForCols)
    return inputNumbersForRows, inputNumbersForCols


if __name__ == "__main__":
    '''sumOfNumbers = 4
    numberOfZeros = 3

    print("______________________")
    r0 = getPossibleCombinations(numberOfZeros, sumOfNumbers)
    print(r0)'''
    rows, cols = inputText()
    allPosabilities = []
    for i in rows:
        print(i)
        possibleCombinations = getPossibleCombinations(i[1], i[0])
        #possibleCombinations = np.array([possibleCombinations])
        allPosabilities = allPosabilities+[possibleCombinations]

    possibleResultTemps = []
    for i0 in allPosabilities[0]:
        # print(i0)
        for i1 in allPosabilities[1]:
            # print(i1)
            for i2 in allPosabilities[2]:
                # print(i2)
                for i3 in allPosabilities[3]:
                    # print(i3)
                    for i4 in allPosabilities[4]:
                        # print(i4)
                        possibleResult = np.array([i0, i1, i2, i3, i4])
                        sumCols = np.sum(possibleResult, axis=0)
                        numberOfZerosCols = np.array([
                            np.count_nonzero(possibleResult[:, 0] == 0),
                            np.count_nonzero(possibleResult[:, 1] == 0),
                            np.count_nonzero(possibleResult[:, 2] == 0),
                            np.count_nonzero(possibleResult[:, 3] == 0),
                            np.count_nonzero(possibleResult[:, 4] == 0),
                        ])
                        resultCols = np.transpose(
                            np.array([sumCols, numberOfZerosCols])
                        )
                        if (resultCols==cols).all():
                            possibleResultTemp = np.array(possibleResult)
                            possibleResultTemp[np.where(possibleResult==1)]=0
                            if len(possibleResultTemps)==0:
                                print("             ")
                                print(possibleResultTemp)
                                print("             ")
                                print("----------------")
                                possibleResultTemps = possibleResultTemps + [possibleResultTemp]
                            else:
                                contained = []
                                for k in possibleResultTemps:
                                    if (k==possibleResultTemp).all():
                                        contained = contained + [True]
                                if not(any(contained)):
                                    print("             ")
                                    print(possibleResultTemp)
                                    print("             ")
                                    print("----------------")
                                    possibleResultTemps = possibleResultTemps + [possibleResultTemp]        

                            
                            

                        #print((resultCols==cols).all())
                        #print(possibleResult)
    print("done!")
