def mergeSortedNumericLists(l1, l2):
    mergedList = l1 + l2
    return mergedList

print("Welcome to the SortedNumericList Combiner!")
l1 = [1, 5, 16, 61, 111]; l2 = [2, 4, 5, 6]
print("List1 : ", l1)
print("List2 : ", l2)
print("Expected result: ", [1, 2, 6, 16, 61, 77]) # this is weird
# TODO: finish this assignment after clarification by the teacher.

print("Actual result: ", mergeSortedNumericLists(l1 ,l2))
