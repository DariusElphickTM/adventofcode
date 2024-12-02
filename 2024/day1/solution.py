import sys
import re
import functools

def main():
  
  list1 = []
  list2 = []
  diffs = []
  
  print("Hello Day 1")
  input = readFile("1.txt")
  
  for line in input:
    locations = getLocations(line)
    print(locations)
    list1.append(locations[0])
    list2.append(locations[1])
    
  list1 = list(map(int, list1))
  list2 = list(map(int, list2))
    
  list1.sort()
  list2.sort()
  
  for i in range(len(list1)):
    if(list2[i] > list1[i]):
      diffs.append(list2[i] - list1[i])
    else:
      diffs.append(list1[i] - list2[i])
  
  print("Total diffs", functools.reduce(lambda a, b: a + b, diffs))
  

def getLocations(line: str):
   return re.findall(r'\d+', line)
  
def readFile(filename):
  file = open(filename, 'r')
  fileContents = file.readlines()
  file.close()
  return fileContents

if __name__ == "__main__":
  main()