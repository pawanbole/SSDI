import string
import operator
import sys


def topUsers():
    INPUTFILE = input("Enter the file path: ")
    INPUT_FILE_PATH = INPUTFILE + '.txt'

    with open(INPUT_FILE_PATH, encoding="latin-1") as myFile:
        twitter = myFile.readlines()
    l = {}
    for dat in twitter:

        fileTemp = dat.split()
        if fileTemp[0] in l:
            l[fileTemp[0]] += 1
        else:
            l[fileTemp[0]] = 1
    l = sorted(l.items(), key=operator.itemgetter(1), reverse=True)

    outputFile = open('C:/Users/pawan/PycharmProjects/TwitterTextAnalysis/TopUsers.txt', 'w', encoding="utf-8")
    outputFile.write("The top 10 users who have tweeted the most for the entire timeline: \n")
    for i in range(0, 10):
        outputFile.write("The user " + l[i][0] + " tweeted " + str(l[i][1]) + " times" + "\n")

    outputFile.close


topUsers()


def topUsersPerHour():
    INPUTFILE = input("Enter the file path: ")
    INPUT_FILE_PATH = INPUTFILE + '.txt'

    with open(INPUT_FILE_PATH, encoding="latin-1") as myFile:
        data = myFile.readlines()

    l = {}
    for dat in data:
        fileTemp = dat.split()
        fileTemp2 = fileTemp[1].split(":")
        twitterTemp = fileTemp[0] + " " + fileTemp2[1]
        if twitterTemp in l:
            l[twitterTemp] += 1
        else:
            l[twitterTemp] = 1
    l = sorted(l.items(), key=operator.itemgetter(1), reverse=True)

    l2 = {}
    totalNumPostsInFile = 0
    for dat in l:
        totalNumPostsInFile += 1
        if (dat[0].split()[1]) in l2:
            l2[dat[0].split()[1]] += 1
        else:
            l2[dat[0].split()[1]] = 1
    l2 = sorted(l2.items(), key=operator.itemgetter(1))

    totalEntriesToPrint = 10 * len(l2)
    outputFile = open('C:/Users/pawan/PycharmProjects/TwitterTextAnalysis/TopUsersPerHour.txt', 'w',
                      encoding='utf-8')

    for x in range(0, len(l2)):

        mSearch = 10

        for dat in l:
            if mSearch == 0:
                break
            if dat[0].split()[1] == l2[x][0]:
                outputFile.write("Username: " + dat[0].split()[0] + "\n Hour: " + l2[x][0] + "\n")

                mSearch -= 1
    outputFile.close


topUsersPerHour()


def maxFollowers():
    INPUTFILE = input("Enter the file path: ")
    INPUT_FILE_PATH = INPUTFILE + '.txt'

    with open(INPUT_FILE_PATH, encoding="latin-1") as myFile:
        twitter = myFile.readlines()

    l = {}
    for dat in twitter:
        fileTemp = dat.split()
        if fileTemp[0] not in l:
            l[fileTemp[0]] = int(fileTemp[-2])

    l = sorted(l.items(), key=operator.itemgetter(1), reverse=True)
    outputFile = open('C:/Users/pawan/PycharmProjects/TwitterTextAnalysis/MaxFollowers.txt', 'w',
                      encoding="utf-8")
    outputFile.write("The top 10 users who has the maximum followers: " + "\n\n")

    for i in range(0, 10):
        outputFile.write(str(i + 1) + ". Username: " + l[i][0] + " -> Number of Followers: " + str(l[i][1]) + "\n\n")
    outputFile.close


maxFollowers()


def maxRetweet():
    INPUTFILE = input("Enter the file path: ")
    INPUT_FILE_PATH = INPUTFILE + '.txt'

    with open(INPUT_FILE_PATH, encoding="latin-1") as myFile:
        twitter = myFile.readlines()

    l = {}
    for dat in twitter:

        fileTemp = dat.split()
        y = len(fileTemp) - 2
        tweet = "\""
        for x in range(4, y):
            tweet += fileTemp[x] + " "
        tweet += " ::::;:::: " + fileTemp[0]

        if tweet not in l:
            l[tweet] = int(fileTemp[-1])

    outputFile = open('C:/Users/pawan/PycharmProjects/TwitterTextAnalysis/MaxRetweets.txt', 'w', encoding="utf-8")
    l = sorted(l.items(), key=operator.itemgetter(1), reverse=True)
    outputFile.write("The top 10 tweets that has the max no of retweets : " + "\n\n")

    for x in range(0, 10):
        outputFile.write(str(x + 1) + ". Username: " + l[x][0].split()[-1] + "\n Tweet: " +
                         l[x][0].split("::::;::::")[0] + "\n No of retweets: " + str(l[x][1]) + "\n\n")
    outputFile.close


maxRetweet()