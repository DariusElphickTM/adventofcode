import sys
import re
import functools

def main():
    
    list1 = []
    list2 = []
    
    print("Hello Day 1")
    input = readFile("1.txt")
    
    for line in input:
        locations = getLocations(line)
        list1.append(locations[0])
        list2.append(locations[1])
    
    list1 = list(map(int, list1))
    list2 = list(map(int, list2))
    
    list1.sort()
    list2.sort()

    getDiffs(list1, list2)
    getSimularities(list1, list2)

def getLocations(line: str):
    return re.findall(r'\d+', line)

def getDiffs(list1, list2):
    diffs = []
    for i in range(len(list1)):
        if(list2[i] > list1[i]):
            diffs.append(list2[i] - list1[i])
        else:
            diffs.append(list1[i] - list2[i])

    print("Total diffs", functools.reduce(lambda a, b: a + b, diffs))

def getSimularities(list1, list2):
    simularities = []
    for item in list1:
        simularities.append(item * list2.count(item))
    
    print("Total simularities", functools.reduce(lambda a, b: a + b, simularities))

def readFile(filename):
    file = open(filename, 'r')
    fileContents = file.readlines()
    file.close()
    return fileContents

if __name__ == "__main__":
    main()