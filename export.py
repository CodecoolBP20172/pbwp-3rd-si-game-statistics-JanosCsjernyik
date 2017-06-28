from reports import *


def export(input_file, output_file):

    function_list = [count_games(input_file),
                     decide(input_file, 1998),
                     get_latest(input_file),
                     count_by_genre(input_file, "RPG"),
                     get_line_number_by_title(input_file, "Diablo III"),
                     sort_abc(input_file),
                     get_genres(input_file),
                     when_was_top_sold_fps(input_file)]

    path = "/home/janos/codecool/python/3SI/pbwp-3rd-si-game-statistics-JanosCsjernyik" + output_file
    with open(output_file, "w") as txt:
        for line in function_list:
            txt.write(str(line)+"\n")

export("game_stat.txt", "exportfile.txt")




