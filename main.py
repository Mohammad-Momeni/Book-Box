def isBlocked(boardArray, x, y):
    if boardArray[x][y] == 'w':
        return False
    if boardArray[x][y] == 'b':
        pass
def get_actions(boardArray, start):
        actions = []
        x, y = start[0], start[1]
        if(x - 1 >= 0 and (not boardArray[x - 1][y].isBlocked)):
            actions.append()
        if(x + 1 < params.rows and not boardArray[x + 1][y].isBlocked):
            actions.append({'x': 1, 'y': 0})
        if(y - 1 >= 0 and not boardArray[x][y - 1].isBlocked):
            actions.append({'x': 0, 'y': -1})
        if(y + 1 < params.cols and not boardArray[x][y + 1].isBlocked):
            actions.append({'x': 0, 'y': 1})
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
        actions = get_actions(self.current_state, start_point)
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
    
    visited, path = bfs_find(boardArray)
    return path

if __name__ == '__main__':
    boardArray = [['f', 'f', 'h'],
                  ['a', 'b', 'f'],
                  ['f', 'f', 'f'],
                ]
    print(findStart(boardArray=boardArray))
    print(boardArray[0])
