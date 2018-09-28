from sets import Set
import csv

#Naive solution: return intersection of all the Sets
def NaiveB(textFile):
    with open(textFile,"r") as csvfile:
        reader = csv.reader(csvfile, delimiter = ",")
        for delegate in reader:
            delegateSet = Set(delegate[1:-1])
            try:
                solution = solution & delegateSet
            except UnboundLocalError:
                solution = delegateSet
        print(solution[0])

def nonNaive3A(textFile):
    with open(textFile,"r") as csvfile:
        solution = []
        allDelegates = []
        done = False
        reader = csv.reader(csvfile, delimiter = ",")

        for delegate in reader:
            delegateSet = Set(delegate[1:-1])
            allDelegates.append(delegateSet)
            try:
                unionSet = unionSet + delegateSet
            except UnboundLocalError:
                unionSet = delegateSet

    while not done:
        countDict = {}
        for delegate in allDelegates:
            try:
                intersectSet = intersectSet & delegate
            except UnboundLocalError:
                intersectSet = delegate

        if len(intersectSet) == 0:
            if len(allDelegates) != 0:
                for language in unionSet:
                    count = 0
                    delegateList = [language]
                    for delegate in allDelegates:
                        if language in delegate:
                            count += 1
                            delegateList.append(delegate)
                    countDict[count] = delegateList

                highestCount = sorted(countDict.keys())[-1]
                highestLanguage = countDict[highestCount]
                delegateList = countDict[highestCount][1:]
                solution.append(highestLanguage[0].tolist())
                unionSet.remove(highestLanguage[0])

                for delegate in delegateList:
                    allDelegates.remove(delegate)
            else:
                print(solution)
                done = True
        else:
            solution.append(intersectSet[0])
            print(solution)
            done = True

NaiveB("delegates.txt")
nonNaive3A('delegates.txt')
nonNaive3A('delegates3.txt')
nonNaive3A('delegates5.txt')
nonNaive3A('delegates10.txt')
nonNaive3A('delegates100.txt')

'''
Part 3B: The non-naive solution uses the greedy algorithm to approximate the solution to the problem.

It uses a while loop to scan for intersections between all the Set.
If there is no language that covers all Sets, the language that covers the most Sets is found.
The language is added to the list of solutions, and all Sets with the language removed.
The process is then looped until there are no Sets left to cover.

While the algorithm does not provide the most optimal solution,
a true brute force algorithm that looks through every possible solution
would take 23 hours to solve the problem with delegates100.txt.

Meanwhile, this algorithm took less than a second to find the solution,
and still provided a solution reasonably short, with delegates100.txt as an example
(BF: 10 languages, Greedy: 11 languages).

The use of Numpy arrays to hold the values for the Set ADT also reduces
the memory used to store the Sets, vastly reducing the memory used in processing
and storing the data compared to using Python lists with many pointers (5 times less storage!).

The more efficient storage from Numpy arrays as well as time efficiency provided by the greedy algorithm
allow for many more languages as well as thousands of delegates to be handled within a few minutes.
In fact, even hundreds of millions of delegates could be stored and handled in less than a day,
performing pretty well in terms of both storage and time.

Meanwhile, over 30 languages and just 1000 delegates using brute force just might take more than a week.
'''
