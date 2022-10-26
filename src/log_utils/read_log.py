from collections import Counter
import operator
import re

init = "InitGame:"
client_conn = "ClientConnect:"
client_disconn = "ClientDisconnect:"
change_info = "ClientUserinfoChanged:"
kill = "Kill:"


# Method to import the log file and perform a filter to reduce
# the raw file to more important data for analysis
def import_data(path):
    if path[-3:] == 'log':
        with open(path, mode="r") as file:
            pattern = rf"{init}|{client_conn}|{client_disconn}|{change_info}|{kill}"
            filtered_log = []
            for line in file:
                if re.search(pattern, line) is not None:
                    filtered_log.append((line.rstrip('\n')))
            return filtered_log
    else:
        raise ValueError('Invalid file')


# Method to extract the range of the lines of each match
def prepare_to_divide_by_match(log):
    init_lines = list()
    total_matches = 0
    for line_index, line in enumerate(log):
        if (re.search(rf"{init}", line)) is not None:
            init_lines.append(line_index)
            total_matches += 1
    init_lines.append(len(log))
    return init_lines, total_matches


# Method to group log records by match | Creating a list of lists (array of arrays)
def divide_log_by_match(log, init_lines, total_matches):
    match_data_list = []
    for index in range(total_matches):
        match_data = []
        for l_index in range(init_lines[index] + 1, init_lines[index + 1]):
            match_data.append(log[l_index])
        match_data_list.append(match_data)
    return match_data_list


# Method to create a dictionary with the information of each match
# JSON similar format
def create_ranking_dict(log_by_match, total_matches):
    ranking = dict()
    match = dict()
    for index in range(total_matches):
        total_kills = 0
        players = list()
        for line_index, line in enumerate(log_by_match[index]):
            if (re.search(rf"{kill}", line)) is not None:
                total_kills += 1
            if (re.search(rf"{change_info}", line)) is not None:
                player = line.split("\\")[1]
                if player not in players:
                    players.append(player)
            if line_index == len(log_by_match[index]) - 1:
                players.sort(reverse=False)
                players_aux = players
                match = {
                    "total_kills": total_kills,
                    "players": players_aux,
                    "kills": {}
                }
        ranking.update({f"game_{index + 1}": match})
    return ranking


# Method to add each player's score for each round
def add_score_to_ranking(ranking, log_by_match, total_matches):
    ranking_aux = dict()
    for index in range(total_matches):
        ranking_aux.update({f"game_{index + 1}": {"kills": {}}})
        players = ranking[f"game_{index + 1}"]["players"]
        for player_index, player in enumerate(players):
            ranking_aux[f"game_{index + 1}"]["kills"][player] = 0
            score_count = 0
            for line in log_by_match[index]:
                kill_re = rf"^(?=.*{kill})(?=.*{player})"
                if re.search(kill_re, line) is not None:
                    if f"killed {player}" not in line:
                        ranking_aux[f"game_{index + 1}"]["kills"][player] += 1
                        score_count += 1
                    if "<world>" in line:
                        ranking_aux[f"game_{index + 1}"]["kills"][player] -= 1
                        score_count -= 1
            if player_index == len(players) - 1:
                ranking_sort = ranking_aux[f"game_{index + 1}"]["kills"]
                # https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
                # How sort a dictionaty in Python converting (key, value) in List of Tuples
                sorted_scores = sorted(ranking_sort.items(), key=operator.itemgetter(1))
                for score in sorted_scores:
                    ranking[f"game_{index + 1}"]["kills"][score[0]] = score[1]


# Method to create a dictionary with death means quantity information by rounds
def create_ranking_by_death_dict(log_by_match, total_matches):
    ranking_by_death = dict()
    for index in range(total_matches):
        death_types = list()
        for line in log_by_match[index]:
            if (re.search(rf"{kill}", line)) is not None:
                death_types.append(line.split("by ")[1])
        death_types_aux = death_types
        sort_death_types = dict(Counter(death_types_aux))
        sorted_death_types = sorted(sort_death_types.items(), key=operator.itemgetter(1))
        sorted_death_types.reverse()
        death_type_match = dict()
        for death_type in sorted_death_types:
            death_type_match.update({death_type[0]: death_type[1]})
        kills_by_mean_dict = {"kills_by_means": death_type_match}
        ranking_by_death.update({f"game-{index + 1}": kills_by_mean_dict})
    return ranking_by_death
