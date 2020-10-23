import constants
import copy
import sys


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


def show_menu():
    print("BASKETBALL TEAM STATS TOOL")
    print("\n---- MENU----\n")
    print("Here are your choices:")
    print("1) Display Team Stats")
    print("2) Quit")

    while True:
        try:
            choise = int(input("\nEnter an option > "))
            if choise == 1:
                show_teams()
                break
            elif choise == 2:
                print("\nThe program will close now.")
                raise SystemExit
            else:
                print("\nPlease select 1 or 2")
                continue
        except ValueError:
            print("\nplease enter a valid number")


def show_teams():

    print("\nWhich team stats would you like te see?\n")
    print("1) Panthers")
    print("2) Bandits")
    print("3) Warriors")

    while True:
        try:
            choise = int(input("\nEnter an option > "))
            if choise == 1:
                display_team(panthers, "Panthers")
                break
            elif choise == 2:
                display_team(bandits, "Bandits")
                break
            elif choise == 3:
                display_team(warriors, "Warriors")
                break
            else:
                print("\nPlease select a number between 1 and 3")
                continue
        except ValueError:
            print("\nplease enter a valid number")


def display_team(team, team_name):
    print("\nTeam: {}".format(team_name))
    print("-------------")
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
    print("\nPress ENTER to go back to the main menu, or enter 'Q' tp quit >")
    while True:
        choise = input()
        if choise == "":
            show_menu()
        elif choise.lower() == "q":
            print("\nThe program will close now.")
            raise SystemExit
        else:
            print("\nPlease press ENTER or enter 'q'")


def run_program():
    clean_data()
    balance_teams()
    show_menu()


if __name__ == "__main__":
    run_program()
