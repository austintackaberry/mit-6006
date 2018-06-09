problemMatrix = [
    [4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
    [5,  6,  7,  8,  9,  8,  7,  6,  5,  4,  3],
    [6,  7,  8,  9, 10,  9,  8,  7,  6,  5,  4],
    [7,  8,  9, 10, 11, 10,  9,  8,  7,  6,  5],
    [8,  9, 10, 11, 12, 11, 10,  9,  8,  7,  6],
    [7,  8,  9, 10, 11, 10,  9,  8,  7,  6,  5],
    [6,  7,  8,  9, 10,  9,  8,  7,  6,  5,  4],
    [5,  6,  7,  8,  9,  8,  7,  6,  5,  4,  3],
    [4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
    [3,  4,  5,  6,  7,  6,  5,  4,  3,  2,  1],
    [2,  3,  4,  5,  6,  5,  4,  3,  2,  1,  0]
]


def localPeakFinder(problem):
    if len(problem) == 1:
        return problem[0]
    mid = len(problem) // 2
    if len(problem) == 2:
        if problem[1] > problem[0]:
            return problem[1]
        return problem[0]
    if problem[mid - 1] < problem[mid] and problem[mid+1] < problem[mid]:
        return problem[mid]
    if problem[mid - 1] > problem[mid]:
        return localPeakFinder(problem[:mid])
    if problem[mid + 1] > problem[mid]:
        return localPeakFinder(problem[mid+1:])


def findGlobalMax(row):
    max = 0
    index = 0
    for i, num in enumerate(row):
        if num > max:
            max = num
            index = i
    return [max, index]


def localPeakFinder2d(matrix):
    if len(matrix) == 1:
        return findGlobalMax(matrix[0])
    if len(matrix) == 2:
        max0 = findGlobalMax(matrix[0])[0]
        max1 = findGlobalMax(matrix[1])[0]
        if max1 > max0:
            return max1
        return max0
    mid = len(matrix) // 2

    currentRow = matrix[mid]

    globalMaxArr = findGlobalMax(currentRow)
    i = globalMaxArr[1]

    if matrix[mid - 1][i] <= matrix[mid][i] and matrix[mid + 1][i] <= matrix[mid][i]:
        return matrix[mid][i]
    if matrix[mid - 1][i] >= matrix[mid][i]:
        return localPeakFinder2d(matrix[:mid])
    if matrix[mid + 1][i] >= matrix[mid][i]:
        return localPeakFinder2d(matrix[mid+1:])


print(localPeakFinder2d(problemMatrix))
