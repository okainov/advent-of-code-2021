import os


def sum_pairs(pair_1, pair_2):
    return pair_1[0] + pair_2[0], pair_1[1] + pair_2[1]


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

            x_inc = 0
            y_inc = 0

            if x1 == x2:
                # Horizontal
                if y2 < y1:
                    y_inc = -1
                else:
                    y_inc = 1
            elif y1 == y2:
                # Vertical
                if x2 < x1:
                    x_inc = -1
                else:
                    x_inc = 1
            else:
                # Should be diagonal
                # Uncomment to get part 1
                # continue
                x_inc = 1
                y_inc = 1
                if x2 < x1:
                    x_inc = -1
                if y2 < y1:
                    y_inc = -1
            increment = (x_inc, y_inc)

            current_point = (x1, y1)

            if increment == (0, 0):
                # Not a real case, but just to handle part1/2 switch
                continue

            while True:
                x, y = current_point
                if x not in field:
                    field[x] = {}
                if y not in field[x]:
                    field[x][y] = 0
                field[x][y] += 1

                if current_point == (x2, y2):
                    break

                current_point = sum_pairs(current_point, increment)

    overlaps = 0
    for x in field:
        for y in field[x]:
            if field[x][y] > 1:
                overlaps += 1

    print(overlaps)

    # First part answer:  6007
    # Second part answer: 19349
