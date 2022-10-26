from src.reports.default_report import generate_default
import json
import pytest

with open("./mocks/default_ranking_dict.json", mode="r") as file:
    default_dict = json.loads(file.read())


def test__match_number():
    report = generate_default(default_dict)
    expected = " Match: 21"
    assert expected in report


def test_total_kills():
    report = generate_default(default_dict)
    expected = " Total Kills in Match: 131"
    assert expected in report


def test_players():
    report = generate_default(default_dict)
    expected = " Players: Assasinu Credi, Dono da Bola, Isgalamido, Mal, Oootsimo, Zeh"
    assert expected in report


def test_ranking():
    report = generate_default(default_dict)
    expected = "Ranking:\n    Mal: 6\n    Dono da Bola: 12\n    Assasinu Credi: 16\n    Isgalamido: 17\n    Zeh: 19\n    Oootsimo: 21"
    assert expected in report


def test_format():
    report = generate_default(default_dict)
    expected = """
--------------------------------------
 Match: 1
 Total Kills in Match: 0
 Players: Isgalamido
 Ranking:
    Isgalamido: 0
--------------------------------------
 Match: 2
 Total Kills in Match: 11
 Players: Dono da Bola, Isgalamido, Mocinha
 Ranking:
    Isgalamido: -7
    Dono da Bola: 0
    Mocinha: 0
--------------------------------------
 Match: 3
 Total Kills in Match: 4
 Players: Dono da Bola, Isgalamido, Mocinha, Zeh
 Ranking:
    Zeh: -2
    Dono da Bola: -1
    Mocinha: 0
    Isgalamido: 1
--------------------------------------
 Match: 4
 Total Kills in Match: 105
 Players: Assasinu Credi, Dono da Bola, Isgalamido, Zeh
 Ranking:
    Dono da Bola: 9
    Assasinu Credi: 12
    Isgalamido: 19
    Zeh: 20
--------------------------------------
 Match: 5
 Total Kills in Match: 14
 Players: Assasinu Credi, Dono da Bola, Isgalamido, Zeh
 Ranking:
    Assasinu Credi: -1
    Dono da Bola: 0
    Zeh: 1
    Isgalamido: 2
--------------------------------------
 Match: 6
 Total Kills in Match: 29
 Players: Assasinu Credi, Dono da Bola, Fasano Again, Isgalamido, Mal, Maluquinho, Oootsimo, UnnamedPlayer, Zeh
 Ranking:
    Fasano Again: 0
    Mal: 0
    Maluquinho: 0
    UnnamedPlayer: 0
    Assasinu Credi: 1
    Dono da Bola: 2
    Isgalamido: 3
    Zeh: 7
    Oootsimo: 8
--------------------------------------
 Match: 7
 Total Kills in Match: 130
 Players: Assasinu Credi, Chessus, Chessus!, Dono da Bola, Isgalamido, Mal, Oootsimo, Zeh
 Ranking:
    Mal: -3
    Chessus: 0
    Chessus!: 0
    Zeh: 8
    Dono da Bola: 10
    Isgalamido: 14
    Assasinu Credi: 19
    Oootsimo: 20
--------------------------------------
 Match: 8
 Total Kills in Match: 89
 Players: Assasinu Credi, Dono da Bola, Isgalamido, Mal, Oootsimo, Zeh
 Ranking:
    Mal: -3
    Dono da Bola: 1
    Assasinu Credi: 9
    Zeh: 12
    Oootsimo: 15
    Isgalamido: 20
--------------------------------------
 Match: 9
 Total Kills in Match: 67
 Players: Assasinu Credi, Chessus, Chessus!, Dono da Bola, Isgalamido, Mal, Oootsimo, Zeh
 Ranking:
    Chessus!: 0
    Dono da Bola: 1
    Isgalamido: 1
    Mal: 2
    Assasinu Credi: 7
    Chessus: 8
    Oootsimo: 8
    Zeh: 12
--------------------------------------
 Match: 10
 Total Kills in Match: 60
 Players: Assasinu Credi, Chessus, Dono da Bola, Isgalamido, Mal, Oootsimo, Zeh
 Ranking:
    Oootsimo: -1
    Mal: 1
    Assasinu Credi: 3
    Dono da Bola: 3
    Chessus: 5
    Isgalamido: 5
    Zeh: 7
--------------------------------------
 Match: 11
 Total Kills in Match: 20
 Players: Assasinu Credi, Chessus, Dono da Bola, Isgalamido, Mal, Oootsimo, UnnamedPlayer, Zeh
 Ranking:
    Assasinu Credi: -3
    Dono da Bola: -2
    Chessus: 0
    Mal: 0
    UnnamedPlayer: 0
    Zeh: 0
    Isgalamido: 4
    Oootsimo: 4
--------------------------------------
 Match: 12
 Total Kills in Match: 160
 Players: Assasinu Credi, Chessus, Dono da Bola, Isgalamido, Mal, Oootsimo, Zeh
 Ranking:
    Mal: -7
    Dono da Bola: 3
    Zeh: 11
    Chessus: 12
    Oootsimo: 12
    Assasinu Credi: 18
    Isgalamido: 24
--------------------------------------
 Match: 13
 Total Kills in Match: 6
 Players: Assasinu Credi, Chessus, Dono da Bola, Isgalamido, Mal, Oootsimo, Zeh
 Ranking:
    Dono da Bola: -1
    Isgalamido: -1
    Assasinu Credi: 0
    Chessus: 0
    Mal: 0
    Oootsimo: 1
    Zeh: 2
--------------------------------------
 Match: 14
 Total Kills in Match: 122
 Players: Assasinu Credi, Chessus, Dono da Bola, Isgalamido, Mal, Oootsimo, Zeh
 Ranking:
    Mal: -5
    Dono da Bola: 1
    Assasinu Credi: 3
    Zeh: 4
    Chessus: 7
    Oootsimo: 9
    Isgalamido: 22
--------------------------------------
 Match: 15
 Total Kills in Match: 3
 Players: Assasinu Credi, Dono da Bola, Fasano Again, Isgalamido, Oootsimo, Zeh
 Ranking:
    Zeh: -3
    Assasinu Credi: 0
    Dono da Bola: 0
    Fasano Again: 0
    Isgalamido: 0
    Oootsimo: 0
--------------------------------------
 Match: 16
 Total Kills in Match: 0
 Players: Assasinu Credi, Dono da Bola, Isgalamido, Oootsimo, Zeh
 Ranking:
    Assasinu Credi: 0
    Dono da Bola: 0
    Isgalamido: 0
    Oootsimo: 0
    Zeh: 0
--------------------------------------
 Match: 17
 Total Kills in Match: 13
 Players: Assasinu Credi, Dono da Bola, Isgalamido, Mal, Oootsimo, UnnamedPlayer, Zeh
 Ranking:
    Assasinu Credi: -3
    Dono da Bola: -2
    Mal: -1
    Isgalamido: 0
    Oootsimo: 0
    UnnamedPlayer: 0
    Zeh: 0
--------------------------------------
 Match: 18
 Total Kills in Match: 7
 Players: Assasinu Credi, Dono da Bola, Isgalamido, Mal, Oootsimo, Zeh
 Ranking:
    Dono da Bola: -1
    Mal: -1
    Oootsimo: 0
    Isgalamido: 1
    Assasinu Credi: 2
    Zeh: 2
--------------------------------------
 Match: 19
 Total Kills in Match: 95
 Players: Assasinu Credi, Dono da Bola, Isgalamido, Mal, Oootsimo, Zeh
 Ranking:
    Mal: 2
    Assasinu Credi: 8
    Oootsimo: 10
    Dono da Bola: 12
    Isgalamido: 13
    Zeh: 20
--------------------------------------
 Match: 20
 Total Kills in Match: 3
 Players: Assasinu Credi, Dono da Bola, Isgalamido, Mal, Oootsimo, Zeh
 Ranking:
    Assasinu Credi: 0
    Isgalamido: 0
    Mal: 0
    Zeh: 0
    Dono da Bola: 1
    Oootsimo: 1
--------------------------------------
 Match: 21
 Total Kills in Match: 131
 Players: Assasinu Credi, Dono da Bola, Isgalamido, Mal, Oootsimo, Zeh
 Ranking:
    Mal: 6
    Dono da Bola: 12
    Assasinu Credi: 16
    Isgalamido: 17
    Zeh: 19
    Oootsimo: 21"""
    assert expected == report
