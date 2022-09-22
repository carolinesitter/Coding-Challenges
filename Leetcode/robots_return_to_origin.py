# CHALLENGE: ROBOT RETURNS TO ORIGIN:
# ------------------------------------
## There is a robot starting at the position (0, 0), the origin, on a 2D plane.
## Given a sequence of its moves, judge if this robot ends up at (0, 0) after it
## completes its moves.

## You are given a string moves that represents the move sequence of the robot where
## moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up),
## and 'D' (down).

## Return true if the robot returns to the origin after it finishes all of its moves, or
## false otherwise.


# TEST CASE 1:
# ------------
## Input: moves = "UD"
## Output: true (robot returns to origin after it finishes all of its moves)

# TEST CASE 2:
# ------------
## Input: moves = "LL"
## Output: false (robot does not return to origin after it finishes all of its moves)


# PSEUDOCODE:
# ------------
## create a class for robots 
## within this class, write a function that takes in the robot(self) and the moves
## establish the orgin of the 2d plane the be 0,0 by setting x and y to 0
## then, iterate through the string moves and for each letter, assign the x and y values
## to establish where the robot will move on the 2d plane.
## Return true if the final placement is 0,0, and false otherwise. 


# CODE:
# -----
class Robot(object):
    def return_to_origin(self, moves):

        # set origin coordinates to 0,0
        x = 0
        y = 0

        # check each move 
        for move in moves:
            if move == "U":
                y += 1
            elif move == "D":
                y -= 1
            elif move == "R":
                x += 1
            elif move == "L":
                y -= 1

        # return true if the final placement is 0,0, and false otherwise
        # statement is truthy
        return x == 0 and y == 0


# RUNTIME COMPLEXITY:
# -------------------
## This solution has an O(N) or linear runtime complexity as it is only
## looping through the "moves" string once. 