# myString = "Day 38"
# for letter in myString:
#   print(letter)

# This code outputs:
#D
#a
#y

#3
#8
# this is a comment in the code, the computer will ignore it

myString = "Day 38"
for letter in myString:
  if letter.lower() == "a":
    print('\033[33m', end='')  #yellow
  print(letter, end='') # getting over because of end so print will not put enter
  #the operation shall began after direclly on that line
  print('\033[0m', end='')  #back to default

# This code outputs (with a yellow 'a'):
#D
#a
#y

#3
#8

# vowels = ["a","e","i","o","u"]

# myString = "Will my vowels now be yellow?"
# for letter in myString:

#   if letter.lower() in vowels:
#     print('\033[33m', end='') #yellow # end means the print statement is officailly over

#   print(letter, end="")
#   print('\033[0m', end='') #back to default
