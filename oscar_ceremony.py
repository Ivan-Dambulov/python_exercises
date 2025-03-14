rent = int(input())

STATUES = (rent - (rent * 0.3))
CATERING = STATUES - (STATUES * 0.15)
SOUND = CATERING / 2



print(f'{rent + STATUES + CATERING + SOUND:.2f}')
