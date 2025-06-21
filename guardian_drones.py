def assemble_drones():
    drones = {
        "Sentinel-X": 100,
        "Viper-MKII": 85,
        "Aegis-7": 75,
        "Striker-R": 65,
        "Titan-Core": 55
    }

    mechanical_parts = list(map(int, input().split()))
    power_cells = list(map(int, input().split()))

    assembled_drones = []
    built_drones = set()

    while mechanical_parts and power_cells and len(assembled_drones) < 5:
        while power_cells and power_cells[0] <= 0:
            power_cells.pop(0)

        if not power_cells:
            break

        mechanical_part = mechanical_parts.pop()
        power_cell = power_cells.pop(0)

        total_power = mechanical_part + power_cell

        exact_match_found = False
        for drone_name, required_power in drones.items():
            if total_power == required_power and drone_name not in built_drones:
                assembled_drones.append(drone_name)
                built_drones.add(drone_name)
                exact_match_found = True
                break

        if not exact_match_found:
            suitable_drone = None
            max_suitable_power = 0

            for drone_name, required_power in drones.items():
                if (required_power < total_power and
                        required_power > max_suitable_power and
                        drone_name not in built_drones):
                    suitable_drone = drone_name
                    max_suitable_power = required_power

            if suitable_drone:
                assembled_drones.append(suitable_drone)
                built_drones.add(suitable_drone)
                reduced_power = power_cell - 30
                if reduced_power > 0:
                    power_cells.append(reduced_power)
            else:
                reduced_power = power_cell - 1
                if reduced_power > 0:
                    power_cells.append(reduced_power)

    if len(assembled_drones) == 5:
        print("Mission Accomplished! All Guardian Drones activated!")
    else:
        print("Mission Failed! Some drones were not built.")

    if assembled_drones:
        print(f"Assembled Drones: {', '.join(assembled_drones)}")

    if mechanical_parts:
        print(f"Mechanical Parts: {', '.join(map(str, reversed(mechanical_parts)))}")

    remaining_power_cells = [cell for cell in power_cells if cell > 0]
    if remaining_power_cells:
        print(f"Power Cells: {', '.join(map(str, remaining_power_cells))}")


assemble_drones()