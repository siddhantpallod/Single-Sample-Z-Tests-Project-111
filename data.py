import statistics
import plotly.graph_objects as pg
import plotly.figure_factory as pf
import pandas as pd
import random

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()

populationMean = statistics.mean(data)
print("Population Mean ", populationMean)

def randomSetOfMeans(counter):
    dataSet = []
    
    for i in range(0,counter):
        randomIndex = random.randint(0, len(data) - 1)
        value = data[randomIndex]
        dataSet.append(value)

    mean = statistics.mean(dataSet)
    return mean

meanList = []

for i in range(0, 100):
    setOfMeans = randomSetOfMeans(30)
    meanList.append(setOfMeans)

std = statistics.stdev(meanList)
mean = statistics.mean(meanList)
print("Sample Mean ", mean)

firstStdStart, firstStdEnd = mean - std, mean + std
secondStdStart, secondStdEnd =  mean - 2 * std,  mean + 2 * std
thirdStdStart, thirdStdEnd = mean - 3 * std, mean + 3 * std


fig = pf.create_distplot([meanList], ["Population"], show_hist = False)
fig.add_trace(pg.Scatter( x = [populationMean, populationMean], y = [0, 0.15], mode = 'lines', name = 'Population Mean'))
fig.add_trace(pg.Scatter( x = [firstStdStart, firstStdStart], y = [0,0.15], mode = 'lines', name = 'Std 1 Start'))
fig.add_trace(pg.Scatter( x = [firstStdEnd, firstStdEnd], y = [0,0.15], mode = 'lines', name = 'Std 1 End'))
fig.add_trace(pg.Scatter( x = [secondStdStart, secondStdStart], y = [0,0.15], mode = 'lines', name = 'Std 2 Start'))
fig.add_trace(pg.Scatter( x = [secondStdEnd, secondStdEnd], y = [0,0.15], mode = 'lines', name = 'Std 2 End'))
fig.add_trace(pg.Scatter( x = [thirdStdStart, thirdStdStart], y = [0,0.15], mode = 'lines', name = 'Std 3 Start'))
fig.add_trace(pg.Scatter( x = [thirdStdEnd, thirdStdEnd], y = [0,0.15], mode = 'lines', name = 'Std 3 End'))
fig.add_trace(pg.Scatter( x = [mean, mean], y = [0,0.15], mode = 'lines', name = 'Sample Mean'))
fig.show()

zScore = (mean - populationMean) / std
print("ZScore is ", zScore)