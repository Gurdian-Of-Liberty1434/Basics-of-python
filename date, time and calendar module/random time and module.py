import random
import time

def getRandomDate(startDate, endDate):
    print("Printing Random date between", startDate, "and", endDate)
    randomGenerator=random.random()
    dateFormat="%m/%d/%Y"

    startTime=time.mktime(time.strptime(startDate, dateFormat))
    endTime=time.mktime(time.strptime(endDate, dateFormat))

    randomTime=startTime+randomGenerator*(endTime-startTime)
    randomDate=time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print("Random date is", getRandomDate("01/01/1999", "02/26/2025"))
