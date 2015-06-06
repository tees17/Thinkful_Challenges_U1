import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''
data = data.splitlines()
data = [i.split(', ') for i in data]
column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)


alMean= df['Alcohol'].mean()
alMean=str(alMean)
print ("Alcohol mean is " + alMean)

alMedian = df['Alcohol'].median()
alMedian=str(alMedian)
print ("Alcohol median is " +alMedian)

alMode = stats.mode(df['Alcohol'])
alMode=str(alMode)
print ("Alcohol mode is " + alMode)

alRange= max(df['Alcohol']) - min(df['Alcohol'])
alRange=str(alRange)
print ("Alcohol range is " + alRange)

alSD= df['Alcohol'].std() 
alSD=str(alSD)
print("Alcohol standard deviation is " + alSD )

alVar= df['Alcohol'].var() 
alVar=str(alVar)
print("Alcohol variance is " +alVar)

TobMean= df['Tobacco'].mean()
TobMean=str(TobMean)
print ("Tobacco mean is " + TobMean)

TobMedian= df['Tobacco'].median()
TobMedian=str(TobMedian)
print ("Tobacco median is " + TobMedian)

TobMode= stats.mode(df['Tobacco'])
TobMode=str(TobMode)
print ("Tobacco mode is " + TobMode)

TobRange= max(df['Tobacco']) - min(df['Tobacco'])
TobRange=str(TobRange)
print ("Tobacco range is " + TobRange)

TobSD= df['Tobacco'].std()
TobSD=str(TobSD)
print ("Tobacco standard deviation is " + TobSD)

TobVar= df['Tobacco'].var()
TobVar=str(TobVar)
print ("Tobacco variance is " + TobVar)


