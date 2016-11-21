import TikTokLib as tl

grid = {1:'O',2:'X',3:'X',4:'O',5:'X',6:'O',7:' ',8:' ',9:'O'}

#Ask the human player what symbol he/she prefers
symbol = input('Who is starting? (H/M) ')
#X always starts the game
if symbol is 'H':
    turn = {'X':'human', 'O':'machine'}
else:
    turn = {'X':'machine', 'O':'human'}



gridStruct = {'grid': grid,
              'score': None,
              'turn': 'X',
              'children': []}

print(gridStruct)
#Generate Children
numChildren = 0
cellsInGrid = list(grid.values())
for c in cellsInGrid:
    if c is '':
        numChildren += 1
print(numChildren)

def generateChildren(gridStruct):
    '''
    #This function creates the possible moves on the game
    :param gridStruct: dic grid, turn, score, children
    :return: children, list of gridstructs
    '''
    #Create the Children
    children = []
    humanScore = 0
    for key, value in gridStruct['grid'].items():
        #we create a child if cell is empty
        if value is ' ':
            gridChild = grid.copy()
            gridChild[key] = gridStruct['turn']

            nextTurn = 'X' if gridStruct['turn'] is 'O' else 'O'

            tl.displayGrid(gridChild)
            gridStructChild = {'grid': gridChild,
                                'score': None,
                                'turn': nextTurn,
                                'children': None}
            children.append(gridStructChild)

    if turn == 'human':
        tl.checkWinner(grid) == gridStruct['turn']
        humanScore = -10

    else:
        None
    print('The human score is now: ' + str(humanScore))

    return children

def getChildren(gridStruct):
    gridChildStruct = {}
    grid = gridStruct['grid']
    score = gridStruct['score']
    turn = gridStruct['turn']
    children = gridStruct['children']

    if score is None:
        for cellkey, cellValue in grid.items():
            if cellValue is ' ':
                gridChild = grid.copy()
                gridChild[cellkey] = cellValue

                scoreChild = tl.checkWinner(gridChild)
                turnChild = 'X' if turn is 'O' else 'O'

                gridChildStruct['grid'] = gridChild
                gridChildStruct['score'] = scoreChild
                gridChildStruct['turn'] = turnChild
                gridChildStruct['children'] = []
                tl.displayGrid(gridChild)

                children.append(getChildren(gridStruct))
        gridStruct['children'] = children

    return gridStruct

children = generateChildren(gridStruct)
getChildren(gridStruct)
