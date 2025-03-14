


minutes = int(input())
seconds = int(input())
lenght = float(input())
seconds_for_100m = int(input())

CONTROL_TIME = minutes * 60 + seconds
TIME_DECREASE = lenght / 120
TOTAL_TIME_DECREASE = TIME_DECREASE * 2.5
TIME_MARTIN = (abs(lenght/100) * seconds_for_100m - TOTAL_TIME_DECREASE)

if TIME_MARTIN <= CONTROL_TIME:
    print("Marin Bangiev won an Olympic quota!")
    print(f'His time is {TIME_MARTIN:.3f}.')
else:
    print(f'No, Marin failed! He was {TIME_MARTIN - CONTROL_TIME:.3f} second slower.')