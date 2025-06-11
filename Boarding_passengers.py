def boarding_passengers(capacity, *passenger_groups):
    boarded_by_program = {}

    remaining_capacity = capacity

    total_passengers = sum(group[0] for group in passenger_groups)
    total_boarded = 0

    for group_size, benefit_program in passenger_groups:
        if remaining_capacity >= group_size:
            remaining_capacity -= group_size
            total_boarded += group_size

            if benefit_program in boarded_by_program:
                boarded_by_program[benefit_program] += group_size
            else:
                boarded_by_program[benefit_program] = group_size

        if remaining_capacity == 0:
            break

    sorted_programs = sorted(boarded_by_program.items(), key=lambda x: (-x[1], x[0]))

    boarding_details = "Boarding details by benefit plan:\n"
    for program, count in sorted_programs:
        boarding_details += f"## {program}: {count} guests\n"

    if total_boarded == total_passengers:
        status_message = "All passengers are successfully boarded!"
    elif remaining_capacity == 0:
        status_message = "Boarding unsuccessful. Cruise ship at full capacity."
    else:
        status_message = f"Partial boarding completed. Available capacity: {remaining_capacity}."

    return boarding_details + status_message