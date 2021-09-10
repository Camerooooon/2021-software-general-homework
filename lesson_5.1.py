class Robot:
    position = 0
    arm_position = 0
    has_cube = False
    score = 0

    def move(self, pos):
        self.position += pos

    def change_arm(self, pos):
        self.arm_position += pos

    def pickup_cube(self):
        if (self.position == 3):
            self.has_cube = True
        else:
            print("Not in space")

    def score_cube(self):
        if (self.has_cube):
            self.has_cube = False
            self.score += 1
        else:
            print("You cannot score without a cube!")

    def print_robot(self):
        print("Pos: " + str(self.position) + ", Arm: " + str(self.arm_position) + ", Cube:" + str(self.has_cube) + "Score: " + str(self.score))

robot = Robot()

while True:
    inpt = input("Do action [move/lowerarm/raisearm/pickup/score]:")
    if (inpt == "move"):
        robot.move(1)
    elif (inpt == "lowerarm"):
        robot.change_arm(-1)
    elif (inpt == "raisearm"):
        robot.change_arm(1)
    elif (inpt == "pickup"):
        robot.pickup_cube()
    elif (inpt == "score"):
        robot.score_cube()
    robot.print_robot();
