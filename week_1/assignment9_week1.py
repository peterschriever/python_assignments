def mergeSortedNumericLists(l1, l2):
    longList = l1 if len(l1) > len(l2) else l2
    shortList = l2 if len(l1) > len(l2) else l1

    llPosition = 0
    for numberA in longList:
        slPosition = 0
        for numberB in shortList:
            if numberB < numberA:
                # extend the longList, reduce the shortList
                # the longList will be our sortedMergedList in the end
                longList.insert(llPosition, shortList.pop(slPosition))
            slPosition = slPosition + 1
        llPosition = llPosition + 1
        if len(shortList) == 0 :
            break # we have succesfully merged
    return longList

print("Welcome to the SortedNumericList Combiner!")
l1 = [1, 5, 16, 61, 111]; l2 = [2, 4, 5, 6]
print("List1 : ", l1)
print("List2 : ", l2)
print("Expected result: ", [1, 2, 4, 5, 6, 16, 61, 111])
print("Actual result: ", mergeSortedNumericLists(l1 ,l2))
