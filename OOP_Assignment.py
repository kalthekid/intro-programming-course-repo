class Players:
    def __init__(self, playerName, playerPosition):
        self.playerName = playerName
        self.playerPosition = playerPosition

    def __str__(self):
        return f"{self.playerName} ({self.playerPosition})"


class NFLTeam:
    def __init__(self, teamName, playerList):
        self.teamName = teamName
        self.playerList = playerList

    def display_roster(self):
        print(f"Team: {self.teamName}")
        print("Players:")
        for player in self.playerList:
            print(f"  - {player}")


# Create Player objects
p1 = Players("Joe Montana", "QB")
p2 = Players("Barry Sanders", "RB")
p3 = Players("Jerry Rice", "WR")
p4 = Players("Graham Gano", "K")

# Add players to playerList
playerList = [p1, p2, p3, p4]

# Create NFLTeam object
team = NFLTeam("Smashmouth Football", playerList)

# Output team name and players
team.display_roster()