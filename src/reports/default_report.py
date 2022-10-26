def generate_default(ranking_dict):
    report_message = ""
    for index, match in enumerate(ranking_dict.values()):
        match_num = index + 1
        total_kills = match["total_kills"]
        players = match["players"]
        scores = match["kills"]
        report_message += "\n--------------------------------------"
        report_message += f"\n Match: {match_num}"
        report_message += f"\n Total Kills in Match: {total_kills}"
        report_message += "\n Players: "
        for player_index, player in enumerate(players):
            if player_index == len(players) - 1:
                report_message += f"{player}"
            else:
                report_message += f"{player}, "
        report_message += "\n Ranking:"
        for player, score in scores.items():
            report_message += f"\n    {player}: {score}"
    return report_message


class DefaultReport:
    # Method to generate the default report
    pass
