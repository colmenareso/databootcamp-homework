# Set up dependencies

import pandas as pd
import os as os

# Import the raw data into a DataFrame

csvpath = ("Resources/budget_data.csv")
data_bank_pd = pd.read_csv(csvpath, parse_dates=True)

# Initialize values for counters and variables

# Variable to be used to calculate total sum of Profit/Losses
total_value = 0

# Variable to use in for loop to calculate highest monthly change
max_increase = 0

# Variable to use in for loop to determine month and year of the maximum monthly change
max_date = 0

# Variable to use in for loop to calculate lowest monthly change
max_decrease = 0

# Variable to use in for loop to determine month and year of the lowest monthly change
min_date = 0

# Calculating total number of months reported

month_number =  sum(1 for row in data_bank_pd["Date"])

# Calculating sum of al profit/losses by looping in all rows of the Profit/Losses column

for index, row in data_bank_pd.iterrows():
    total_value += row['Profit/Losses']
    
# Creating a list that will include the monthly differences of Profit/Loses

change_list=[]

# For loop to calculate the difference between two consecutive months

previous_value = data_bank_pd['Profit/Losses'].loc[0]
for index, row in data_bank_pd.iterrows():
        change_list.append(row['Profit/Losses']-previous_value)
        previous_value = row['Profit/Losses']

        
# Adding the total of the monthly changes

total_change = sum(change_list)

# Calculating number of values in the lists (adjusted with -1 to remove 0 in the first month value in the list)

count_change = data_bank_pd['Profit/Losses'].count()-1

# Calculating the average of the monthly changes
    
average_change = round(total_change/count_change,2)

# Inserting change list values in the file for final output

data_bank_pd.insert(2, "Change", change_list)

# For loop to calculate the highest and the lowest monthly changes and the resspective month/year values

previous_value = data_bank_pd['Profit/Losses'].loc[0]
for index, row in data_bank_pd.iterrows():
    if row['Profit/Losses']-previous_value > max_increase:
        max_increase = row['Profit/Losses']-previous_value
        max_date = row['Date']
    if row['Profit/Losses']-previous_value < max_decrease:
        max_decrease = row['Profit/Losses']-previous_value
        min_date = row['Date']
    total_change += row['Profit/Losses']
    previous_value = row['Profit/Losses']


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

# Writing output text file with financial analysis summary

file_to_output = os.path.join("Output", "Financial_Analysis_v1.txt")

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

# Writing output file with added column showing monthly changes (Budget_Data_Analysis_v1.csv)

data_bank_pd.to_csv("Output/Budget_Data_Analysis_v1.csv", index=False, header=True)
