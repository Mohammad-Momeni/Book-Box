import copy
def isBlocked(boardArray, start, direction):
    x, y = start
    if direction == 'u':
        if boardArray[x - 1][y] == 'w':
            return True
        if boardArray[x - 1][y] == 'd':
            return True
        if boardArray[x - 1][y] == 'b' and (x - 2 < 0 or
                                            boardArray[x - 2][y] == 'b' or
                                            boardArray[x - 2][y] == 'd' or
                                            boardArray[x - 2][y] == 'w'):
            return True
        return False
    elif direction == 'd':
        if boardArray[x + 1][y] == 'w':
            return True
        if boardArray[x + 1][y] == 'd':
            return True
        if boardArray[x + 1][y] == 'b' and (x + 2 >= len(boardArray) or
                                            boardArray[x + 2][y] == 'b' or
                                            boardArray[x + 2][y] == 'd' or
                                            boardArray[x + 2][y] == 'w'):
            return True
        return False
    elif direction == 'l':
        if boardArray[x][y - 1] == 'w':
            return True
        if boardArray[x][y - 1] == 'd':
            return True
        if boardArray[x][y - 1] == 'b' and (y - 2 < 0 or
                                            boardArray[x][y - 2] == 'b' or
                                            boardArray[x][y - 2] == 'd' or
                                            boardArray[x][y - 2] == 'w'):
            return True
        return False
    elif direction == 'r':
        if boardArray[x][y + 1] == 'w':
            return True
        if boardArray[x][y + 1] == 'd':
            return True
        if boardArray[x][y + 1] == 'b' and (y + 2 >= len(boardArray[x]) or
                                            boardArray[x][y + 2] == 'b' or
                                            boardArray[x][y + 2] == 'd' or
                                            boardArray[x][y + 2] == 'w'):
            return True
        return False

def getActions(boardArray, start):
        actions = []
        x, y = start
        if(x - 1 >= 0 and not isBlocked(boardArray, start, 'u')):
            actions.append('u')
        if(x + 1 < len(boardArray) and not isBlocked(boardArray, start, 'd')):
            actions.append('d')
        if(y - 1 >= 0 and not isBlocked(boardArray, start, 'l')):
            actions.append('l')
        if(y + 1 < len(boardArray[x]) and not isBlocked(boardArray, start, 'r')):
            actions.append('r')
        return actions
def isGoal(boardArray):
    for i in range(len(boardArray)):
        if 'b' in boardArray[i]:
            return False
    return True

def updateBoard(start, boardArray, move):
    newBoard = copy.deepcopy(boardArray)
    x, y = start
    if move == 'u':
        if newBoard[x - 1][y] == 'b':
            if newBoard[x - 2][y] == 's':
                newBoard[x - 2][y] = 'd'
            else:
                newBoard[x - 2][y] = 'b'
        if newBoard[x - 1][y] == 's':
            newBoard[x - 1][y] = 'as'
        else:
            newBoard[x - 1][y] = 'a'
    elif move == 'd':
        if newBoard[x + 1][y] == 'b':
            if newBoard[x + 2][y] == 's':
                newBoard[x + 2][y] = 'd'
            else:
                newBoard[x + 2][y] = 'b'
        if newBoard[x + 1][y] == 's':
            newBoard[x + 1][y] = 'as'
        else:
            newBoard[x + 1][y] = 'a'
    elif move == 'l':
        if newBoard[x][y - 1] == 'b':
            if newBoard[x][y - 2] == 's':
                newBoard[x][y - 2] = 'd'
            else:
                newBoard[x][y - 2] = 'b'
        if newBoard[x][y - 1] == 's':
            newBoard[x][y - 1] = 'as'
        else:
            newBoard[x][y - 1] = 'a'
    elif move == 'r':
        if newBoard[x][y + 1] == 'b':
            if newBoard[x][y + 2] == 's':
                newBoard[x][y + 2] = 'd'
            else:
                newBoard[x][y + 2] = 'b'
        if newBoard[x][y + 1] == 's':
            newBoard[x][y + 1] = 'as'
        else:
            newBoard[x][y + 1] = 'a'
    if newBoard[x][y] == 'as':
        newBoard[x][y] = 's'
    else:
        newBoard[x][y] = 'f'
    return newBoard

def findStart(boardArray):
    for i in range(len(boardArray)):
        if 'a' in boardArray[i]:
            return i, boardArray[i].index('a')
        elif 'a' in boardArray[i]:
            return i, boardArray[i].index('a')

def bfs_find(boardArray):
    start = findStart(boardArray)
    x, y = start
    open_list = []
    open_list.append([start, boardArray, []])
    while True:
        new_path = open_list.pop(0)
        start = new_path[0]
        x, y = start
        board = new_path[1]
        actions = getActions(board, start)
        new_start = x - 1, y
        if 'u' in actions:
            afterBoard = updateBoard(start, board, 'u')
            afterPath = copy.deepcopy(new_path[2])
            afterPath.append('u')
            if isGoal(afterBoard):
                return afterPath, afterBoard
            open_list.append([new_start, afterBoard, afterPath])
        new_start = x + 1, y
        if 'd' in actions:
            afterBoard = updateBoard(start, board, 'd')
            afterPath = copy.deepcopy(new_path[2])
            afterPath.append('d')
            if isGoal(afterBoard):
                return afterPath, afterBoard
            open_list.append([new_start, afterBoard, afterPath])
        new_start = x, y - 1
        if 'l' in actions:
            afterBoard = updateBoard(start, board, 'l')
            afterPath = copy.deepcopy(new_path[2])
            afterPath.append('l')
            if isGoal(afterBoard):
                return afterPath, afterBoard
            open_list.append([new_start, afterBoard, afterPath])
        new_start = x, y + 1
        if 'r' in actions:
            afterBoard = updateBoard(start, board, 'r')
            afterPath = copy.deepcopy(new_path[2])
            afterPath.append('r')
            if isGoal(afterBoard):
                return afterPath, afterBoard
            open_list.append([new_start, afterBoard, afterPath])

def bfs(boardArray):
    path, board = bfs_find(boardArray)
    return path, board

def dfs_find(boardArray, maxPathLength):
    start = findStart(boardArray)
    x, y = start
    open_list = []
    open_list.append([start, boardArray, ['F']])
    while True:
        new_path = open_list.pop(len(open_list) - 1)
        start = new_path[0]
        x, y = start
        board = new_path[1]
        actions = getActions(board, start)
        new_start = x - 1, y
        afterPath = copy.deepcopy(new_path[2])
        if 'u' in actions and (afterPath[len(afterPath) - 1] != 'd' or board[x - 1][y] == 'b'):
            afterBoard = updateBoard(start, board, 'u')
            afterPath.append('u')
            if isGoal(afterBoard):
                return afterPath[1:], afterBoard
            if len(afterPath) < maxPathLength:
                open_list.append([new_start, afterBoard, afterPath])
        new_start = x + 1, y
        afterPath = copy.deepcopy(new_path[2])
        if 'd' in actions and (afterPath[len(afterPath) - 1] != 'u' or board[x + 1][y] == 'b'):
            afterBoard = updateBoard(start, board, 'd')
            afterPath.append('d')
            if isGoal(afterBoard):
                return afterPath[1:], afterBoard
            if len(afterPath) < maxPathLength:
                open_list.append([new_start, afterBoard, afterPath])
        new_start = x, y - 1
        afterPath = copy.deepcopy(new_path[2])
        if 'l' in actions and (afterPath[len(afterPath) - 1] != 'r' or board[x][y - 1] == 'b'):
            afterBoard = updateBoard(start, board, 'l')
            afterPath.append('l')
            if isGoal(afterBoard):
                return afterPath[1:], afterBoard
            if len(afterPath) < maxPathLength:
                open_list.append([new_start, afterBoard, afterPath])
        new_start = x, y + 1
        afterPath = copy.deepcopy(new_path[2])
        if 'r' in actions and (afterPath[len(afterPath) - 1] != 'l' or board[x][y + 1] == 'b'):
            afterBoard = updateBoard(start, board, 'r')
            afterPath.append('r')
            if isGoal(afterBoard):
                return afterPath[1:], afterBoard
            if len(afterPath) < maxPathLength:
                open_list.append([new_start, afterBoard, afterPath])

def dfs(boardArray):
    for i in range(1, 6):
        try:
            path, board = dfs_find(boardArray, i*10)
            return path, board
        except:
            pass
    return 'Stuck in an Infinite Loop'

def h_calculator(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'b':
                if i == 0 or i == len(board) - 1:
                    if j == 0 or j == len(board[i]) - 1:
                        return 1000
                    if 's' not in board[i]:
                        return 1000
                if j == 0:
                    if 's' not in [row[j] for row in board]:
                        return 1000
                if j == len(board[i]) - 1:
                    if 's' not in [row[j] for row in board]:
                        return 1000
    return 0

def star_find(boardArray):
    start = findStart(boardArray)
    x, y = start
    open_list = []
    open_list.append([start, boardArray, h_calculator(boardArray), []])
    while len(open_list) > 0:
        least = 1000
        leastIndex = 0
        for i in range(len(open_list)):
            if open_list[i][2] < least:
                leastIndex = i
                least = open_list[i][2]
        new_path = open_list.pop(leastIndex)
        start = new_path[0]
        x, y = start
        board = new_path[1]
        cost = new_path[2] + 1
        if cost > 1000:
            continue
        actions = getActions(board, start)
        new_start = x - 1, y
        if 'u' in actions:
            afterBoard = updateBoard(start, board, 'u')
            afterPath = copy.deepcopy(new_path[3])
            afterPath.append('u')
            if isGoal(afterBoard):
                return afterPath, afterBoard
            open_list.append([new_start, afterBoard, cost + h_calculator(afterBoard), afterPath])
        new_start = x + 1, y
        if 'd' in actions:
            afterBoard = updateBoard(start, board, 'd')
            afterPath = copy.deepcopy(new_path[3])
            afterPath.append('d')
            if isGoal(afterBoard):
                return afterPath, afterBoard
            open_list.append([new_start, afterBoard, cost + h_calculator(afterBoard), afterPath])
        new_start = x, y - 1
        if 'l' in actions:
            afterBoard = updateBoard(start, board, 'l')
            afterPath = copy.deepcopy(new_path[3])
            afterPath.append('l')
            if isGoal(afterBoard):
                return afterPath, afterBoard
            open_list.append([new_start, afterBoard, cost + h_calculator(afterBoard), afterPath])
        new_start = x, y + 1
        if 'r' in actions:
            afterBoard = updateBoard(start, board, 'r')
            afterPath = copy.deepcopy(new_path[3])
            afterPath.append('r')
            if isGoal(afterBoard):
                return afterPath, afterBoard
            open_list.append([new_start, afterBoard, cost + h_calculator(afterBoard), afterPath])
    return 'Not Found', afterBoard

def a_star(boardArray):
    path, board = bfs_find(boardArray)
    return path, board

if __name__ == '__main__':
    boardArray = [['s', 'f', 's'],
                  ['a', 'b', 'f'],
                  ['f', 'f', 'f'],
                ]
    # print(bfs(boardArray)[0])
    # print(dfs(boardArray)[0])
    print(a_star(boardArray)[0])