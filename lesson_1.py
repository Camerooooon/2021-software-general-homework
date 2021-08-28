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


val = input("Team number: ");
print(val);

try:
    team_number = int(val);
    print("Accepted");
except ValueError:
    team_number = 0;
    print("Invalid team number");

val = input("Team name: ");
print(val);
team_name = val

val = input("Team location: ");
print(val);
location = val

val = input("Rookie year [y/n]:");
print(val);
rookie_year = parse_input(val);

val = input("Is Active [y/n]:");
print(val);
is_active = parse_input(val);

print(str(team_number) + ", " + team_name + ", " + location + ", " + str(rookie_year) + ", " + str(is_active))

