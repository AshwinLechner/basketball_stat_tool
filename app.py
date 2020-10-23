import constants
import copy
import sys
import pdb


PLAYERS_COPY = copy.deepcopy(constants.PLAYERS)
panthers = []
bandits = []
warriors = []
all_teams = [panthers, bandits, warriors]


def clean_data():
    for player in PLAYERS_COPY:
        player["height"] = int(player["height"][slice(2)])
        if player["experience"] == "YES":
            player["experience"] = True
        else:
            player["experience"] = False


def balance_teams():
    num_players_team = len(PLAYERS_COPY) / len(all_teams)
    for team in all_teams:
        while len(team) < num_players_team:
            team.append(PLAYERS_COPY.pop())


def check_input():
    while True:
        try:
            user_input = int(input("Enter an option > "))
            break
        except ValueError:
            print("Please enter a valid number.\n ")
    return user_input


def show_menu():
    print("""BASKETBALL TEAM STATS TOOL

---- MENU----

Here are your choices:
1) Display Team Stats
2) Quit
""")
    while True:
        check_input()
        if check_input() == 1:
            show_teams()
            break
        elif check_input() == 2:
            print("The program will close now.")
            raise SystemExit
        else:
            print("Please select 1 or 2")
            continue


def show_teams():
    print("""
1) Panthers
2) Bandits
3) Warriors
""")
    while True:
        check_input()
        if check_input() == 1:
            display_team(panthers, "Panthers")
            break
        elif check_input() == 2:
            display_team(bandits, "Bandits")
            break
        elif check_input() == 3:
            display_team(warriors, "Warriors")
            break
        else:
            print("Please select a number between 1 and 3")
            continue


def display_team(team, team_name):
    print("\nTeam: {}".format(team_name))
    print("----------")
    print("total players: {}".format(len(team)))
    print("\nPlayers on team:")
    i = 0
    player_names = []
    while i < len(team):
        player_names.append(team[i]['name'])
        i += 1
    print(", ".join(player_names))
    show_end()


def show_end():
    while True:
        print("\nPress ENTER to go back to the main menu, or enter 'Q' tp quit")
        if input() == "":
            show_menu()
        elif input().lower() == "q":
            print("The program will close now.")
            raise SystemExit
        else:
            print("Please press ENTER or enter 'q'")


def start_program():
    clean_data()
    balance_teams()
    show_menu()


if __name__ == "__main__":
    start_program()
