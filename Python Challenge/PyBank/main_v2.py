# Setting dependencies

import pandas as pd
import os as os

# Reading csv file

csvpath = ("Resources/budget_data.csv")

data_bank_pd = pd.read_csv(csvpath, parse_dates=True)
new_data_bank_pd = pd.DataFrame(data_bank_pd)

# Calculating monthly differences

Change = new_data_bank_pd["Profit/Losses"].diff()

# adding new column (Change) to the dataframe

new_data_bank_pd.insert(2, "Change", Change) 

# Total number of months in the file
month_number =  sum(1 for row in new_data_bank_pd["Date"])

# Total of profit/loses

total_value = new_data_bank_pd["Profit/Losses"].sum()

# Average of monthly changes

average_change = round(new_data_bank_pd["Change"].mean(),2)

# Maximum increase of monthly changes

max_increase = int(new_data_bank_pd["Change"].max())

# Maximum decrease of monthly changes

max_decrease = int(new_data_bank_pd["Change"].min())

# Getting the date (month and year) for maximum increase

max_date = new_data_bank_pd.loc[new_data_bank_pd["Change"] == max_increase, "Date"].iloc[0]

# Getting the date (month and year) for maximum decrease

min_date = new_data_bank_pd.loc[new_data_bank_pd["Change"] == max_decrease]["Date"].iloc[0]

# Printing terminal 
output = (
f"Financial Analysis\n"
f"---------------------------------\n"
f"Total Months: {month_number}\n"
f"Total: ${total_value}\n"
f"Average change: ${average_change}\n"
f"Greatest Increase in Profits: {max_date} (${max_increase})\n"
f"Greatest Decrease in Profits: {min_date} (${max_decrease})\n"
f"```\n"
)
print(output)

# Writing output text file with finacial analysis summary

file_to_output = os.path.join("Output", "Financial_Analysis_v2.txt")

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)


# Writing output file - Budget_Data_Analysis_v2.csv with blank value for the first month monthly change

new_data_bank_pd.to_csv("Output/Budget_Data_Analysis_v2.csv", index=False, header=True)