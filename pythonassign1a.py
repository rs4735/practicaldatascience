# Python Assignment 1a
# Name: Richard Saito
# Assignment Reference: https://github.com/jattenberg/PDS-Spring-2014/blob/master/assignments/python_1.md

#import counter in collections library 
from collections import Counter
import matplotlib.pyplot as plt

#declare array variables
lID = []
lUnix = []
lUnixCount = []
lDatabase = []
lDatabaseCount = []
lProgramming = []
lProgrammingCount = []
iCount = 0
iSumUnix = 0
iSumDB = 0
iSumProg = 0
fAvgUnix = 0.0
fAvgDB = 0.0
fAvgProg = 0.0

#run options 1,2a,2b,2c,3,4 corresponding to each subpart of the assignment
sOption = '4'

#open file in read-only mode and load into file object
fsurvey = open('/Users/richardsaito/Documents/Education/nyu/module 1/practical data science/data/survey_anon.txt', 'r')

# parse through file and load values into arrays
for line in fsurvey:
    #print line
    iCount +=1
    sID, sUnix, sDatabase, sProgramming = line.strip().replace('"',"").split("\t")
    lUnix.append(sUnix)
    lDatabase.append(sDatabase)
    lProgramming.append(sProgramming)

# count answers
cUnix = Counter(lUnix)
cDatabase = Counter(lDatabase)
cProgramming = Counter(lProgramming)

# Separate out the counter to order it correctly when plotting.
unix_list = [cUnix["I dont even understand the question"], #Unix
            cUnix["I have issued a few commands in a terminal based on given instructions"] * 3,
            cUnix["I have no experience working in a terminal"] * 2,
            cUnix["I have written simple terminal commands or done some system work on the terminal"] * 4
            ]
            
db_list =   [cDatabase["I am a database hacker"] * 5, #DB
            cDatabase["I have never directly accessed a database"],
            cDatabase["I have issued simple queries to a relational database based on given instructions"] * 2,
            cDatabase["I can write simple queries and issue them to a database"] * 3,
            cDatabase["I can write very complex queries when needed"] * 4
            ]
            
prog_list = [cProgramming["I have never programmed before."], #prog
            cProgramming["I am a hacker or have  senior-level programming experience"] * 5,
            cProgramming["I have written simple programs, based on instructions or a tutorial"] * 2,
            cProgramming["I can write simple programs to accomplish tasks I encounter"] * 3,
            cProgramming["I can write complex programs, am familiar with programming design patterns, software testing, system design, and algorithms."] * 4
            ]

#load chart labels
tUnix = tuple(["UX Don't", "UX Few", "UX No", "UX Smp"])
tDB = tuple(["DB Hck","DB Nvr","DB Ins","DB WSmp","DB Cpx"])
tProg = tuple(["PG Nvr","PG Hck","PG Ins","PG Smp","PG Cpx"])
tSurvey = tuple(["UNo", "UFw", "UIns", "UNnd", "DIns", "DCmp", "DSmp", "DNvr", "DHck", "PNvr", "PSmp", "PCmp", "PIns", "PHck"])


print "Total survey records processed %i" % iCount

# Q1. print survey answer totals
if sOption == '1':
    iSumUnix = sum(unix_list)
    iSumDB = sum(db_list)
    iSumProg = sum(prog_list)
    fAvgUnix = float(iSumUnix) / float(iCount)
    fAvgDB = float(iSumDB) / float(iCount)
    fAvgProg = float(iSumProg) / float(iCount)
    print "\nUnix Total %i" % iSumUnix
    print "Database Total %i" % iSumDB
    print "Programming Total %i" % iSumProg
    print "\nUnix Avg %f" % fAvgUnix
    print "Database Total %f" % fAvgDB
    print "Programming Total %f" % fAvgProg
    print "\nAnswer"
    if iSumUnix == max(iSumUnix,iSumDB,iSumProg):
        print "Highest: Unix"
    elif iSumDB == max(iSumUnix,iSumDB,iSumProg):
        print "Highest: Database"
    elif iSumProg == max(iSumUnix,iSumDB,iSumProg):
        print "Highest: Programming"

    if iSumUnix == min(iSumUnix,iSumDB,iSumProg):
        print "Lowest: Unix"
    elif iSumDB == min(iSumUnix,iSumDB,iSumProg):
        print "Lowest: Database"
    elif iSumProg == min(iSumUnix,iSumDB,iSumProg):
        print "Lowest: Programming"

elif sOption == '2a':
    #Q2 Plot part 1
    plt.plot(unix_list)
    plt.title('Unix Survey') 
    plt.xlabel('Questions')
    plt.ylabel('Answers')
    plt.xticks(range(len(tUnix)), tUnix)
    plt.show()

elif sOption == '2b':
    #Q2 Plot part 2
    plt.plot(db_list)
    plt.title('Database Survey') 
    plt.xlabel('Questions')
    plt.ylabel('Answers')
    plt.xticks(range(len(tDB)), tDB)
    plt.show()

elif sOption == '2c':
    #Q2 Plot part 3
    plt.plot(prog_list)
    plt.title('Programming Survey') 
    plt.xlabel('Questions')
    plt.ylabel('Answers')
    plt.xticks(range(len(tProg)), tProg)
    plt.show()

elif sOption == '3':
    #Q3
    plt.plot(unix_list)
    plt.plot(db_list)
    plt.plot(prog_list)
    plt.title('Student Skills Survey') 
    plt.xlabel('Questions')
    plt.ylabel('Answers')
    plt.grid(True)
    plt.legend(['Unix','Database','Programming'])
    # Render the plot!
    plt.show()

elif sOption == '4':
    #Q4
    plt.bar([1,2,3,4],unix_list,color='r')
    plt.bar([6,7,8,9,10],db_list,color='b')
    plt.bar([12,13,14,15,16],prog_list,color='g')
    plt.title('Student Skills Survey') 
    plt.xlabel('Questions')
    plt.ylabel('Answers')
    plt.grid(True)
    plt.legend(['Unix','Database','Programming'])
    # Render the plot!
    plt.show()