from collections import deque

suggested_links = deque(map(int, input().split()))
featured_articles = list(map(int, input().split()))
target_engagement = int(input())

final_feed = []

while suggested_links and featured_articles:
    fifo_val = suggested_links.popleft()
    lifo_val = featured_articles.pop()

    # If values are equal
    if fifo_val == lifo_val:
        final_feed.append(0)
        continue

    if fifo_val > lifo_val:
        greater, smaller = fifo_val, lifo_val
        source = 'FIFO'
    else:
        greater, smaller = lifo_val, fifo_val
        source = 'LIFO'

    remainder = greater % smaller

    if source == 'LIFO':
        final_feed.append(remainder)
        if remainder != 0:
            featured_articles.append(remainder * 2)
    else:
        final_feed.append(-remainder)
        if remainder != 0:
            suggested_links.append(remainder * 2)

total_engagement = sum(final_feed)

print("Final Feed:", ', '.join(map(str, final_feed)))
if total_engagement >= target_engagement:
    print(f"Goal achieved! Engagement Value: {total_engagement}")
else:
    shortfall = target_engagement - total_engagement
    print(f"Goal not achieved! Short by: {shortfall}")
