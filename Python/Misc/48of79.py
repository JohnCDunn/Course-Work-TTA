
numList=[67,45,2,13,998]

print('before sort list = ' + str(numList))

def bubble_sort(numList):
    """ Implementation of bubble sort """
    for i in range(len(numList)):
        for j in range(len(numList)-1-i):
            if numList[j] > numList[j+1]:
                numList[j], numList[j+1] = numList[j+1], numList[j]

    print('afters sort list = ' + str(numList))

bubble_sort(numList)
