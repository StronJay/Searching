test, target = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
  ], 98


def getTargetValueInMatrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        potentialMatch = matrix[row][col]
        print(potentialMatch)
        if target == potentialMatch:
            return [row, col]
        elif target < potentialMatch:
            col -= 1
        else:
            row += 1
    return [-1, -1]

print(getTargetValueInMatrix(test, target))