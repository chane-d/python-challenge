import os
import csv

csvpath = os.path.join('../Resources/budget_data.csv')

months = []
profit_revenue = []



with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader, None)

    for row in csvreader:
        months.append(row[0])
        profit_revenue.append(int(row[1]))

total_months = len(months)


greatest_increase = profit_revenue[0]
greatest_decrease = profit_revenue[0]
total_revenue = 0

for x in range(len(profit_revenue)):
    if profit_revenue[x] >= greatest_increase:
        greatest_increase = profit_revenue[x]
        greatest_increase_month = months[x]
    elif profit_revenue[x] <= greatest_decrease:
        greatest_decrease = profit_revenue[x]
        greatest_decrease_month = months[x]
    total_revenue += profit_revenue[x]


average_change = round(total_revenue/total_months, 2)

print()
print("Financial Analysis")
print('----------------------')
print(f'Total Months {total_months}')
print(f'Average Change: $ + {average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')
print()



output_path = open('pybank_results_summary.txt', 'w')

output_path.write('Financial Analysis\n')
output_path.write('------------------------\n')
output_path.write(f'Total Months: {total_months}\n')
output_path.write(f'Total Revenue: {total_revenue}\n')
output_path.write(f'Average Change: {average_change}\n')
output_path.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n')
output_path.write(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n')
output_path.write('')
output_path.close

