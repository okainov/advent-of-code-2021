import os


def sum_population(population):
    total_fishes = 0
    for x in population:
        total_fishes += population[x]
    return total_fishes


if __name__ == '__main__':
    first = True
    boards = []
    current_board = {}
    current_line = 0
    population = {}
    with open(os.path.join('..', 'day_6_input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            fishes = line.split(',')
            for fish in fishes:
                fish = int(fish)
                if fish not in population:
                    population[fish] = 0
                population[fish] += 1

    # 80 for part 1, 256 for part 2
    n_days = 80
    for day in range(n_days):
        # Simulate each cycle
        new_population = {}
        for cycle in population:
            if cycle == 0:
                # do the magic
                # reset 0 to 6
                if 6 not in new_population:
                    new_population[6] = 0
                new_population[6] += population[cycle]
                # Add new fishes with 8
                if 8 not in new_population:
                    new_population[8] = 0
                new_population[8] += population[cycle]
            else:
                # Just decrease
                if cycle - 1 not in new_population:
                    new_population[cycle - 1] = 0
                new_population[cycle - 1] += population[cycle]
        population = new_population

    print(sum_population(population))

    # First part answer:  345387
    # Second part answer: 1574445493136
