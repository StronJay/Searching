test = [-3, -7, -17, -27, -18, -1, -541, -8, -7, -2, 7]


def findThreeLargestNumbers(array):
    threeLargestNumbers = [None, None, None]
    for number in array:
        getLargestNumbers(number, threeLargestNumbers)
    return threeLargestNumbers


def getLargestNumbers(number, threeLargestNumbers):
    if threeLargestNumbers[2] is None or number > threeLargestNumbers[2]:
        shiftAndUpdate(number, threeLargestNumbers, 2)
    elif threeLargestNumbers[1] is None or number > threeLargestNumbers[1]:
        shiftAndUpdate(number, threeLargestNumbers, 1)
    elif threeLargestNumbers[0] is None or number > threeLargestNumbers[0]:
        shiftAndUpdate(number, threeLargestNumbers, 0)


def shiftAndUpdate(number, threeLargestNumbers, idx):
    for i in range(idx + 1):
        if i == idx:
            threeLargestNumbers[i] = number
        else:
            threeLargestNumbers[i] = threeLargestNumbers[i + 1]


print(findThreeLargestNumbers(test))
