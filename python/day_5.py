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
    field = {}
    with open(os.path.join('..', 'day_5_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            coords = []
            for part in line.split('->'):
                for coord in part.split(','):
                    number = int(coord.strip())
                    coords.append(number)
            x1, y1, x2, y2 = coords



            if x1 == x2:
                # Horizontal
                # Swap just in case so y2 is always bigger
                if y2 < y1:
                    y1, y2 = y2, y1
                if x1 not in field:
                    field[x1] = {}
                for y in range(y1, y2+1):
                    if y not in field[x1]:
                        field[x1][y] = 0
                    field[x1][y] += 1
            if y1 == y2:
                # Vertical
                # Swap just in case so x2 is always bigger
                if x2 < x1:
                    x1, x2 = x2, x1
                for x in range(x1, x2+1):
                    if x not in field:
                        field[x] = {}
                    if y1 not in field[x]:
                        field[x][y1] = 0
                    field[x][y1] += 1


    overlaps = 0
    for x in field:
        for y in field[x]:
            if field[x][y] > 1:
                overlaps += 1

    print(overlaps)

    # First part answer:  6007
    # Second part answer: 13158
