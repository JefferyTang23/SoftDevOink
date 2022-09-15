def string_times(str, n):
  if n == 0:
    return ""
  string = ""
  while n > 0:
    string = string + str
    n = n - 1
  return string

def front_times(str, n):
  front = str[:3]
  string = ""
  while n > 0:
    string = string + front
    n = n - 1
  return string

def string_bits(str):
  string = ""
  index = 0
  while index < len(str):
    string += str[index]
    index += 2
  return string

def string_splosion(str):
  string = ""
  index = 1
  while index <= len(str):
    string += str[:index]
    index += 1
  return string