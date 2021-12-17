import os

if __name__ == '__main__':
    with open(os.path.join('..', 'day_17_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            line = line[15:]
            x_str, y_str = line.split(',')
            x_from, x_to = map(int, x_str.split('..'))
            y_from, y_to = map(int, y_str[3:].split('..'))

    highest_y = 0
    best_speed = []
    good_speeds = 0

    for x_speed in range(0, x_to + 5):
        for y_speed in range(-200, 200):
            x = 0
            y = 0
            speed = [x_speed, y_speed]
            start_speed = speed

            highest_y_current = 0
            hit = False
            for step in range(2000):
                x += speed[0]
                y += speed[1]
                overshoot = x > x_to and y > y_to
                stuck_in_x = (x < x_from or x > x_to) and speed[0] == 0
                falling_away = y < y_from and speed[1] < 0
                if overshoot or stuck_in_x or falling_away:
                    break
                if y > highest_y_current:
                    highest_y_current = y
                speed[1] -= 1
                if speed[0] > 0:
                    speed[0] -= 1
                if speed[0] < 0:
                    speed[0] += 1
                s = f'{x}, {y} with speed {start_speed}'
                if x_from <= x <= x_to and y_from <= y <= y_to:
                    hit = True
                    good_speeds += 1
                    s += ' - HIT'
                    # print(s)
                    break
                # print(s)
            if hit and highest_y < highest_y_current:
                highest_y = highest_y_current
                best_speed = start_speed

    print(f'Part 1: {highest_y} from speed {best_speed}')
    print(f'Part 2: {good_speeds}')

# First part answer:  17766
# Second part answer: 1733
