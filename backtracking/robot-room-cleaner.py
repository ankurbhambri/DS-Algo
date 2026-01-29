# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        visited = set()

        # Directions: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def backtrack(x, y, d):

            robot.clean()
            visited.add((x, y))

            for i in range(4):

                new_d = (d + i) % 4

                new_x = x + directions[new_d][0]
                new_y = y + directions[new_d][1]

                if (new_x, new_y) not in visited and robot.move():

                    backtrack(new_x, new_y, new_d)

                    # Backtrack to the previous position and orientation
                    robot.turnRight()
                    robot.turnRight()

                    robot.move()

                    robot.turnRight()
                    robot.turnRight()

                robot.turnRight()

        backtrack(0, 0, 0)


# Variant

'''

Given a mouse with 2 APIs in a maze. Design an algorithm to find a cheese in the maze using only the 2 given APIs shown below.

class Mouse {

	/**
	* Moves to one of the directions (left, right, up, down) and returns false if you can't move and true if you can.
	*/
	public boolean move(Direction direction);

	/**
	* Returns true if there is a cheese in the current cell.
	*/
	public boolean hasCheese();

	/**
	* Should return true and leave the mouse at that location or false if we can't find cheese and return the mouse back to where it started.
	*/
	public boolean getCheese() {
		// your code goes here
	}
}

'''

class Mouse:

    # --- Placeholder APIs provided by the problem ---
    def move(self, direction):
        # Implementation provided by the maze environment
        pass

    def hasCheese(self):
        # Implementation provided by the maze environment
        pass

    def getCheese(self):

        # Track visited cells using a set of (x, y) tuples
        visited = set()

        def dfs(x, y):

            if self.hasCheese():
                return True

            visited.add((x, y))

            directions = {
                "up": (0, 1),
                "down": (0, -1),
                "left": (-1, 0),
                "right": (1, 0)
            }

            opposites = {
                "up": "down",
                "down": "up",
                "left": "right",
                "right": "left"
            }

            for d_name, (dx, dy) in directions.items():

                neighbor = (x + dx, y + dy)

                if neighbor not in visited:

                    # 5. Try to move the physical mouse
                    if self.move(d_name):

                        # Recursive call
                        if dfs(neighbor[0], neighbor[1]):
                            return True # Found cheese! Stay here.

                        # 6. Backtrack: If no cheese found that way, move back
                        self.move(opposites[d_name])

            return False

        # Start DFS at origin (0, 0)
        return dfs(0, 0)