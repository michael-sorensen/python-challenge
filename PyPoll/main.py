import pandas as pd
import sys as sys
from statistics import mode

df = pd.read_csv("./PyPoll/Resources/election_data.csv")

candidate = df['Candidate']
vote_total = int(len(df.index))
cand_total = (df['Candidate'].value_counts())
cand_pct = (df['Candidate'].value_counts(normalize=True)).mul(100).round(0).astype(str) + '%'
winner = candidate.mode().values

print("----------------------------\nELECTION RESULTS\n----------------------------")
print(f"Total Votes: {vote_total}\n----------------------------")
print(f"Share of Total Vote by Candidate:\n{cand_pct.to_string()}\n----------------------------")
print(f"Total Vote by Candidate:\n{cand_total.to_string()}\n----------------------------")
print(f"Winner: {winner}\n----------------------------")

sys.stdout = open("./PyPoll/Analysis/election_data_analysis.txt", "w")
print("----------------------------\nELECTION RESULTS\n----------------------------")
print(f"Total Votes: {vote_total}\n----------------------------")
print(f"Share of Total Vote by Candidate:\n{cand_pct.to_string()}\n----------------------------")
print(f"Total Vote by Candidate:\n{cand_total.to_string()}\n----------------------------")
print(f"Winner: {winner}\n----------------------------")
sys.stdout.close()