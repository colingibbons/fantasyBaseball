import pybaseball as pb
import pandas as pd
from pybaseball.lahman import people
from pybaseball.analysis.projections.marcels import MarcelProjectionsBatting, MarcelProjectionsPitching
from calculate import pitcherValue, hitterValue

# list of stats to extract for each category of player
hitterCols = ['SINGLES', 'DOUBLES', 'TRIPLES', 'HR', 'R', 'RBI', 'BB', 'SO', 'HBP', 'SB', 'CS']
pitcherCols = ['W', 'L', 'SV', 'BS', 'IP', 'H', 'ER', 'BB', 'HBP', 'SO', 'WAR']

# fetch player names to display them instead of playing IDs
ppl = people()
ppl['Player'] = ppl['nameFirst'].str.cat(ppl['nameLast'], ' ')

# initialize the Marcel Projections objects
marcelBatting = MarcelProjectionsBatting()
marcelPitching = MarcelProjectionsPitching()

# generate projections for next season
batProj = marcelBatting.projections(2023)
pitchProj = marcelPitching.projections(2023)

pitchProj = pd.merge(ppl[['playerID', 'Player']], pitchProj, on='playerID', how='right')
batProj = pd.merge(ppl[['playerID', 'Player']], batProj, on='playerID', how='right')

# get player stats from last season
lastYearHitters = pb.batting_stats(2022, position='ALL', stat_columns=hitterCols)
lastYearPitchers = pb.pitching_stats(2022, stat_columns=pitcherCols)

# extract 2022 hitter data
hitterVals = lastYearHitters.values
hitterStatLabels = lastYearHitters.axes[1]
pitcherVals = lastYearPitchers.values
pitcherStatLabels = lastYearPitchers.axes[1]

# calculates the projected fantasy baseball value of each position player based on
# the Marcel the Monkey forecasting system, and stores all results in a list
projHitterValues = [(player[1], hitterValue(player)) for _, player in batProj.iterrows()]

# performs the same projection calculation as above, but this time for pitchers
projPitcherValues =  [(player[1], pitcherValue(player)) for _, player in pitchProj.iterrows()]

# # get the fantasy value of each qualified hitter in the league
# for player in hitterVals:
#     playerValue = hitterValue(player, statList=hitterStatLabels)
#     print(f'{player[2]} was worth {playerValue} fantasy points during the 2022 season.')
#
# for player in pitcherVals:
#     playerValue = pitcherValue(player, statList=hitterStatLabels)
#     print(f'{player[2]} was worth {playerValue} fantasy points during the 2022 season.')



