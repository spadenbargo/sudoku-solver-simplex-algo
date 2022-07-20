def gen_board(input_p):
    b_nums = [i fori in range(1, 10)]
    board = [[0 for j in range(9)] for i in range(9)]  # blank board
    for i in range(len(board)):
        for j in range(len(board[i])):
            # Avoid weird float things
            if rand.random() > float(input_p):  # cell left empty
                board[i][j] = 0
            else:
                # picked randomly and uniformly
                board[i][j] = rand.choice(b_nums)
    return board 
