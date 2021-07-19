import pandas as pd
import numpy as np
import sys as sys

df = pd.read_csv("./PyBank/Resources/budget_data.csv")

prof_loss = df['Profit/Losses']
sum_total = (prof_loss.sum()) #sum of profit/losses
month_total = int(len(df.index)) #length of index
diff_values = np.diff(prof_loss) #calculate differences between profit/loss values
avg_change = (sum(diff_values))/(month_total-1) #sum of differences/month total
pos_chg_index = np.argmax(diff_values, axis=0)+1 #index value of largest positive increase
pos_change = (df.iloc[pos_chg_index].values) #find value and month of largest positive increase
neg_chg_index = np.argmin(diff_values, axis=0)+1 #index value of largest negative increase
neg_change = (df.iloc[neg_chg_index].values) #find value and month of largest negative increase

print("----------------------------\nFINANCIAL ANALYSIS\n----------------------------")
print(f"Total Months: {month_total}")
print(f"Total: ${sum_total:,}")
print(f"Average Change: ${avg_change:,.2f}")
print(f"Greatest Increase in Profits:{pos_change}")
print(f"Greatest Decrease in Profits:{neg_change}\n----------------------------")

sys.stdout = open("./PyBank/Analysis/budget_data_analysis.txt", "w")
print("----------------------------\nFINANCIAL ANALYSIS\n----------------------------")
print(f"Total Months: {month_total}")
print(f"Total: ${sum_total:,}")
print(f"Average Change: ${avg_change:,.2f}")
print(f"Greatest Increase in Profits:{pos_change}")
print(f"Greatest Decrease in Profits:{neg_change}\n----------------------------")
sys.stdout.close()

