austin_list = [1, 4, 66, 54, 2, 6, 76, 6, 4, 3, 3, 646, 76, 8]


def merge(a_list, b_list):
    newArray = []
    while len(a_list + b_list) > 0:
        if len(a_list) == 0:
            newArray.append(b_list.pop(0))
        elif len(b_list) == 0:
            newArray.append(a_list.pop(0))
        elif a_list[0] <= b_list[0]:
            newArray.append(a_list.pop(0))
        else:
            newArray.append(b_list.pop(0))
    print(newArray)
    return newArray


def mergeSort(list):
    if len(list) == 1:
        return list
    if len(list) == 2:
        return merge([list[0]], [list[1]])
    mid = len(list) // 2
    return merge(mergeSort(list[:mid]), mergeSort(list[mid:]))


print(mergeSort(austin_list))
