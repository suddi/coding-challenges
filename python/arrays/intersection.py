def intersections(arrays, intersectionsCount):
    count = {}
    result = set()
    for array in arrays:
        for k in set(array):
            if k not in count:
                count[k] = 1
            else:
                count[k] += 1
            if count[k] >= intersectionsCount:
                result.add(k)
    return list(result)


arrays = [
    [2, 5, 3, 2, 8, 1, 1, 2, 2],
    [7, 9, 5, 2, 4, 10, 10],
    [6, 7, 5, 5, 3, 7]
]
print(intersections(arrays, 2))
