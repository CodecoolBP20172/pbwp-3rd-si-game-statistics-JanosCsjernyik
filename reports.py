def file_filtering(file_name):
    path = "/home/janos/codecool/python/3SI/pbwp-3rd-si-game-statistics-JanosCsjernyik/"+file_name
    game_list = []
    with open(path) as txt:
        for line in txt:
            lines = line.split("\t")
            game_list.append(lines)
    return game_list


def count_games(file_name):
    return len(file_filtering(file_name))


def decide(file_name, year):
    for games in range(count_games(file_name)):
        if file_filtering(file_name)[games][2] == str(year):
            return True
    return False


def get_latest(file_name):
    years_list = []
    for games in range(count_games(file_name)):
        years_list.append(file_filtering(file_name)[games][2])
    max_year = years_list.index(max(years_list))
    return file_filtering(file_name)[max_year][0]


def count_by_genre(file_name, genre):
    summ = 0
    for games in range(count_games(file_name)):
        if file_filtering(file_name)[games][3] == str(genre):
            summ += 1
    return summ


def get_line_number_by_title(file_name, title):
    for games in range(count_games(file_name)):
        if file_filtering(file_name)[games][0] == str(title):
            return games + 1
    else:
        raise ValueError("No title found")


def sort_abc(file_name):
    game_list = []
    for games in range(count_games(file_name)):
        game_list.append(file_filtering(file_name)[games][0])
    return sorted(game_list, key=str.lower)


def get_genres(file_name):
    genres_list = []
    for games in range(count_games(file_name)):
        genres_list.append(file_filtering(file_name)[games][3])
    return sorted(set(genres_list))


def when_was_top_sold_fps(file_name):
    fps_list = []
    copies_list = []

    for games in range(count_games(file_name)):
        if file_filtering(file_name)[games][3] == "First-person shooter":
            fps_list.append(file_filtering(file_name)[games])

    for games in range(len(fps_list)):
        copies_list.append(fps_list[games][1])

    int_copies_list = [float(i) for i in copies_list]
    best_seller_index = int_copies_list.index(max(int_copies_list))
    answer = int(fps_list[best_seller_index][2])
    return answer


# Report functions
