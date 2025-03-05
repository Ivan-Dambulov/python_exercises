MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
TIME_INCRIMENT = 15


hour = int(input())
minutes = int(input())

minutes += TIME_INCRIMENT

if minutes >= MINUTES_IN_HOUR:
    hour += 1
    minutes -= MINUTES_IN_HOUR

if hour >= HOURS_IN_DAY:
    hour -= HOURS_IN_DAY

if minutes < 10:
    print(f'{hour}:{minutes:02d}')
else:
    print(f'{hour}:{minutes}')