# Python Assignment #1 DIY Data Utilities
# Github reference https://github.com/jattenberg/PDS-Spring-2014/blob/master/assignments/python_1.md
# Group: Richard Saito, Thiago Teodoro, Grace Peng, Ajeshkumar Vijayadas 
 
#unix command for part a: cat pythonlessondata.txt | python pythonassign1part2.py a
#unix command for part b: cat pythonlessondata.txt | python pythonassign1part2.py b
#unix command for part c: cat pythonlessondata.txt | python pythonassign1part2.py c

#import libraries
import sys
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

#declare variables
sSales = []
sPrice = []
dSalesPrice = {}

sOption = str(sys.argv[1])

#print sys.argv[1]
print sOption

#loop through data by row
for line in sys.stdin:
    tempSales, tempPrice = line.strip().split(',')
    #add data rows to arrays 
    sSales.append(tempSales)    
    sPrice.append(tempPrice)
    
print sSales
print sPrice

if sOption == 'a':
    #single data column plot
    plt.plot(sSales)
    plt.title('Sales') 
    
elif sOption == 'b':
    labels, values = zip(*Counter(sSales).items())
    indexes = np.arange(len(labels))
    width=1
    plt.bar(indexes,values,width)
    plt.xticks(indexes + width * 0.5, labels)
    plt.title('Sales') 
    
elif sOption == 'c':
    plt.plot(sSales)
    plt.plot(sPrice)
    
    #plt.plot(prog_list)
    plt.title('Sales') 
    plt.grid(True)
    plt.legend(['Sales','Price'])
    
# Render the plot!
plt.show()

