class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

    def check_win(self):
        win_conditions = [
            [self.board[0][0], self.board[0][1], self.board[0][2]],  # top row
            [self.board[1][0], self.board[1][1], self.board[1][2]],  # middle row
            [self.board[2][0], self.board[2][1], self.board[2][2]],  # bottom row
            [self.board[0][0], self.board[1][0], self.board[2][0]],  # left column
            [self.board[0][1], self.board[1][1], self.board[2][1]],  # middle column
            [self.board[0][2], self.board[1][2], self.board[2][2]],  # right column
            [self.board[0][0], self.board[1][1], self.board[2][2]],  # diagonal top-left to bottom-right
            [self.board[2][0], self.board[1][1], self.board[0][2]],  # diagonal bottom-left to top-right
        ]
        return [self.current_player, self.current_player, self.current_player] in win_conditions

    def check_tie(self):
        return all(cell != " " for row in self.board for cell in row)

    def get_move(self):
        while True:
            try:
                row = int(input(f"Player {self.current_player}, enter row (1-3): ")) - 1
                col = int(input(f"Player {self.current_player}, enter column (1-3): ")) - 1
                if row in range(3) and col in range(3):
                    if self.board[row][col] == " ":
                        return row, col
                    else:
                        print("This position is already taken. Try again.")
                else:
                    print("Invalid input. Please enter numbers between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter numbers.")

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        while True:
            self.print_board()
            row, col = self.get_move()
            self.board[row][col] = self.current_player

            if self.check_win():
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break

            if self.check_tie():
                self.print_board()
                print("It's a tie!")
                break

            self.switch_player()

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()