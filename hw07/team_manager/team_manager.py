from team import Team
from bench import Bench


def main():
    print("Welcome to the team manager.")
    the_team = Team()
    the_bench = Bench()

    while True:
        # Immediately converting the input to lower() lets the user enter
        # any kind of capitalization, so it's a little less strict.
        command = (input("What do you want to do?\n")).lower()

        if command == "done":
            print("Shutting down team manager\n")
            return  # this return statement exits main, ending the session.
        elif command == "set team name":
            do_set_team_name(the_team)
        elif command == "show roster":
            do_show_team_roster(the_team)
        elif command == "add player":
            do_add_player_to_team(the_team)
        elif command == "check position is filled":
            do_check_position_filled(the_team)
        elif command == "send player to bench":
            do_send_player_to_bench(the_team, the_bench)
        elif command == "get player from bench":
            do_get_player_from_bench(the_bench)
        elif command == "cut player":
            do_cut_player(the_team, the_bench)
        elif command == "show bench":
            do_show_bench(the_bench)
        else:
            do_not_understand()


def do_set_team_name(team):
    name = input("What do you want to name the team?\n")
    team.set_team_name(name)


def do_show_team_roster(team):
    # call the method on the team object that
    # displays the roster
    print("The lineup for", team.name, "is:")
    team.show_roster()


def do_check_position_filled(team):
    # call the method on the team object that determines
    # whether a given position has at least one player filling it
    position = input("What position are you checking for?\n").lower()
    team.is_position_filled(position)


def do_add_player_to_team(team):
    # Call the method on team that creates a new player and
    # adds the player to the team.
    player_name = input("What's the player's name?\n").lower()
    # enforce well-formed input
    if player_name.isalpha():
        player_number = input("What's " + player_name + "'s number?\n").lower()
        if player_number.isnumeric():
            player_position = input(
                "What's " + player_name + "'s position?\n").lower()
        else:
            return
    else:
        return
    team.add_player(player_name, player_number, player_position)
    print("Added", player_name, "to", team.name)


def do_send_player_to_bench(team, bench):
    name = input("Who do you want to send to the bench?\n").lower()
    bench.send_to_bench(name, team)
    # TODO: make sure that the player is actually on the team first,
    # and then call a method on the bench object to place the player
    # "on the bench". If this is accomplished successfully, print
    # "Sent", name, "to bench."
    # otherwise print
    # name, "isn't on the team."


def do_get_player_from_bench(bench):
    # get the best-rested player by name from the bench
    if len(bench.bench) >= 1:
        print("Got", bench.bench[0].player_name, "from bench")
        bench.get_from_bench()
    else:
        print("The beach is empty.")


def do_cut_player(team, bench):
    # cut player(Note:the player being cut should not be player
    # already on the bench)
    name = input("Who do you want to cut?\n").lower()
    for i in team.players:
        if i.player_name == name:
            for j in bench.bench:
                if j.player_name == name:
                    print("You can not cut this player already on the bench")
                    return
            team.cut_player(name)


def do_show_bench(bench):
    # show the names of the players who are currently on the bench.
    print("The bench currently includes:")
    for i in bench.bench:
        print(i.player_name)


def do_not_understand():
    print("I didn't understand that command")


main()
