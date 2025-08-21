def create_board() -> list:
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append('-')
        board.append(row)
    return board

def display_board(board):
        print(f'''|_{board[0][0]}_|_{board[1][0]}_|_{board[2][0]}_|
|_{board[0][1]}_|_{board[1][1]}_|_{board[2][1]}_|
|_{board[0][2]}_|_{board[1][2]}_|_{board[2][2]}_|''')
        
board = create_board()
display_board(board)

def player_input(player):
    position = int(input(f'Player {player} enter your position from 1 to 9: '))



