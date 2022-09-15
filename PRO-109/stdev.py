import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

diceresult = []
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceresult.append(dice1+dice2)

mean = sum(diceresult)/len(diceresult)
stantdev = statistics.stdev(diceresult)
medi = statistics.median(diceresult)
mod = statistics.mode(diceresult)
#,b = 4,5
frststandrdstrt,frststndrdend = mean - stantdev , mean + stantdev
scndstndrdstrt,scndstndrdend = mean - (2*stantdev) , mean + (2*stantdev)
thrdstndrdstrt , thrdstndrdend = mean -  (3*stantdev) , mean + (3*stantdev)
fig = ff.create_distplot([diceresult],["results"] , show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "mean"))  
fig.add_trace(go.Scatter(x = [frststandrdstrt,frststandrdstrt],y = [0,0.17],mode = "lines",name = "FirstStandardDeviation"))
fig.add_trace(go.Scatter(x = [frststndrdend,frststndrdend],y = [0,0.17],mode = "lines",name = "Firststandarddeviation"))
fig.add_trace(go.Scatter(x = [scndstndrdstrt,scndstndrdstrt],y = [0,0.17],mode = "lines",name = "secondstandarddeviation"))
fig.add_trace(go.Scatter(x = [scndstndrdend,scndstndrdend],y = [0,0.17],mode = "lines",name = "secondstandarddevaiation"))
fig.add_trace(go.Scatter(x = [thrdstndrdstrt,thrdstndrdstrt],y = [0,0.17],mode = "lines",name = "thirdstandarddeviation"))
fig.add_trace(go.Scatter(x = [thrdstndrdend,thrdstndrdend],y = [0,0.17],mode = "lines",name = "thirdstandarddeviation"))

fig.show()

#print(a,b)