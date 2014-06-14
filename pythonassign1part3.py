# Python Assignment #1 Income Prediction
# Group: Richard Saito, Thiago Teodoro, Grace Peng, Ajeshkumar Vijayadas 
# Assignment https://github.com/jattenberg/PDS-Spring-2014/blob/master/assignments/python_1.md
# Data definition https://github.com/jattenberg/PDS-Spring-2014/blob/master/data/marketing.info

#declare variables
sIncome = []
iNomInc = 4.0
iCurrInc = 0.0
iPredInc = 0.0
iPredInc2 = 0.0
iDiff = 0.0
iDiff2 = 0.0
iTtlDiff = 0.0
iTtlDiff2 = 0.0
avgDiff = 0.0
avgDiff2 = 0.0
iTtlActInc = 0.0
iTtlPredIncAbs = 0.0
iTtlPredIncAbs2 = 0.0
iTtlPredInc = 0.0
iTtlPredInc2 = 0.0
iNumRecs = 0
fSignDiff = 0.0
iCountOverEdu = 0
iCountUnderEdu = 0
iCountOverOccup = 0
iCountUnderOccup = 0

#open file in read-only mode and load into file object
fIncome = open('/Users/richardsaito/Documents/Education/nyu/module 1/practical data science/data/marketing.data', 'r')

for line in fIncome:
    #break apart record into separate fields and load into variable
    sIncome = line.strip().split(" ")
    #print sIncome
       
    if len(line) > 1 and sIncome[4] != 'NA' and sIncome[5] != 'NA' and sIncome[0] != 'NA':
        #count number of records processed
        iNumRecs +=1
 
        #get income level for current record
        iCurrInc = int(sIncome[0])
        iTtlActInc += iCurrInc
           
        #process education level by accumulating total of actual and predicted incomes
        if sIncome [4] == '1':
            iPredInc = iNomInc - 3
        elif sIncome [4] == '2':
            iPredInc = iNomInc - 1
        elif sIncome [4] == '3':
            iPredInc = iNomInc
        elif sIncome [4] == '4':
            iPredInc = iNomInc + 1
        elif sIncome [4] == '5':
            iPredInc = iNomInc + 3
        elif sIncome [4] == '6':
            iPredInc = iNomInc + 4
        
        iTtlPredInc += iPredInc
        iDiff = abs(iCurrInc - iPredInc)
        iTtlDiff += iDiff
        iPredInc2 = iPredInc
            
        #process occupations
        if sIncome [5] == '1':
            iPredInc2 = iPredInc2 + 2.5
        elif sIncome [5] == '2':
            iPredInc2 = iPredInc2 - 0.6
        elif sIncome [5] == '4':
            iPredInc2 = iPredInc2 + 0.2
        elif sIncome [5] == '5':
            iPredInc2 = iPredInc2 - 0.5
        elif sIncome [5] == '6':
            iPredInc2 = iPredInc2 - 1.5
        elif sIncome [5] == '7':
            iPredInc2 = iPredInc2 + 0.3
        elif sIncome [5] == '8':
            iPredInc2 = iPredInc2 + 0.8
        elif sIncome [5] == '9':
            iPredInc2 = iPredInc2 - 2.5

        iTtlPredInc2 += iPredInc2
        iDiff2 = abs(iCurrInc - iPredInc2)
        iTtlDiff2 += iDiff2
        
        if iPredInc > iCurrInc:
            iCountOverEdu +=1
        elif iPredInc < iCurrInc:
            iCountUnderEdu += 1

        if iPredInc2 > iCurrInc:
            iCountOverOccup +=1
        elif iPredInc2 <= iCurrInc:
            iCountUnderOccup += 1
            
avgDiff = iTtlDiff / iNumRecs
avgDiff2 = iTtlDiff2 / iNumRecs
fSignDiff = iTtlPredInc2 - iTtlActInc

print "\n----- Records Processed -----"
print "Number of Records %i" % iNumRecs
#print "Actual %i" % len(dActInc)
#print "Predicted %i" % len(dPredInc)

print "\n----- Education Only -----"
print "Total Actual Income Level %i" % iTtlActInc
print "Total Predicted Income Level Ed Only %i" % iTtlPredInc
print "Total Difference %f" % iTtlDiff
print "Average Difference Per Person %f" % avgDiff
print "Model Over Estimations %i" % iCountOverEdu
print "Model Under Estimations %i" % iCountUnderEdu
if iCountOverEdu > iCountUnderEdu:
    print "The model likely over estimates"
else:
    print "The model likely over under estimates"

print "\n----- Education and Occupation -----"
print "Total Actual Income Level %i" % iTtlActInc
print "Total Predicted Income Level %f" % iTtlPredInc2
print "Total Difference %f" % iTtlDiff2 
print "Average Difference Per Person %f" % avgDiff2
print "Signed Difference %f" % fSignDiff
print "Model Over Estimations %i" % iCountOverOccup
print "Model Under Estimations %i" % iCountUnderOccup
if iCountOverOccup > iCountUnderOccup:
    print "The model likely over estimates"
else:
    print "The model likely over under estimates"