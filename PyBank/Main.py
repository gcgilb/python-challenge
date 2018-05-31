import pandas as pd
import csv
import numpy as nb

#import CSV file

budget = "budget_data_1.csv"

budget_df = pd.read_csv(budget)

budget_df.head()

#Total Months
Total = "Total Months: " + str(len(budget_df))


#total sum
total_sum = budget_df["Revenue"].sum()

Total_sum = "Total Revenue: $" + str(total_sum)



#add change column
Change = budget_df["Revenue"] - budget_df["Revenue"].shift(-1)

budget_df = budget_df.assign(Change=Change.values)

#max value

max_change = budget_df.loc[budget_df["Change"].idxmax()]
 
Date = max_change["Date"]
Change = max_change["Change"]
x = int(Change)

max_value = "Greatest Increase in Revenue: " + str(Date) + " ($" + str(x) + ")"

#min Value

min_change = budget_df.loc[budget_df["Change"].idxmin()]
 
Date = min_change["Date"]
Change = min_change["Change"]
x = int(Change)

min_value = "Greatest Decrease in Revenue: " + str(Date) + " ($" + str(x) + ")"


#Average Value

avg = budget_df["Change"].mean()

avg = int(avg)

out = "Average Revenue Change: $" + str(avg)


print ("Financial Analysis") 
print ("---------------------------------------------------")
print (" ")
print (Total)
print (Total_sum)
print (max_value)
print (min_value)



