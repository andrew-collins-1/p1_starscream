import pandas as pd
import git
import seaborn as sns

repo = git.Repo('.', search_parent_directories=True)
wthr_path = repo.working_tree_dir + '\Data\MET Office Weather Data.csv'
sttn_path = repo.working_tree_dir + '\Data\MET Office Station Data.csv'

# column defs
# year: Year in which the measurements were taken
# month: Month in which the measurements were taken
# tmax: Mean daily maximum temperature (°C)
# tmin: Mean daily minimum temperature (°C)
# af: Days of air frost recorded that month (days)
# rain: Total rainfall (mm)
# sun: Total sunshine duration (hours)
# station: Station location where measurement was recorded

df_wthr = pd.read_csv(wthr_path)
df_wthr.drop(columns=['af'])
df_wthr = df_wthr.rename(columns={"tmax":"temp_max","tmin":"temp_min","sun":"hours_of_sunshine"})
#print(df_wthr.columns)

df_sttn = pd.read_csv(sttn_path)

print(df_wthr['station'].drop_duplicates())
print(df_sttn['Station name'].drop_duplicates())