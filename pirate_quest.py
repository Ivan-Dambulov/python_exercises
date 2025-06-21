def pirate_treasure_hunt():
    n = int(input())

    sea_map = []
    for _ in range(n):
        sea_map.append(list(input().strip()))

    ship_row, ship_col = 0, 0
    total_treasures = 0

    for i in range(n):
        for j in range(n):
            if sea_map[i][j] == 'S':
                ship_row, ship_col = i, j
            elif sea_map[i][j] == '*':
                total_treasures += 1

    durability = 100
    collected_treasures = 0
    charm_used = False
    first_move = True

    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }

    while True:
        try:
            command = input().strip()
        except EOFError:
            break

        if command == 'stop':
            break

        if first_move:
            sea_map[ship_row][ship_col] = '.'
            first_move = False

        if command in directions:
            dr, dc = directions[command]
            ship_row = (ship_row + dr) % n
            ship_col = (ship_col + dc) % n

        current_cell = sea_map[ship_row][ship_col]

        if current_cell == '*':
            collected_treasures += 1
            sea_map[ship_row][ship_col] = '.'

        elif current_cell == 'C':
            if not charm_used:
                durability = min(100, durability + 25)  # Don't exceed max durability
                charm_used = True
            sea_map[ship_row][ship_col] = '.'

        elif current_cell == 'M':
            durability -= 25
            sea_map[ship_row][ship_col] = '.'

        if durability <= 0:
            print(f"Shipwreck! Last known coordinates ({ship_row}, {ship_col})")
            print(f"Ship Durability: 0")
            remaining_treasures = total_treasures - collected_treasures
            if remaining_treasures > 0:
                print(f"Unclaimed chests: {remaining_treasures}")

            sea_map[ship_row][ship_col] = 'S'
            for row in sea_map:
                print(''.join(row))
            return

        if collected_treasures == total_treasures:
            print("Yo-ho-ho! All treasure chests collected!")
            print(f"Ship Durability: {durability}")

            sea_map[ship_row][ship_col] = 'S'
            for row in sea_map:
                print(''.join(row))
            return

    print("Retreat! Some treasures remain unclaimed.")
    print(f"Ship Durability: {durability}")
    remaining_treasures = total_treasures - collected_treasures
    if remaining_treasures > 0:
        print(f"Unclaimed chests: {remaining_treasures}")

    sea_map[ship_row][ship_col] = 'S'
    for row in sea_map:
        print(''.join(row))


pirate_treasure_hunt()