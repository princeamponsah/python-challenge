# import modules / dependencies
import csv
import os

# identify path for input date 
pybank_file_input = os.path.join("PyBank","budget_data.csv")
pybank_file_output = os.path.join("PyBank","Analysis.txt")

# Create a list variables
months = [] # to capture the count of months from loop
change_pro_loss = [] # to hold the month to month change from the loop

# defining variables with their initial values
total_monthCount = 0
totalProfLoss = 0
curr_monthProfLoss = 0
prev_monthProfLoss = 0

# Read in the csv file
with open(pybank_file_input) as csvFile:
    reader = csv.reader(csvFile, delimiter=",")

    # identify that the file has a header
    header = next(csvFile)
    # print(f"Header:  {header}")

    # loop through the rows
    for rows in reader:
        # print(rows[0],rows[1])

        # calculate total month count - counting each line in dataset
        total_monthCount = total_monthCount + 1

        #total profit/loss - interate through from the loop and add each value
        curr_monthProfLoss = int(rows[1])
        totalProfLoss += float(rows[1])

        if (total_monthCount == 1):
            # make the value of prev month match current month
            prev_monthProfLoss = curr_monthProfLoss
        else:
            # calculate change in profit/loss
            profLoss_change = curr_monthProfLoss - prev_monthProfLoss

            # add the value to month list
            months.append(rows[0])

            # add the calculated prof/loss change to its intended list
            change_pro_loss.append(profLoss_change)

            # reset loop with current month equal to previous month
            prev_monthProfLoss = curr_monthProfLoss

# calculate the average change by adding values in change list and dividing by count
total_value = sum(change_pro_loss) # add up values in the list
avg_change = round((total_value/(total_monthCount-1)),2)

# Maximum change and minimum change calculation
max_change = max(change_pro_loss)
min_change = min(change_pro_loss)

# locate max and min change index. return value of index as best month/worst month
max_month_index = change_pro_loss.index(max_change)
min_month_index = change_pro_loss.index(min_change)
max_month = months[max_month_index]
min_month = months[min_month_index]

# Create Summary table
financial_output = (
    f"Financial Analysis\n"
    f"-------------------------------------\n"
    f"Total Months: {total_monthCount}\n"
    f"Total: ${totalProfLoss}\n"
    f"Average Change: ${avg_change}\n"
    f"Greatest Increase in Profit: {max_month} ${max_change}\n"
    f"Greatest Decrease in Profit: {min_month} ${min_change} "

)

print(financial_output)

# locate path to where to output final results
analysis_file = os.path.join("PyBank","Analysis.txt")

# push output of financial analysis to output file in location
with open(analysis_file, "w") as final_output:
    final_output.write(financial_output)