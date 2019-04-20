#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while (x < 5):
      print(x)
      x = x + 1
      # 0, 1, 2, 3, 4, 5

  # define a for loop - x is iterator btwn args, not inclusive
  for x in range(5, 10):
      print(x)
      # 5, 6, 7, 8, 9

  # use a for loop over a collection
  arr = ["a", "b", "c"]
  for x in arr:
      print(x)
      # "a", "b", "c"

  # use the break and continue statements
  for x in range(5, 10):
      if (x == 7): break
      print(x)
      # 5, 6

  for x in range(5, 10):
      if (x % 2 == 0): continue
      print(x)
      # 5, 7, 9

  #using the enumerate() function to get index
  arr = ["a", "b", "c"]
  for i, d in enumerate(arr):
      print(i, d)
      # 0"a", 1"b", 2"c"

if __name__ == "__main__":
  main()
