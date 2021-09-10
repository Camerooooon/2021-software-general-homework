inpt = input()

try:
    parsed = int(inpt)
except ValueError:
    print("Not an integer weirdo")

print ((parsed-32)*(5/9))
