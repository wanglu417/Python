from team import Team


class Bench:
    """A class representing a sidelines bench"""

    def __init__(self):
        """Initialize the bench object"""
        self.bench = []  # Initialize players on the bench an empty list

    def send_to_bench(self, player_name, team):
        # Put the player "onto the bench
        # Make sure that the player is actually on the team first,
        for i in team.players:
            if i.player_name == player_name:
                self.bench.append(i)  # Display players currently on the bench
                print("Sent", player_name, "to bench.")
                return
        # If the player is not on the team
        print(player_name, "isn't on the team.")

    def get_from_bench(self):
        # Return the name of the player who has been on the bench longest
        self.bench.pop(0)
