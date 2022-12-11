def toglislashn(numbers):

    return [s.rstrip('\n') for s in numbers]


def count_visible_numbers(numbers):

    numbers = toglislashn(numbers)

    numbers = [[int(c) for c in row] for row in numbers]

    rows = len(numbers)
    cols = len(numbers[0])

    count = 0

    for r in range(rows):
        for c in range(cols):

            if all(numbers[i][c] < numbers[r][c] for i in range(r)):
                count += 1

            elif all(numbers[i][c] < numbers[r][c] for i in range(r + 1, rows)):
                count += 1

            elif all(numbers[r][i] < numbers[r][c] for i in range(c)):
                count += 1

            elif all(numbers[r][i] < numbers[r][c] for i in range(c + 1, cols)):
                count += 1

    return count



file = open("input_f.txt", "r")
lines = file.readlines()

print(count_visible_numbers(lines))