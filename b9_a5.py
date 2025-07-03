from random import randint

def sevenEleven(prints = False):
  s = randint(1, 6) + randint(1, 6)
  if prints:
    print(f"Erster Wurf: {s}")
  if (s == 7 or s == 11):
    if prints:
      print("gewonnen")
    return 1
  if (s == 2 or s == 3 or s == 12):
    if prints:
      print("verloren")
    return -1
  while True:
    n = randint(1, 6) + randint(1, 6)
    if prints:
      print(f"Wurf: {n}")
    if n == 7:
      if prints:
        print("verloren")
      return -1
    if n == s:
      if prints:
        print("gewonnen")
      return 1

if __name__ == "__main__":
  gewinn = 0
  for _ in range(1000):
    gewinn += sevenEleven()
  print(gewinn/1000)