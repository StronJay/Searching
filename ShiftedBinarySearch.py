test, target = [33, 45, 45, 61, 71, 72, 73, 355, 0, 1, 21], 354
def shiftedBinarySearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        potentialMatch = array[middle]
        leftBound = array[left]
        rightBound = array[right]
        print("left", left, "right", right, "middle", middle, "potentialMatch", potentialMatch, "leftBound", leftBound, "rightBound", rightBound)
        if target == potentialMatch:
            return middle
        elif leftBound <= potentialMatch:
            if target >= leftBound and target < potentialMatch:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if target <= rightBound and target > potentialMatch:
                left = middle + 1
            else:
                right = middle - 1
    return -1

print(shiftedBinarySearch(test, target))