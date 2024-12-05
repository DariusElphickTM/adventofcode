import sys
import re

def main():
    reports = readFile("1.txt")
    safeReports = process_reports(reports)
    print("Safe reports:", safeReports.count(True))
    
def process_reports(reports):
    return list(map(checkSafety, reports))

def checkSafety(report, useDampner = False):
    reportValues = list(map(int, re.findall(r'\d+', report)))
    isSafe = True
    
    isReportAscending = True
    for i in range(len(reportValues) - 1):
        currentDiff = reportValues[i + 1] - reportValues[i]
        
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
    return isSafe

def readFile(filename):
    file = open(filename, 'r')
    fileContents = file.readlines()
    file.close()
    return fileContents

if __name__ == "__main__":
    main()