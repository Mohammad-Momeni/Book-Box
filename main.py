def isBlocked(boardArray, start, direction):
    x, y = start[0], start[1]
    if direction == 'u':
        if boardArray[x - 1][y] == 'w':
            return True
        if boardArray[x - 1][y] == 'b' and (x - 2 < 0 or boardArray[x - 2][y] == 'b'):
            return True
        if boardArray[x - 1][y] != 'b' or (x - 2 >= 0 and boardArray[x - 2][y] != 'b'):
            return False
    elif direction == 'd':
        if boardArray[x + 1][y] == 'w':
            return True
        if boardArray[x + 1][y] == 'b' and (x + 2 >= len(boardArray) or boardArray[x + 2][y] == 'b'):
            return True
        if boardArray[x + 1][y] != 'b' or (x + 2 < len(boardArray) and boardArray[x + 2][y] != 'b'):
            return False
    elif direction == 'l':
        if boardArray[x][y - 1] == 'w':
            return True
        if boardArray[x][y - 1] == 'b' and (y - 2 < 0 or boardArray[x][y - 1] == 'b'):
            return True
        if boardArray[x][y - 1] != 'b' or (y - 2 >= 0 and boardArray[x][y - 1] != 'b'):
            return False
    elif direction == 'r':
        if boardArray[x][y + 1] == 'w':
            return True
        if boardArray[x][y + 1] == 'b' and (y + 2 >= len(boardArray[x]) or boardArray[x][y + 2] == 'b'):
            return True
        if boardArray[x][y + 1] != 'b' or (y + 2 < len(boardArray[x]) and boardArray[x][y + 2] != 'b'):
            return False

def getActions(boardArray, start):
        actions = []
        x, y = start[0], start[1]
        if(x - 1 >= 0 and not isBlocked(boardArray, start, 'u')):
            actions.append('u')
        if(x + 1 < len(boardArray) and not isBlocked(boardArray, start, 'd')):
            actions.append('d')
        if(y - 1 >= 0 and not isBlocked(boardArray, start, 'l')):
            actions.append('l')
        if(y + 1 < len(boardArray[x]) and not isBlocked(boardArray, start, 'r')):
            actions.append('r')
        return actions

def findStart(boardArray):
    for i in range(len(boardArray)):
        if 'a' in boardArray[i]:
            return i, boardArray[i].index('a')


def bfs_find(boardArray):
    generalVisited = []
    start_point = self.get_position()
    x, y = start_point[0], start_point[1]
    open_list = []
    open_list.append([start_point])
    while not self.current_state[x][y].isGoal:
        if start_point not in generalVisited:
            generalVisited.append(start_point)
        new_path = open_list.pop(0)
        start_point = new_path[len(new_path) - 1]
        x, y = start_point[0], start_point[1]
        actions = getActions(self.current_state, start_point)
        new_start = x - 1, y
        if {'x':-1, 'y': 0} in actions and not new_start in  new_path:
            open_list.append(new_path + [new_start])
        new_start = x + 1, y
        if {'x':1, 'y': 0} in actions and not new_start in  new_path:
            open_list.append(new_path + [new_start])
        new_start = x, y - 1
        if {'x':0, 'y': -1} in actions and not new_start in  new_path:
            open_list.append(new_path + [new_start])
        new_start = x, y + 1
        if {'x':0, 'y': 1} in actions and not new_start in  new_path:
            open_list.append(new_path + [new_start])
    return generalVisited, new_path

def bfs(boardArray):
    start = findStart(boardArray)
    visited, path = bfs_find(boardArray)
    return path

if __name__ == '__main__':
    boardArray = [['f', 'f', 'h'],
                  ['a', 'b', 'f'],
                  ['f', 'f', 'f'],
                ]
    start = findStart(boardArray)
    print(getActions(boardArray, start))