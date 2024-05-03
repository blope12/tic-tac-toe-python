import curses

def start_game(stdscr):

    wins = {'X': 0, 'O': 0}  # Dictionary to store the number of wins for each player
    while True:  # Continue indefinitely
        stdscr.clear()
        stdscr.addstr(0, 0, "Welcome to Tic-Tac-Toe!")
        stdscr.addstr(2, 0, "Press 'X' or 'O' to place your mark.")
        stdscr.addstr(3, 0, "Use arrow keys to navigate the board.")
        stdscr.addstr(5, 0, "   |   |   ")
        stdscr.addstr(6, 0, "---+---+---")
        stdscr.addstr(7, 0, "   |   |   ")
        stdscr.addstr(8, 0, "---+---+---")
        stdscr.addstr(9, 0, "   |   |   ")

        # Set up the game board
        board = [[' ' for _ in range(3)] for _ in range(3)]
        row, col = 5, 0
        player = 'X'

        while True:
            stdscr.move(row, col)

            # Player's move
            key = stdscr.getch()
            if key == curses.KEY_LEFT and col > 0:
                col -= 4
            elif key == curses.KEY_RIGHT and col < 8:
                col += 4
            elif key == curses.KEY_UP and row > 5:
                row -= 2
            elif key == curses.KEY_DOWN and row < 9:
                row += 2
            elif key == ord(' ') and board[(row - 5) // 2][(col // 4)] == ' ':
                make_move(board, (row - 5) // 2, col // 4, player)
                stdscr.addch(row, col, player) 
                player = 'O' if player == 'X' else 'X'

            # Check for winner or draw
            if check_draw(board):
                stdscr.addstr(11, 0, "It's a draw!")
                break
            winner = check_winner(board)
            if winner:
                stdscr.addstr(11, 0, f"Player {winner} wins!")
                wins[winner] += 1  # Update the number of wins for the winning player
                break

        # Display the number of wins for each player just for show...
        stdscr.addstr(12, 0, f"Player X num wins: {wins['X']}")
        stdscr.addstr(13, 0, f"Player O num wins: {wins['O']}")
        stdscr.addstr(14, 0, "Press any key to start a new game.")

        stdscr.getch()  # Wait for a key press to start a new game...

def make_move(board, row, col, player):

    if board[row][col] == ' ': 
        board[row][col] = player
        return True
    else:
        return False

def check_winner(board):

    winner = None  # Set the default value to None
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            winner = board[i][0]
            break
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            winner = board[0][i]
            break
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        winner = board[0][2]
    return winner

def check_draw(board):

    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def main():
    curses.wrapper(start_game)

if __name__ == "__main__":
    main()
