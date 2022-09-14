def sleep_in(weekday, vacation):
  return (not weekday) or vacation

def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

def sum_double(a, b):
  if a == b:
    return 4 * a
  return a + b

def diff21(n):
  if n > 21:
    return 2*(n - 21)
  return 21 - n

def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)

def makes10(a, b):
  return a == 10 or b == 10 or (a + b) == 10
