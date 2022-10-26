def generate_by_death(ranking_by_death_dict):
    report_message = ""
    for index, match in enumerate(ranking_by_death_dict.values()):
        match_num = index + 1
        deaths = match["kills_by_means"]
        report_message += "\n--------------------------------------"
        report_message += f"\n Match: {match_num}"
        report_message += "\n Deaths By Mean:"
        for mean, death_quantity in deaths.items():
            report_message += f"\n    {mean}: {death_quantity}"
    return report_message

