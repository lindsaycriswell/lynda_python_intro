#
# Example file for working with conditional statements
#

def main():
  x, y = 1000, 100

  # conditional flow uses if, elif, else
  if x < y:
      st = "y wins"
  elif x > y:
    st = "x wins"
  else: st = "tie"

  print(st)
  # conditional statements let you use "a if C else b"
  st = "y wins" if (x < y) else "x wins"
  print(st)

if __name__ == "__main__":
  main()
