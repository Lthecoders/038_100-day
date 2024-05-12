import os
import random
import time

red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
white = '\033[37m'

taking_uses = input(
    "\nEnter any sentence to see it's rainbow colored version.😲😲 ------> "
).strip().capitalize()

os.system("clear")
print("\n\n\nconverting your text into rainbow....😲🔥")
print("\nPlease wait....")
time.sleep(3)
os.system("clear")

print()
print()
print()
print(
    green,
    "\nsuccessfully converted your simple looking text into rainbow text.👍👍\n\n",
    white)
for i in taking_uses:
  if i.lower() == 'r':
    print(red, end="")
  elif i.lower() == 'g':
    print(green, end="")
  elif i.lower() == 'y':
    print(yellow, end="")
  elif i.lower() == 'b':
    print(blue, end="")
  elif i.lower() == 'p':
    print(purple, end="")
  elif i.lower() == 'c':
    print(cyan, end="")
  elif i.lower() == ' ':
    print(white, end="")

  print(i, end="")


print()
print()
