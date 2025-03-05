WATER_RESISTANCE = 15
WATER_RESISTANCE_DELAY = 12.5

record_in_seconds = float(input())
distance_in_meters = float(input())
time_for_swimming_1m = float(input())

delay = (distance_in_meters // WATER_RESISTANCE) * WATER_RESISTANCE_DELAY
swimming_record = (time_for_swimming_1m * distance_in_meters) + delay

if swimming_record < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {swimming_record:.2f} seconds.')
else:
    print(f'No, he failed! He was {abs(record_in_seconds - swimming_record):.2f} seconds slower.')