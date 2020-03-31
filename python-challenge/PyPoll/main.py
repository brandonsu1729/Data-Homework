import os
import csv

file_path = os.path.join("..", "election_data.csv")
list_of_polls = []
election_results = {}
with open(file_path) as poll_file:
	poll_reader = csv.reader(poll_file, delimiter = ",")
	line_number = 0
	for line in poll_reader:
		if line_number > 0:
			list_of_polls.append(line)
			if line[2] not in election_results: #votes per candidate
				election_results[line[2]] = 1
			else:
				election_results[line[2]]+=1
		line_number += 1
total_votes = len(list_of_polls)

election_output = open('../election_report.txt', 'w')
print(f'Election Results')
election_output.write(f'Election Results\n')
print(f'-----------------------')
election_output.write(f'----------------\n')
print(f'Total Votes: {total_votes}')
election_output.write(f'Total Votes: {total_votes}\n')
print(f'-----------------------')
election_output.write(f'-----------------------\n')
for candidates in election_results:
	print(f'{candidates}: {round((election_results[candidates]/total_votes)*100, 3)}% ({election_results[candidates]})')
	election_output.write(f'{candidates}: {round((election_results[candidates]/total_votes)*100, 3)}% ({election_results[candidates]})\n')	
print(f'-----------------------')
election_output.write(f'-------------------\n')
print(f'Winner: {max(election_results, key = election_results.get)}')
election_output.write(f'Winner: {max(election_results, key = election_results.get)}\n')
election_output.close()