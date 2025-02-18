def calculate_burger_bus_profits():
    # Get number of cities
    num_cities = int(input())
    total_profit = 0

    # Process each city
    for city_num in range(1, num_cities + 1):
        # Get city information
        city_name = input()
        income = float(input())
        expenses = float(input())

        # Calculate profit for current city
        current_profit = income

        # Check if it's a rainy day (every 5th city)
        if city_num % 5 == 0:
            # Loss of 10% of income on rainy days
            current_profit = income * 0.90
        # Check for special event (every 3rd city, but not on rainy days)
        elif city_num % 3 == 0:
            # Additional 50% expenses for special event
            expenses *= 1.50

        # Calculate final profit for the city
        current_profit -= expenses

        # Add to total profit
        total_profit += current_profit

        # Print profit for current city
        print(f"In {city_name} Burger Bus earned {current_profit:.2f} leva.")

    # Print total profit
    print(f"Burger Bus total profit: {total_profit:.2f} leva.")


# Run the program
calculate_burger_bus_profits()