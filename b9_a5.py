from random import randint

def sevenEleven():
  s = randint(1, 6) + randint(1, 6)
  if (s == 7 or s == 11):
    return 1
  if (s == 2 or s == 3 or s == 12):
    return -1
  while True:
    n = randint(1, 6) + randint(1, 6)
    if n == 7:
      return -1
    if n == s:
      return 1

if __name__ == "__main__":
  gewinn = 0
  for _ in range(1000):
    gewinn += sevenEleven()
  print(gewinn/1000)
