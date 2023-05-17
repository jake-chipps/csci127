import random

## Global Variables ###########
###############################

## Define functions ###########
def getAmountFromUser():
    numInts = (int(input("How many integers?")))
    return numInts

def printRandomIntegers():
    for i in range( getAmountFromUser() ):
        num = random.randint(1,100)
        print(num)
###############################

## Build main (runner) ########
def main():
    printRandomIntegers()
#################################
    
## Call main
main()
