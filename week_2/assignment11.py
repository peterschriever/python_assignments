students = { 0: "Nynke", 1: "Lolle", 2: "Jikke", 3: "Popke",\
    4: "Teake", 5: "Lieuwe", 6: "Tsjabbe", 7: "Klaske", 8: "Ypke", 9: "Lobke"}
friendships = [ (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4)\
    , (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9) ]

# could do: create function to dynamically create this list
listOfFriendships = [
    [0, 1, 2],
    [1, 0, 2, 3],
    [2, 0, 1, 3],
    [3, 1, 2, 4],
    [4, 3, 5],
    [5, 4, 6, 7],
    [6, 5, 8],
    [7, 5, 8],
    [8, 6, 7, 9],
    [9, 8]
]
print("11.A:", listOfFriendships)

lstCountFriendShips = [0] * len(listOfFriendships)
for item in listOfFriendships:
    lstCountFriendShips[listOfFriendships.index(item)] = (item[0], len(item)-1)
listOfFriendships.sort(key=lambda x: x[1])
print("11.B:", lstCountFriendShips)

def findCommonFriendsForStudent(intStudentNumber, lstFriendships):
    lstCommonFriends = []
    for student in lstFriendships:
        if intStudentNumber in student: # skip everything that is a direct friend
            continue                 # or the student himself

        amntOfCommonFriends = 0
        for friend in student:
            if intStudentNumber in lstFriendships[friend]:
                amntOfCommonFriends += 1 # common friend found, increase counter
        lstCommonFriends.append((student[0], amntOfCommonFriends))
    return lstCommonFriends

print("\n11.C:\nStudent 3:", findCommonFriendsForStudent(3, listOfFriendships),\
     "\nStudent 5:", findCommonFriendsForStudent(5, listOfFriendships))

studentInterests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"), (0, "Spark"),
    (0, "Storm"), (0, "Cassandra"), (1, "NoSQL"), (1, "MongoDB"),
    (1, "Cassandra"), (1, "HBase"), (1, "Postgres"), (2, "Python"),
    (2, "scikit-learn"), (2, "scipy"), (2, "numpy"), (2, "statsmodels"),
    (2, "pandas"), (3, "R"), (3, "Python"), (3, "statistics"), (3, "regression"),
    (3, "probability"), (4, "machine learning"), (4, "regression"),
    (4, "decision trees"), (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"),
    (5, "C++"), (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"), (7, "machine learning"),
    (7, "scikit-learn"), (7, "Mahout"), (7, "neural networks"),
    (8, "neural networks"), (8, "deep learning"), (8, "Big Data"),
    (8, "artificial intelligence"), (9, "Hadoop"), (9, "Java"),
    (9, "MapReduce"), (9, "Big Data")
]

# create dict with all student ids and an empty list for the value
dictStudInterests = {x[0]: [] for x in studentInterests}
for studInterest in studentInterests:
    # assuming that studInterest[0] is always the student number
    # and studInterest[1] is always the interest value/string
    dictStudInterests[studInterest[0]].append(studInterest[1])

print("\n11.D: ", dictStudInterests)

# almost use the same tricks as in 11.D but with different keys
dictInterestStud = {str(x[1]): [] for x in studentInterests}
for interestStud in studentInterests:
    dictInterestStud[str(interestStud[1])].append(interestStud[0])

print("\n11.E: ", dictInterestStud)
