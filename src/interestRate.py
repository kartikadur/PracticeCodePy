##Problem 1
#remBalance = int(input("the outstanding balance on the credit card"))
#intRate = float(input("annual interest rate"))
#payRate = float(input("minimum monthly payment rate"))
#
#def MonthlyPayments(bal,intR,payR):
#    totalInterest = 0
#    for i in range(1, 13):
#        minMonthlyPay = round(bal * payR, 2)
#        intPaid = round(intR/12 * bal, 2)
#        princPaid = round(minMonthlyPay - intPaid, 2)
#        bal = bal - round(princPaid, 2)
#        totalInterest += minMonthlyPay
#        print("Month ", i)
#        print("Minimum monthly payment: $%0.2f" % minMonthlyPay)
#        print("Principal paid: $%0.2f" % princPaid)
#        print("Remaining Balance: $%0.2f" % bal)
#    print("RESULT")
#    print("Total amount paid $%0.2f" % totalInterest)
#    print("Remaining Balance: $%0.2f" % bal)
#MonthlyPayments(remBalance, intRate, payRate)

##Problem 2
#def makePayments(bal, monthlyRate, monthlyPay):
#    for i in range(1, 13):
#        bal = bal * (1 + monthlyRate) - monthlyPay
#        if(bal <= 0):
#            print("%d, %d, %.2f" %(monthlyPay, i, bal)) 
#            return [monthlyPay, i, bal]
#    return None
#
#def findMonthlyPayments(bal, aRoi):
#    mRoi = aRoi/12.0
#    mPay = 10
#    while(makePayments(bal, mRoi, mPay) == None):
#        mPay += 10
#
#
#bal = int(input("enter outstanding balance on credit card"))
#aRoi = float(input("enter annual rate of interest"))
#
#findMonthlyPayments(bal, aRoi) 

#Problem 3

bal = int(input("enter outstanding balance on credit card"))
aRoi = float(input("enter annual rate of interest"))


def calcPayments(oBal, aRoi):
    mRoi = aRoi / 12.0
    bal = oBal
    hiPay = (bal * (1 + (aRoi / 12.0)) ** 12.0) / 12.0
    loPay = bal / 12.0
    while(True):
        bal = oBal
        mPay = (loPay + hiPay) / 2.0
        newBal = makePayments(bal, mRoi, mPay)
        if(hiPay - loPay < 0.005):
            mPay = round(mPay + 0.004999, 2)
            result = makePayments(bal, mRoi, mPay)
            print("%.2f, %d, %.2f" %(result[0], result[1], result[2]))
            break
        elif(newBal[2] < 0):
            hiPay = mPay
        else:
            loPay = mPay

def makePayments(bal, mRoi, mPay):
    for i in range(1, 13):
        bal = bal * (1 + mRoi) - mPay
        if(bal <= 0):
            break
    return [mPay, i, bal]

calcPayments(bal, aRoi)