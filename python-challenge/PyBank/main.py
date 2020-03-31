import os
import csv

file_path = os.path.join('..', 'budget_data.csv')
lines = []
budget = 0
changes_list = []
changes_total = 0

greatest_increase = ['Month', 0]
greatest_decrease = ['Month', 0]

with open(file_path) as budget_file:
	budget_reader = csv.reader(budget_file, delimiter = ",")
	line_counter = 0
	for budget_line in budget_reader:
		if line_counter > 0:
			lines.append(budget_line)
			budget += int(budget_line[1]) #total budget
		line_counter+=1
print(f'Financial Anaylsis')
print(f'----------------------')
print(f'Total Months: {len(lines)}')
print(f'Total: ${budget}')

#changes
for month in range(len(lines)):
	if month > 0:
		changes_list.append(int(lines[month][1]) - int(lines[month-1][1]))
		changes_total += changes_list[month-1]

		if changes_list[month-1] < greatest_decrease[1]:
			greatest_decrease = [lines[month][0], changes_list[month-1]]
		elif changes_list[month-1] > greatest_increase[1]:
			greatest_increase = [lines[month][0], changes_list[month-1]]
print(f'Average Change: ${changes_total/len(changes_list)}')
print(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})')
print(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})')




budget_report = open("../pybank_report.txt", "w")
budget_report.write(f'Financial Anaylsis\n')
budget_report.write(f'----------------------\n')
budget_report.write(f'Total Months: {len(lines)}\n')
budget_report.write(f'Total: ${budget}\n')
budget_report.write(f'Average Change: ${changes_total/len(changes_list)}\n')
budget_report.write(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n')
budget_report.write(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n')
budget_report.close()

