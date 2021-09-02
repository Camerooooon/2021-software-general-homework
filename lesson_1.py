# Create a program in which the user creates 
# a specific FRC team and store the following variables:
	# Team Number (named team_number)
	# Team Name (named team_name)
	# Location (named location)
	# Rookie Year (named rookie_year)
	# Is Active (named is_active)
# Be sure to store each variable as the correct type!

def parse_input(inpt):
    if (inpt == "y"):
        return True
    elif (inpt == "n"):
        return False
    else:
        print("Unknown input " + inpt + " interperating as no")
        return False

def parse_int(inpt):
    try:
        return int(val)
    except ValueError:
        print("Could not parse int: " + inpt);
        return 0

val = input("Team number: ");
team_number = parse_int(val);
print(val);

val = input("Team name: ");
print(val);
team_name = val

val = input("Team location: ");
print(val);
location = val

val = input("Rookie year: ");
print(val);
rookie_year = parse_int(val);

val = input("Is Active [y/n]:");
print(val);
is_active = parse_input(val);

print(str(team_number) + " aka " + team_name + " is located in " + location + " and their rookie year was in " + str(rookie_year) + " and they are " + "active" if is_active else "not active")
