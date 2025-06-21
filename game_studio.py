def sort_games(*args, **kwargs):
    console_games = []
    pc_games = []

    for platform, game_title in args:
        if platform == "console":
            console_games.append(game_title)
        elif platform == "pc":
            pc_games.append(game_title)

    console_releases = []
    pc_releases = []

    for release_id, game_title in kwargs.items():
        if game_title in console_games:
            console_releases.append((release_id, game_title))
        elif game_title in pc_games:
            pc_releases.append((release_id, game_title))

    console_releases.sort(key=lambda x: x[0])

    pc_releases.sort(key=lambda x: x[0], reverse=True)

    result = []

    if console_releases:
        result.append("Console Games:")
        for release_id, game_title in console_releases:
            release_date = "_".join(release_id.split("_")[:-1])
            result.append(f">>>{release_date}: {game_title}")

    if pc_releases:
        result.append("PC Games:")
        for release_id, game_title in pc_releases:
            release_date = "_".join(release_id.split("_")[:-1])
            result.append(f"<<<{release_date}: {game_title}")



    return "\n".join(result)

