import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
dfLap = pd.read_csv("LapTimes.csv")
dfRace = pd.read_csv("RaceResults.csv")
top_ten = dfRace[dfRace["Position"] <= 10]
top_ten_sorted = top_ten.sort_values(by="TeamName")
print(top_ten_sorted[["TeamName","Position","FullName","Location"]].head(10))
print(top_ten_sorted.groupby("TeamName").size().reset_index(name="Top 10 Count").to_string(index=False))
top_ten_sorted["Q1Seconds"] = pd.to_timedelta(top_ten_sorted["Q1"]).dt.total_seconds()
top_ten_sorted["Q2Seconds"] = pd.to_timedelta(top_ten_sorted["Q2"]).dt.total_seconds()
top_ten_sorted["Q3Seconds"] = pd.to_timedelta(top_ten_sorted["Q3"]).dt.total_seconds()
dfLap["PitOutTimeSeconds"] = pd.to_timedelta(dfLap["PitOutTime"]).dt.total_seconds()
dfLap["PitInTimeSeconds"] = pd.to_timedelta(dfLap["PitInTime"]).dt.total_seconds()
dfLap["Sector1TimeSeconds"] = pd.to_timedelta(dfLap["Sector1Time"]).dt.total_seconds()
dfLap["Sector2TimeSeconds"] = pd.to_timedelta(dfLap["Sector1Time"]).dt.total_seconds()
dfLap["Sector3TimeSeconds"] = pd.to_timedelta(dfLap["Sector1Time"]).dt.total_seconds()
dfLap["Sector1SessionTimeSeconds"] = pd.to_timedelta(dfLap["Sector1SessionTime"]).dt.total_seconds()
dfLap["Sector2SessionTimeSeconds"] = pd.to_timedelta(dfLap["Sector2SessionTime"]).dt.total_seconds()
dfLap["Sector3SessionTimeSeconds"] = pd.to_timedelta(dfLap["Sector3SessionTime"]).dt.total_seconds()
print(top_ten_sorted[["Q1Seconds","Q2Seconds","Q3Seconds"]])
print(dfLap[["PitOutTimeSeconds","PitInTimeSeconds","Sector1TimeSeconds","Sector2TimeSeconds","Sector3TimeSeconds","Sector1SessionTimeSeconds","Sector2SessionTimeSeconds","Sector3SessionTimeSeconds"]])