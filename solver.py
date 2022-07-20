import gurobipy as gb
def sudoku_feasible(M_board = [[0 for _ in range(9)] for _ in range(9)]):
    model = gb.Model("sudoku feasibility")
    model.Params.LogToConsole = 0
    n = range(9)
    cells = model.addVars(9, 9, 9, vtype=gb.GRB.BINARY, name='cell')
    # * Already filled cells
    for i in n:
        for j in n:
            if M_board[i][j] != 0:
                val = int(M_board[i][j] - 1)
                # Set so that ILP isn't allowed to change the board
                cells[i, j, val].LB = 1
    # * Each cell has only one value
    model.addConstrs(
        (cells.sum(i, j, '*') == 1
            for i in n
            for j in n),
        name='val'
    )
    # * One value per row
    model.addConstrs(
        (cells.sum(i, '*', val) == 1
            for i in n
            for val in n),
        name='row'
    )
    # * One value per column
    model.addConstrs(
        (cells.sum('*', j, val) == 1
            for j in n
            for val in n),
        name='col'
    )
    # * One value per 3x3 matrix
    model.addConstrs((
        gb.quicksum(
            cells[i, j, val]
            for i in range(subi*3, (subi+1)*3)
            for j in range(subj*3, (subj+1)*3)) == 1
        for val in n
        for subi in range(3)
        for subj in range(3)),
        name='sub-board'
    )
    model.optimize()
    return model.Status == gb.GRB.status.OPTIMAL