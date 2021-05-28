import os
import pandas as pd

def isConsolidating(df, percentage = 2):
    recentCandles = df[-5:]

    maxClose = recentCandles['Close'].max()
    minClose = recentCandles['Close'].min()

    threshold = 1 - percentage / 100
    if minClose > maxClose*threshold: # within 2%
        return True
    return False

def isBreakout(df, percentage = 2):

    if len(df) < 5:
        return False

    lastClose = df[-1:]['Close'].values[0]

    if isConsolidating(df[:-1],percentage = percentage):
        recentCandles = df[-16:-1]

        if lastClose > recentCandles['Close'].max():
            return True

    return False

for filename in os.listdir('datasets/daily'):
    df = pd.read_csv('datasets/daily/{}'.format(filename))

    # if isConsolidating(df,2.5):
    #     print("{} is consolidating".format(filename))

    # if len(df) > 5:
    #     print ("{} has close of {}".format(filename, df[-1:]['Close'].values))

    if isBreakout(df) : 
         print("{} is breaking out".format(filename))