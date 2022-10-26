from src.reports.by_death_mean_report import generate_by_death
import json

with open("./mocks/by_death_ranking_dict.json", mode="r") as file:
    by_death_dict = json.loads(file.read())


def test_match_number():
    report = generate_by_death(by_death_dict)
    expected = " Match: 21"
    assert expected in report


def test_death_by_mean():
    report = generate_by_death(by_death_dict)
    expected = " Deaths By Mean:\n    MOD_ROCKET_SPLASH: 60\n    MOD_ROCKET: 37\n    MOD_TRIGGER_HURT: 14\n    MOD_RAILGUN: 9\n    MOD_SHOTGUN: 4\n    MOD_MACHINEGUN: 4\n    MOD_FALLING: 3"
    assert expected in report


def test_format():
    report = generate_by_death(by_death_dict)
    expected = """
--------------------------------------
 Match: 1
 Deaths By Mean:
--------------------------------------
 Match: 2
 Deaths By Mean:
    MOD_TRIGGER_HURT: 7
    MOD_ROCKET_SPLASH: 3
    MOD_FALLING: 1
--------------------------------------
 Match: 3
 Deaths By Mean:
    MOD_TRIGGER_HURT: 2
    MOD_FALLING: 1
    MOD_ROCKET: 1
--------------------------------------
 Match: 4
 Deaths By Mean:
    MOD_ROCKET_SPLASH: 51
    MOD_ROCKET: 20
    MOD_FALLING: 11
    MOD_TRIGGER_HURT: 9
    MOD_RAILGUN: 8
    MOD_MACHINEGUN: 4
    MOD_SHOTGUN: 2
--------------------------------------
 Match: 5
 Deaths By Mean:
    MOD_TRIGGER_HURT: 5
    MOD_ROCKET_SPLASH: 4
    MOD_ROCKET: 4
    MOD_RAILGUN: 1
--------------------------------------
 Match: 6
 Deaths By Mean:
    MOD_ROCKET_SPLASH: 13
    MOD_ROCKET: 5
    MOD_SHOTGUN: 4
    MOD_TRIGGER_HURT: 3
    MOD_RAILGUN: 2
    MOD_MACHINEGUN: 1
    MOD_FALLING: 1
--------------------------------------
 Match: 7
 Deaths By Mean:
    MOD_ROCKET_SPLASH: 49
    MOD_ROCKET: 29
    MOD_TRIGGER_HURT: 20
    MOD_MACHINEGUN: 9
    MOD_RAILGUN: 9
    MOD_SHOTGUN: 7
    MOD_FALLING: 7
--------------------------------------
 Match: 8
 Deaths By Mean:
    MOD_ROCKET_SPLASH: 39
    MOD_ROCKET: 18
    MOD_RAILGUN: 12
    MOD_TRIGGER_HURT: 9
    MOD_FALLING: 6
    MOD_MACHINEGUN: 4
    MOD_SHOTGUN: 1
--------------------------------------
 Match: 9
 Deaths By Mean:
    MOD_ROCKET_SPLASH: 25
    MOD_ROCKET: 17
    MOD_RAILGUN: 10
    MOD_TRIGGER_HURT: 8
    MOD_FALLING: 3
    MOD_MACHINEGUN: 3
    MOD_SHOTGUN: 1
--------------------------------------
 Match: 10
 Deaths By Mean:
    MOD_TELEFRAG: 25
    MOD_TRIGGER_HURT: 17
    MOD_RAILGUN: 7
    MOD_ROCKET: 4
    MOD_BFG: 2
    MOD_BFG_SPLASH: 2
    MOD_CRUSH: 1
    MOD_MACHINEGUN: 1
    MOD_ROCKET_SPLASH: 1
--------------------------------------
 Match: 11
 Deaths By Mean:
    MOD_TRIGGER_HURT: 7
    MOD_RAILGUN: 4
    MOD_ROCKET_SPLASH: 4
    MOD_BFG_SPLASH: 3
    MOD_MACHINEGUN: 1
    MOD_CRUSH: 1
--------------------------------------
 Match: 12
 Deaths By Mean:
    MOD_RAILGUN: 38
    MOD_TRIGGER_HURT: 37
    MOD_ROCKET_SPLASH: 35
    MOD_ROCKET: 25
    MOD_BFG: 8
    MOD_BFG_SPLASH: 8
    MOD_MACHINEGUN: 7
    MOD_FALLING: 2
--------------------------------------
 Match: 13
 Deaths By Mean:
    MOD_TRIGGER_HURT: 2
    MOD_BFG: 1
    MOD_BFG_SPLASH: 1
    MOD_ROCKET_SPLASH: 1
    MOD_ROCKET: 1
--------------------------------------
 Match: 14
 Deaths By Mean:
    MOD_TRIGGER_HURT: 31
    MOD_ROCKET_SPLASH: 24
    MOD_ROCKET: 23
    MOD_RAILGUN: 20
    MOD_BFG_SPLASH: 10
    MOD_BFG: 5
    MOD_FALLING: 5
    MOD_MACHINEGUN: 4
--------------------------------------
 Match: 15
 Deaths By Mean:
    MOD_TRIGGER_HURT: 3
--------------------------------------
 Match: 16
 Deaths By Mean:
--------------------------------------
 Match: 17
 Deaths By Mean:
    MOD_TRIGGER_HURT: 6
    MOD_FALLING: 3
    MOD_ROCKET_SPLASH: 2
    MOD_RAILGUN: 2
--------------------------------------
 Match: 18
 Deaths By Mean:
    MOD_ROCKET_SPLASH: 4
    MOD_TRIGGER_HURT: 1
    MOD_FALLING: 1
    MOD_ROCKET: 1
--------------------------------------
 Match: 19
 Deaths By Mean:
    MOD_ROCKET_SPLASH: 32
    MOD_ROCKET: 27
    MOD_TRIGGER_HURT: 12
    MOD_RAILGUN: 10
    MOD_MACHINEGUN: 7
    MOD_SHOTGUN: 6
    MOD_FALLING: 1
--------------------------------------
 Match: 20
 Deaths By Mean:
    MOD_ROCKET_SPLASH: 2
    MOD_ROCKET: 1
--------------------------------------
 Match: 21
 Deaths By Mean:
    MOD_ROCKET_SPLASH: 60
    MOD_ROCKET: 37
    MOD_TRIGGER_HURT: 14
    MOD_RAILGUN: 9
    MOD_SHOTGUN: 4
    MOD_MACHINEGUN: 4
    MOD_FALLING: 3"""
    assert expected == report
