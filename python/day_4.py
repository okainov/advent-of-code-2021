import operator
import os


def mark_number_in_board(board, number):
    sum_unmarked = 0
    marked = False
    for i in board:
        for j in board[i]:
            current_number = list(board[i][j].keys())[0]
            if number == current_number:
                board[i][j][number] = True
                marked = True
            if not board[i][j][current_number]:
                sum_unmarked += int(current_number)
    return marked, sum_unmarked


def is_winning(board):
    for i in range(len(board)):
        # Check column i
        column_all_trues = True
        for line in board:
            current_number = list(board[line][i].keys())[0]
            if not board[line][i][current_number]:
                column_all_trues = False
                break
        if column_all_trues:
            return True

        # Check line i
        row_all_trues = True
        for q in board[i]:
            current_number = list(board[i][q].keys())[0]
            if not board[i][q][current_number]:
                row_all_trues = False
        if row_all_trues:
            return True


if __name__ == '__main__':
    first = True
    boards = []
    current_board = {}
    current_line = 0
    with open(os.path.join('..', 'day_4_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            line = " ".join(filter(lambda a: operator.is_not(a, ""), line.strip().split(" ")))

            if first:
                sequence = line.split(',')
                first = False
                continue

            if not line:
                # Separator between boards
                if current_board:
                    boards.append(current_board)
                current_board = {}
                current_line = 0
            else:
                # Line of the board
                numbers = line.split(' ')
                current_board[current_line] = {}
                for i, number in enumerate(numbers):
                    current_board[current_line][i] = {number: False}
                current_line += 1
        else:
            # Add final board
            boards.append(current_board)

    # Play bingo

    board_which_have_won = set()
    for number in sequence:
        for n, board in enumerate(boards):
            marked, sum_unmarked = mark_number_in_board(board, number)
            if n not in board_which_have_won and is_winning(board):
                board_which_have_won.add(n)

                print(f'Board {n} has won with: {sum_unmarked * int(number)}')

    # First part answer:  54275
    # Second part answer: 13158
