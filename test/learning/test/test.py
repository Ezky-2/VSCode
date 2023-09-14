from os import rename, path, walk
from re import findall

def find_in_list_with_regex (regex_patern, the_list):
    for each_item in the_list:
        if findall(regex_patern, each_item) != []: return each_item

def name_of_each_file (path_to_the_targeted_folder):
    directory_names, file_names = [], []

    for (dirpath, dirnames, filenames) in walk(path_to_the_targeted_folder):
        directory_names.extend(dirnames)
        file_names.extend(filenames)
        break

    return directory_names,file_names

def switch_names_with_numbers (path_to_the_targeted_folder):

    default_regex = r'.*%s.*?%s'

    for number_of_season in range(1,7):

        path_to_the_season_folder = path_to_the_targeted_folder + 'Season %s\\' % str(number_of_season)
        directory_names, file_names = name_of_each_file(path_to_the_season_folder)

        if len(str(number_of_season)) == 1: number_of_season = '0' + str(number_of_season)

        for each_episode in range(1, len(file_names) + 1):
            if len(str(each_episode)) == 1: each_episode = '0' + str(each_episode)

            matched_episode = find_in_list_with_regex(default_regex % (number_of_season, each_episode), file_names)
            file_names.remove(matched_episode)

            old_name = path.join(path_to_the_season_folder, matched_episode)
            print(matched_episode)
            new_name = path.join(path_to_the_season_folder, str(number_of_season) + str(each_episode) + '.' + findall(r'.*\.(.+)' , matched_episode)[0])

            rename(old_name , new_name)

        path_to_the_subs_folder = path_to_the_season_folder + directory_names[0] + '\\'
        tmp, file_names = name_of_each_file(path_to_the_subs_folder)

        for each_subtitle in range(1 , len(file_names) + 1):
            if len(str(each_subtitle)) == 1: each_subtitle = '0' + str(each_subtitle)

            matched_episode = find_in_list_with_regex(default_regex % (number_of_season, each_subtitle), file_names)
            file_names.remove(matched_episode)

            old_name = path.join(path_to_the_subs_folder, matched_episode)
            print(matched_episode)
            new_name = path.join(path_to_the_subs_folder, str(number_of_season) + str(each_subtitle) + '.' + findall(r'.*\.(.+)' , matched_episode)[0])

            rename(old_name , new_name)

# x = 'C:\\Users\\ezafa\\Downloads\\Video\\Lucifer\\'
# switch_names_with_numbers(x)
