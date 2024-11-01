grid = [[3, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0,1, 1, 1, 1, 0,1],
    [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0,1],
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1,1],
    [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0,0],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0,0],
    [0, 0, 1, 0, 1, 1, 1, 2, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0,1],
    [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0,1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1,1],
    [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0,1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0,0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1,0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,1],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0,1],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0,0]
]
queue = [(0,0)]

stack = [(0,0)]
visited= []




def moveDfs():
    steps = 0
    while stack:
        current = stack.pop(-1)
        visited.append(current)
        steps +=1
        print("visited",current)

        if(grid[current[0]][current[1]] == 2):
            print("Target Reached")
            print("Steps: " ,steps)
            return

        getReadyNeighbours(current[0],current[1])

        print("Visited:",visited)
        print("Stack:", stack)
    print("No Path to the Target")

def getReadyNeighbours(row,col):
    #up direction
    new_row = row -1
    new_col= col
    if isValid(new_row,new_col) and (new_row,new_col) not in visited:
        stack.append((new_row,new_col))

    # right direction
    new_row = row
    new_col = col +1
    if isValid(new_row,new_col) and (new_row,new_col) not in visited:
        stack.append((new_row,new_col))

    #down direction
    new_row = row + 1
    new_col = col
    if isValid(new_row,new_col) and (new_row,new_col) not in visited:
        stack.append((new_row,new_col))

    #left direction
    new_row = row
    new_col = col -1
    if isValid(new_row,new_col) and (new_row,new_col) not in visited:
        stack.append((new_row,new_col))

def movebfs():
    steps =0
    while queue:
        current = queue.pop(0)
        visited.append(current)
        steps += 1

        print('visited: ',current)


        if grid[current[0]][current[1]] == 2:
            print("Target Reached")
            print("Steps :",steps)
            return

        getNeigbourCells(current[0], current[1])

        print("Visited:",visited)
        print("Queue:", queue)
    print("No Path to the Target")

def isValid(row,col):
    print("Neighbour:", row, ",", col)
    if (0 <= row < len(grid)) and (0 <= col < len(grid[0])):
        return grid[row][col] != 0
    return False

def getNeigbourCells(row,col):
    #up direction
    new_row = row -1
    new_col= col
    if isValid(new_row,new_col) and (new_row,new_col) not in visited:
        queue.append((new_row,new_col))

    # right direction
    new_row = row
    new_col = col +1
    if isValid(new_row,new_col) and (new_row,new_col) not in visited:
        print("it moved right")
        queue.append((new_row,new_col))

    #down direction
    new_row = row + 1
    new_col = col
    if isValid(new_row,new_col) and (new_row,new_col) not in visited:
        print("it moved down")
        queue.append((new_row,new_col))

    #left direction
    new_row = row
    new_col = col -1
    if isValid(new_row,new_col) and (new_row,new_col) not in visited:
        queue.append((new_row,new_col))

moveDfs()
#movebfs()

