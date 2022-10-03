# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
# to set the path
file_path =  os.path.join('./Resources/budget_data.csv')
output_path =  os.path.join('./results/budget_results.txt')
# to open and read csv file
with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        
       
        # to avoid counting header
        header= next(csvreader)

        # declare variables
        month_counter = []
        profit_losses =[]
        revenue_change =[]
        first= next(csvreader)
        month_counter.append(first[0])   
        profit_losses.append(int(first[1]))  
        first_pl =  int(first[1])



# calculate total months 
        for row in csvreader:
                month_counter.append(row[0])
             
      


        # The net total amount o "Profit/Losses" over the entire period
                profit_losses.append(int(row[1]))
                # total_profit = profit_losses+ int(row[1]) 
                # print(total_profit)

        #The changes in "Profit/Losses" over the entire period, and then the average of those changes
                change = int(row[1])- first_pl
                revenue_change.append (change)
                first_pl = int(row[1])
                # average_change = ({round(sum(revenue_change) / len(revenue_change),2)})
                # print(average_change)



        # the greatest increase and decrease in profit
        greatest_increase_profits = max(revenue_change)
        greatest_decrease_profits = min(revenue_change)

        increase_date = revenue_change.index(greatest_increase_profits)+1
        decrease_date = revenue_change.index(greatest_decrease_profits)+1
      
        max_date = month_counter [increase_date] 
        min_date = month_counter [decrease_date] 
        
        total_month = (len(month_counter))    
        # print(total_month)
        # print(sum(profit_losses))
        # print(round(sum(revenue_change) / len(revenue_change),2))
        # print(max_date, greatest_increase_profits)
        # print(min_date, greatest_decrease_profits)

        op = (f"Financial Analysis\n"
  f"----------------------------\n"
  f"Total Months: {total_month}\n"
  f"Total: ${(sum(profit_losses))}\n"
  f"Average Change: ${round(sum(revenue_change) / len(revenue_change),2)}\n"
  f"Greatest Increase in Profits: {max_date} (${greatest_increase_profits})\n"
  f"Greatest Decrease in Profits: {min_date} (${greatest_decrease_profits})\n")

        print(op)


with open(output_path, 'w') as textfile:
        textfile.write (op)
