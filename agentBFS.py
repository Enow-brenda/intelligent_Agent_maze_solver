import pygame


pygame.init()

WIDTH = 1200
HEIGHT = 600

min_x, min_y = 0, 40
max_x, max_y = WIDTH - 240, HEIGHT


def can_move(new_x, new_y, world, visited):
    """Check if the new position is within bounds and is a valid move."""
    if min_x <= new_x < max_x and min_y <= new_y < max_y:
        row = (new_y - 40) // 40  # Adjusted for y-offset starting at 40
        col = new_x // 40
        if world[row][col] == 1 and not any(node[0] == row and node[1] == col for node in visited):
            return True
    return False


class AgentBFS:
    def __init__(self, image, start_x, start_y):
        self.image = image
        self.x = start_x
        self.y = start_y
        self.visited = []
        self.steps = 0
        self.queue = [(start_x // 40,(start_y - 40 )//40)]  # Queue for BFS
        self.found_target = False
        self.target_position = None
        self.parent_nodes = {(start_x // 40,(start_y - 40 )//40):None}
        self.path = []  # To keep track of the path taken
        self.current_step = 0  # To keep track of the current step in the path

    def bfs(self, world):
        while self.queue:
            current = self.queue.pop(0)
            self.visited.append(current)
            self.steps += 1
            if world[current[0]][current[1]] == 2:
                print("Target Reached")
                print("Steps :", self.steps)
                self.found_target = True
                self.reconstruct_path(self.parent_nodes,current)
                return

            self.getNeigbourCells(current[0], current[1],world)
        print("Target not reachable.")

    def reconstruct_path(self, parent_map, target):
        """Reconstruct the path from the target to the start."""
        current = target
        while current is not None:
            self.path.append(current)
            current = parent_map[current]
        self.path.reverse()  # Reverse to get the path from start to target
        print(f"Path taken: {self.path}")

    def getNeigbourCells(self,row, col,world):
        # up direction
        new_row = row - 1
        new_col = col
        if self.isValid(new_row, new_col,world) and (new_row, new_col) not in self.visited:
            self.queue.append((new_row, new_col))
            self.parent_nodes[new_row,new_col]= (row,col)

        # right direction
        new_row = row
        new_col = col + 1
        if self.isValid(new_row, new_col,world) and (new_row, new_col) not in self.visited:
            print("it moved right")
            self.queue.append((new_row, new_col))
            self.parent_nodes[new_row,new_col]= (row,col)

        # down direction
        new_row = row + 1
        new_col = col
        if self.isValid(new_row, new_col,world) and (new_row, new_col) not in self.visited:
            print("it moved down")
            self.queue.append((new_row, new_col))
            self.parent_nodes[new_row, new_col] = (row, col)

        # left direction
        new_row = row
        new_col = col - 1
        if self.isValid(new_row, new_col,world) and (new_row, new_col) not in self.visited:
            self.queue.append((new_row, new_col))
            self.parent_nodes[new_row,new_col]= (row,col)

    def isValid(self,row, col,world):
        print("Neighbour:", row, ",", col)
        if (0 <= row < len(world)) and (0 <= col < len(world[0])):
            return world[row][col] != 0
        return False

    def move(self):

        """Move the agent along the path every second after finding the target."""
        if self.found_target and self.path:
            self.x = self.path[0][1] * 40
            self.y = (self.path[0][0] *40)+40
            self.path.pop(0)


    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


