from src.reports.by_death_mean_report import generate_by_death
from src.reports.default_report import generate_default
from src.log_utils.read_log import LogReader

import_instance = LogReader()
filepath = input("filepath (default = python_test/data/input/qgames.log): ")
if not filepath:
    filepath = '../data/input/qgames.log'

file_log = import_instance.import_data(filepath)
joined_info_to_divide = import_instance.prepare_to_divide_by_match(file_log)
init_lines = joined_info_to_divide[0]
total_matches = joined_info_to_divide[1]
log_by_match = import_instance.divide_log_by_match(file_log, init_lines, total_matches)
ranking = import_instance.create_ranking_dict(log_by_match, total_matches)
import_instance.add_score_to_ranking(ranking, log_by_match, total_matches)
ranking_by_death = import_instance.create_ranking_by_death_dict(log_by_match, total_matches)

def write_report():
    # write default report
    file = open('../data/output/default_report', 'w')
    file.write(ranking)
    file.close()

    # write by death mean report
    file = open('src/data/output/by_death_mean_report', 'w')
    file.write(ranking_by_death)
    file.close()


if __name__ == "__main__":
    print('Default report -----------------------------------------------')
    print(generate_default(ranking))
    print('End Default report -----------------------------------------------')
    print('By Death Mean report -----------------------------------------------')
    print(generate_by_death(ranking_by_death))
    print('End By Death Mean report -----------------------------------------------')
    write_report()
