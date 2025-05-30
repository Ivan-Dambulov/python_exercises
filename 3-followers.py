def facebook_followers():
    followers = {}

    while True:
        command = input()
        if command == "Log out":
            break

        parts = command.split(": ")
        action = parts[0]

        if action == "New follower":
            username = parts[1]
            if username not in followers:
                followers[username] = {"likes": 0, "comments": 0}

        elif action == "Like":
            username, count = parts[1], int(parts[2])
            if username not in followers:
                followers[username] = {"likes": count, "comments": 0}
            else:
                followers[username]["likes"] += count

        elif action == "Comment":
            username = parts[1]
            if username not in followers:
                followers[username] = {"likes": 0, "comments": 1}
            else:
                followers[username]["comments"] += 1

        elif action == "Blocked":
            username = parts[1]
            if username in followers:
                del followers[username]
            else:
                print(f"{username} doesn't exist.")

    print(f"{len(followers)} followers")
    for user, stats in followers.items():
        print(f"{user}: {stats['likes'] + stats['comments']}")

facebook_followers()
