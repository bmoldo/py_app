import pandas as pd
import glob

path = 'https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports/'
all_files = glob.glob(path + "/*.csv")

all_files

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)
    
df = pd.concat(li, axis=0, ignore_index=True)
df
