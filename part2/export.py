from reports import *


def export(file_name, output_file):

    function_list = [get_most_played(file_name),
                     sum_sold(file_name),
                     get_selling_avg(file_name),
                     count_longest_title(file_name),
                     get_date_avg(file_name),
                     get_game(file_name, "Half-Life 2")]

    path = "/home/janos/codecool/python/3SI/pbwp-3rd-si-game-statistics-JanosCsjernyik/part2/" + output_file
    with open(output_file, "w") as txt:
        for line in function_list:
            txt.write(str(line)+"\n")

export("game_stat.txt", "exportfile.txt")
# Export functions
