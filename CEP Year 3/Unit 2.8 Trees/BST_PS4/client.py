from movietrees import *

movies = list(open('movies.txt', 'r').readlines())
for i in range(len(movies)): movies[i] = movies[i][:-1].split("\t")

#Task 1 - addition of movie records
title = TitleTree(movies[0][0], movies[0][1:])
score = ScoreTree(float(movies[1][1]), movies[1][0])
boxoffice = BoxOfficeTree(float(movies[1][4]), movies[1][0])
for i in movies[1:]:
    title.add(i[0], i[1:])
    score.add(float(i[1]), (i[0]))
    boxoffice.add(float(i[4]), (i[0]))

def task2():
    #Task 2 - deletion of movie records
    print('\nTask 2:')
    print('\nBefore deletion:')
    for i in title:
        print(i)

    for i in movies[1:]:
        title.delete(i[0])

    print('\nAfter deletion:')
    print(title)

def task3():
    #Task 3 - searching titles
    print('\nTask 3:')
    print(title.search('2 Fast 2 Furious'))
    print(title.search('28 Days Later'))
    print(title.search('big fish'))

def task4():
    #Task 4 - count number of titles with less than y million dollars in box office
    print('\nTask 4:')
    print(boxoffice.bocount(30)) #in this case, y is 30

def task5():
    #Task 5 - display all titles with box office within range [a, b]
    print('\nTask 5:')
    boxoffice.boprint(70, 90) #does not include 70 and 90 mil.

def task6():
    #Task 6 - print the movie with the highest box office
    print('\nTask 6:')
    boxoffice.highestboprint()

def task7():
    #Task 7 - print all titles by ascending score
    print('\nTask 7:')
    score.scoreprint()

def task8():
    #Task 8 - print all titles with score higher than x
    print('\nTask 8:')
    score.scoreprint(90) #in this case, x is 90

task3()
task2()
task4()
task5()
task6()
task7()
task8()
