# Set the variable in_list to whatever value you want. Let's use 
# [ 5, 2, 3, 1, 4, 6, 8, 7 ] as an example.

# Use for loops, while loops, and whatever else we've learned to 
# set the variable x to the length of in_list - but you may NOT use len! 
# Try to mimic the behavior of len.

#nums = [5, 2, 3, 1, 4, 6, 8, 7]
#
#index = 0
#
#for i in nums:
#    index += 1
#
#print(index);


################################################
# Create a program to accept words from a user, and add them to a dictionary. 
# At the end, use print(mydict) to print out the user's work to them

#indexes = []
#dictionary = []
#
#
#while True:
#    inpt = input("Add index to dictionary or done to finish: ")
#    if (inpt == "done"):
#        break;
#    indexes.append(inpt)
#    inpt = input("Add value to dictionary")
#    dictionary.append(inpt)
#
#index = 0;
#for i in indexes:
#    print(i, dictionary[index]);
#    index += 1;

################################################
# Extend your dictionary program from assignment #2 to have some added capabilities:

# Make sure the user cannot enter more than one translation for the same word, 
# in either direction. For example, if ‘dog’: ‘Hund’ is already an entry in the 
# dictionary, then adding a new translation for ‘dog’ OR another word that translates 
# to ‘Hund’ should fail.

# Make sure the user cannot input a key that contains a space, but a value that 
# contains a space is acceptable. So adding ‘the dog’ : ‘Hund’ should fail, but 
# ‘dog’ : ‘der Hund’ is fine.

indexes = []
dictionary = []


while True:
    inpt = input("Add index to dictionary or done to finish: ")
    if (inpt in " "):
        print("STOP You have violated the law, indexes cannot contain spaces");
        continue;
    if (inpt == "done"):
        break;
    indexes.append(inpt)
    inpt = input("Add value to dictionary")
    if inpt in dictionary:
        indexes.pop();
        print("STOP You have violated the law, duplicate dictionary item try again");
        continue;
    dictionary.append(inpt)

index = 0;
for i in indexes:
    print(i, dictionary[index]);
    index += 1;
















################################################
# Instead of printing out the dictionary when the program is done, ask the user 
# for a sentence and “translate” it, word-by-word, as output. 

# If a word has no translation, use the word unchanged.
