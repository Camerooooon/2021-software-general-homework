#inpt = input()
#
#try:
#    parsed = int(inpt)
#except ValueError:
#    print("Not an integer weirdo")
#
#print ((parsed-32)*(5/9))

# PART 2
import math

inpt = input()

try:
    parsed = int(inpt)
except ValueError:
    print("Not an integer weirdo go away strange person")


print((4/3) * math.pi * (parsed * parsed * parsed))
