import sys

def my_function(a: str) -> bool:
  return a == 'help'

def main():
  print("Holy shit Dar, you can code!")
  if(my_function("Help")):
    print("You in trouble, son")
  else: 
    print("You're alright")
  

if __name__ == '__main__':
  main()

