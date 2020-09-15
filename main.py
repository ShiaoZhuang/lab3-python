# Author: Shiao Zhuang sqz5328@psu.edu
# Collaborator: Yue Wu yzw5627@psu.edu
# Collaborator: Grace Lavin gcl5087@psu.edu
# Collaborator: Michael Artlip mva5905@psu.edu
# Section: 1
# Breakout: 18

def sum_n(n):
  if n == 0:
    return 0
  else:
    return n + sum_n(n-1)

def print_n(s, n):
  if n > 0:
    print(s)
    print_n(s, n-1)
    

def run():
  n = int(input("Enter an int: "))
  print(f"sum is {sum_n(n)}.")
  s = input("Enter a string: ")
  print_n(s,n)

if __name__ == "__main__":
  run()