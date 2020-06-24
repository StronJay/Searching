test, k = [102, 41, 58, 81, 2, -5, 1000, 10021, 181, -14515, 25, 15], 5


def quickselect(array, k):
    position = k - 1
    startIdx = 0
    endIdx = len(array) - 1
    while True:
        if startIdx > endIdx:
            raise Exception("This isn't recursive Quick Sort!")
        pivotValue = array[startIdx]
        leftIdx = startIdx + 1
        rightIdx = endIdx
        while leftIdx <= rightIdx:
            if array[leftIdx] > pivotValue and array[rightIdx] < pivotValue:
                swap(leftIdx, rightIdx, array)
            if array[leftIdx] <= pivotValue:
                leftIdx += 1
            if array[rightIdx] >= pivotValue:
                rightIdx -= 1
        swap(startIdx, rightIdx, array)
        print("left:", leftIdx, "right:", rightIdx, "array:", array)
        if rightIdx == position:
            return array[rightIdx]
        elif rightIdx > position:
            endIdx = rightIdx - 1
        else:
            startIdx = rightIdx + 1


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


print(quickselect(test, k))
