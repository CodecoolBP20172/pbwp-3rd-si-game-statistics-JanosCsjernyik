import math


def file_filtering(file_name):
    path = "/home/janos/codecool/python/3SI/pbwp-3rd-si-game-statistics-JanosCsjernyik/part2/"+file_name
    game_list = []
    with open(path) as txt:
        for line in txt:
            lines = line.split("\t")
            game_list.append(lines)
    return game_list


def count_games(file_name):
    return len(file_filtering(file_name))


def get_most_played(file_name):
    sold_copies = []
    for game in range(count_games(file_name)):
        sold_copies.append(file_filtering(file_name)[game][1])
    float_sold_copies = [float(copy) for copy in sold_copies]
    most_played_index = float_sold_copies.index(max(float_sold_copies))
    most_played = file_filtering(file_name)[most_played_index][0]
    return most_played


def sum_sold(file_name):
    games_sold = []
    for game in range(count_games(file_name)):
        games_sold.append(file_filtering(file_name)[game][1])
    float_games_sold = [float(copy) for copy in games_sold]
    summa = sum(float_games_sold)
    return summa


def get_selling_avg(file_name):
    games_sold = []
    for game in range(count_games(file_name)):
        games_sold.append(file_filtering(file_name)[game][1])
    float_games_sold = [float(copy) for copy in games_sold]
    avg_selling = sum(float_games_sold)/len(float_games_sold)
    return avg_selling


def count_longest_title(file_name):
    game_names = []
    names_lenght = []
    for game in range(count_games(file_name)):
        game_names.append(file_filtering(file_name)[game][0])
    for game in range(len(game_names)):
        names_lenght.append(len(game_names[game]))
    longest_name_char = max(names_lenght)
    return longest_name_char


def get_date_avg(file_name):
    game_dates = []
    for game in range(count_games(file_name)):
        game_dates.append(file_filtering(file_name)[game][2])
    float_game_dates = [float(copy) for copy in game_dates]
    avg_selling = math.ceil(sum(float_game_dates)/len(float_game_dates))
    return avg_selling


def get_game(file_name, title):
    for game in file_filtering(file_name):
        if game[0] == title:
            length = len(game[4])
            return [game[0], float(game[1]), int(game[2]), game[3], game[4][0:length-1]]
    else:
        raise ValueError("There is no game named like that in the file!")


def count_grouped_by_genre(file_name):
    genre_list = []
    genre_dic = {}
    for game in file_filtering(file_name):
        genre_list.append(game[3])
    for genre in genre_list:
        if genre in genre_dic.keys():
            genre_dic[genre] += 1
        else:
            genre_dic[genre] = 1
    return genre_dic


def get_date_ordered(file_name):
    games_dict = {}
    for game in file_filtering(file_name):
        games_dict[game[0]] = int(game[2])
    ordered_by_dates = [item[0] for item in sorted(games_dict.items(), key=lambda kv: (-kv[1], kv[0]))]
    return ordered_by_dates

# Report functions
