import numpy as np

### point values of each player outcome for the CMT baseball league ###
### "fluke" events such as no-hitters, perfect games, shutouts, and cycles have been omitted ###

# hitter points
hitterPointsDict = {
    "1B": 1,
    "2B": 2,
    "3B": 3,
    "HR": 4,
    "BB": 1,
    "CS": -1,
    "HBP": 1,
    "SO": -0.5,
    "R": 1,
    "RBI": 1,
    "SB": 1
}

# pitching points
pitcherPointsDict = {
    "BB": -1,
    "BS": -5,
    "ER": -1,
    "H": -1,
    "HBP": -1,
    "IP": 3,
    "K": 1,
    "L": -5,
    "W": 10,
    "SV": 10
}

### end of point value definitions ###

# function to calculate the full-season value of a pitcher
def pitcherValue(playerStats, statList=None):

    value = 0
    # loop through stats and use them to calculate the player's fantasy value
    if statList:
        for ind, stat in enumerate(statList):
            if stat in pitcherPointsDict:
                value += (pitcherPointsDict[stat] * playerStats[ind])

    return value

# function to calculate the full-season value of a hitter
def hitterValue(playerStats, statList=None):

    value = 0
    # loop through stats and use them to calculate the player's fantasy value
    if statList:
        for ind, stat in enumerate(statList):
            if stat in hitterPointsDict:
                value += (hitterPointsDict[stat] * playerStats[ind])
    else:
        stats = playerStats.keys()
        for ind, s in enumerate(stats):
            if s in hitterPointsDict:
                value += (hitterPointsDict[s] * playerStats[ind])

    return np.round(value)