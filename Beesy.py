def read_matrix(n):
    matrix = []
    bee_pos = None
    for i in range(n):
        row = list(input().strip())
        if 'B' in row:
            bee_pos = [i, row.index('B')]
        matrix.append(row)
    return matrix, bee_pos


def move_bee(bee_pos, direction, n):
    row, col = bee_pos
    if direction == "up":
        row = (row - 1) % n
    elif direction == "down":
        row = (row + 1) % n
    elif direction == "left":
        col = (col - 1) % n
    elif direction == "right":
        col = (col + 1) % n
    return [row, col]


def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))


def main():
    n = int(input())
    matrix, bee_pos = read_matrix(n)

    energy = 15
    nectar = 0
    energy_restored = False

    while True:
        command = input()
        if not command:
            break

        # Move bee
        matrix[bee_pos[0]][bee_pos[1]] = '-'
        bee_pos = move_bee(bee_pos, command, n)

        energy -= 1

        row, col = bee_pos
        current = matrix[row][col]

        if current == 'H':
            matrix[row][col] = 'B'
            if nectar >= 30:
                print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
            else:
                print("Beesy did not manage to collect enough nectar.")
            print_matrix(matrix)
            return

        elif current.isdigit():
            nectar += int(current)
            matrix[row][col] = 'B'

        else:
            matrix[row][col] = 'B'

        if energy == 0:
            if nectar >= 30 and not energy_restored:
                energy = nectar - 30
                nectar = 30
                energy_restored = True
            else:
                print("This is the end! Beesy ran out of energy.")
                print_matrix(matrix)
                return


if __name__ == "__main__":
    main()