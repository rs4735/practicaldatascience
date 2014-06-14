# Python Assignment #1
# Group: Richard Saito, Thiago Teodoro, Grace Peng, Ajeshkumar Vijayadas 
 
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

sOption = 'a'
#sOption = str(sys.argv[1])

#open file in read-only mode and load into file object
fsurvey = open('/Users/richardsaito/Documents/Education/nyu/module 1/practical data science/data/survey_anon.txt', 'r')

# parse through file and load values into arrays
for line in fsurvey:
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
            cUnix["I have written simple terminal commands or done some system work on the terminal"],
            cUnix["I have issued a few commands in a terminal based on given instructions"],
            cUnix["I have no experience working in a terminal"] 
            ]
            
db_list =   [cDatabase["I am a database hacker"], #DB
            cDatabase["I have never directly accessed a database"],
            cDatabase["I can write simple queries and issue them to a database"],
            cDatabase["I can write very complex queries when needed"],
            cDatabase["I have issued simple queries to a relational database based on given instructions"]            
            ]
            
prog_list = [cProgramming["I am a hacker or have  senior-level programming experience"], #prog
            cProgramming["I have written simple programs, based on instructions or a tutorial"],
            cProgramming["I can write complex programs, am familiar with programming design patterns, software testing, system design, and algorithms."],
            cProgramming["I can write simple programs to accomplish tasks I encounter"],
            cProgramming["I have never programmed before."]
            ]

#load labels
tUnix = tuple(["UNnd", "UIns", "UFw", "UNo"])
tDB = tuple(["DHck","DNvr","DSmp","DCmp","DIns"])
tProg = tuple(["PHack","PIns","PCmp","PSmp","PNvr"])
tSurvey = tuple(["UNo", "UFw", "UIns", "UNnd", "DIns", "DCmp", "DSmp", "DNvr", "DHck", "PNvr", "PSmp", "PCmp", "PIns", "PHck"])

# Q1. print answer counts
if sOption == 'a':
    print "Unix"
    print cUnix
    print "\nDatabase"
    print cDatabase
    print "\nProgramming"
    print cProgramming

elif sOption == 'b1':
    #Q2 Plot part 1
    plt.plot(unix_list)
    plt.title('Unix Survey') 
    plt.xlabel('Questions')
    plt.ylabel('Answers')
    plt.xticks(range(len(tUnix)), tUnix)
    plt.show()

elif sOption == 'b2':
    #Q2 Plot part 2
    plt.plot(db_list)
    plt.title('Database Survey') 
    plt.xlabel('Questions')
    plt.ylabel('Answers')
    plt.xticks(range(len(tDB)), tDB)
    plt.show()

elif sOption == 'b3':
    #Q2 Plot part 3
    plt.plot(prog_list)
    plt.title('Programming Survey') 
    plt.xlabel('Questions')
    plt.ylabel('Answers')
    plt.xticks(range(len(tProg)), tProg)
    plt.show()

elif sOption == 'c':
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

elif sOption == 'd':
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
