def maximumUnits(boxTypes, truckSize):

    boxTypes.sort(key=lambda x: -x[1])
    boxes = 0

    for box, units in boxTypes:
        if truckSize > box:
            truckSize -= box
            # [2, 2] -> 2 box and 2 units per box means 4 units will be taken
            boxes += box * units
        else:
            boxes += truckSize * units
            return boxes

    return boxes


print(maximumUnits([[1,3],[2,2],[3,1]], 4))  # Output: 8
print(maximumUnits([[1,2],[2,3],[3,4]], 5))  # Output: 18
print(maximumUnits([[1,1],[2,2],[3,3],[4,4]], 10))  # Output: 30
print(maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))  # Output: 91
