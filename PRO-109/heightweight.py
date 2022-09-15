import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import csv
import pandas as pd


df = pd.read_csv("StudentsPerformance.csv")
hl = df["reading score"].to_list()
#wl = df["Weight(Pounds)"].to_list()
hmean = statistics.mean(hl)
#wmean = statistics.mean(wl)
hmode = statistics.mode(hl)
#wmode = statistics.mode(wl)
hmedian = statistics.median(hl)
#wmedian = statistics.median(wl)
hstnd = statistics.stdev(hl)
#wstnd = statistics.stdev(wl)

hfstrt,hfend = hmean-hstnd, hmean + hstnd 
hsstrt,hsend = hmean - (2*hstnd) , hmean + (2*hstnd)
htstrt,htend = hmean -(3*hstnd) , hmean + (3*hstnd)

###wsstrt,wsend = wmean - (2*wstnd) , wmean + (2*wstnd)
#tstrt,wtend = wmean -(3*wstnd) , wmean + (3*wstnd)

hdfsd = [result for result in hl if result > hfstrt and result < hfend]
hdssd = [result for result in hl if result > hsstrt and result < hsend]
hdtsd = [result for result in hl if result > htstrt and result < htend]

#wdfsd = [result for result in wl if result > wfstrt and result < wfend]
#wdssd = [result for result in wl if result > wsstrt and result < wsend]
#wdtsd = [result for result in wl if result > wtstrt and result < wtend]

print("{}% of data per height lies within firststd".format(len(hdfsd)*100.0/len(hl)))
print("{}% of data per height lies within secondstd".format(len(hdssd)*100.0/len(hl)))
print("{}% of data per height lies within thirdstd".format(len(hdtsd)*100.0/len(hl)))

print("{}% of data per weight lies within firststd".format(len(wdfsd)*100.0/len(wl)))
print("{}% of data per weight lies within secondstd".format(len(wdssd)*100.0/len(wl)))
print("{}% of data per weight lies within thirdstd".format(len(wdtsd)*100.0/len(wl)))

#Very tedious process