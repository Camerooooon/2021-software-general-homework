# A student has taken 3 tests in a class, and wants to know their current grade 
# (which is only calculated by these tests). 

# Ask the user to input all three of the test scores for the student, one by one. 

# The program should then calculate the average test score (average is adding all three 
# test scores together then dividing by 3), and then print the student's letter grade 
# (as well as the average score as a number).

def try_parse_int(str):
    try:
        return int(str)
    except ValueError:
        print("Failed to parse int: " + str)
        exit();

inpts = []

print("Enter a number or done to calculate average")

while True:
    inpt = input()

    if (inpt == "done"):
        break;

    num = try_parse_int(inpt);
    inpts.append(num);

print(inpts);

avg = 0

for i in inpts:
    avg += i

avg = avg / len(inpts)

print (avg)

#########################################################

# Gregory wants to know how many toys they can buy at Toys'N'Us

# They prioritize buying the most expensive toys first (For ejm. If Gregory had $50 
# they'd end up buying 2 Jumbo Baby Yoda Plushies, 1 Beyblade, and 5 Sticky Hands with 
# a remainder of $0.30 left)

# Have the user input how much money Gregory has then print how many of each 
# toy they can afford, as well as how much money they'd have remaining


