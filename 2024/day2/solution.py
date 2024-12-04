import sys
import re

def main():
    reports = readFile("1.txt")
    safeReports = list(map(checkSafety, reports))
    print("Safe reports:", safeReports.count(True))

def checkSafety(report):
    reportValues = list(map(int, re.findall(r'\d+', report)))
    isSafe = True
    
    isReportAscending = True
    for i in range(len(reportValues) - 1):
        currentDiff = reportValues[i + 1] - reportValues[i]
        print(currentDiff)
        
        if(abs(currentDiff) < 1 or abs(currentDiff) > 3):
            isSafe = False
            break
        
        isReportCurrentlyAscending = currentDiff > 0
        
        if i == 0:
            isReportAscending = isReportCurrentlyAscending
        else:
            isSafe = isReportAscending == isReportCurrentlyAscending
            if not isSafe:
                break
    print("Final decision", isSafe)
    return isSafe

def readFile(filename):
    file = open(filename, 'r')
    fileContents = file.readlines()
    file.close()
    return fileContents

if __name__ == "__main__":
    main()