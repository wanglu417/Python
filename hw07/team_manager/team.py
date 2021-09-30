from player import Player


class Team:
    """A class representing a dodgeball team"""

    def __init__(self):
        self.name = "Anonymous Team"
        self.players = []

    def set_team_name(self, name):
        # set the team name
        self.name = name

    def add_player(self, player_name, player_number, player_position):
        # call the Player class constructor"""
        self.players.append(
            Player(player_name, player_number, player_position))

    def cut_player(self, player_name):
        # Remove the player with the name player_name
        # from the players list
        for i in range(len(self.players)):
            if player_name == self.players[i].player_name:
                self.players.pop(i)
                return

    def is_position_filled(self, position):
        # checks whether there is currently at least one player
        # on the team occupying the requested position
        for i in range(0, len(self.players)):
            if position == self.players[i].player_position:
                print("Yes, the", position, "position is filled")
                return
        print("No, the", position, "position is not filled")

    def show_roster(self):
        # display (print to screen) the full team roster
        if self.players == []:
            print("The team currently has no players")
        else:
            for i in self.players:
                print(i.player_number+' '*8 +
                      i.player_name+' '*8 + i.player_position)
