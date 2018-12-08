import os
import csv

csvpath = os.path.join('../Resources/election_data.csv')


candidates = []
vote_counts = []
number_of_votes = 0



with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader, None)

    for row in csvreader:
        number_of_votes = number_of_votes + 1
        candidate = row[2]

        if candidate in candidates:
            candidate_count = candidates.index(candidate)
            vote_counts[candidate_count] = vote_counts[candidate_count] + 1
        else:
            candidates.append(candidate)
            vote_counts.append(1)



percentage_of_votes = []
max_votes = vote_counts[0]
max_index = 0


for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/number_of_votes*100
    percentage_of_votes.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        max_index = count
    
    winner = candidates[max_index]


print('')
print('Election Results')
print('---------------------')
print(f'Total Votes: {number_of_votes}')
for count in range(len(candidates)):
    print(f'{candidates[count]}: {percentage_of_votes[count]}% ({vote_counts[count]})')
print('---------------------')
print(f'Winner: {winner}')
print('---------------------')


output_path = open('pypoll_results_summary.txt', 'w')

output_path.write('Election Results\n')
output_path.write('-----------------------\n')
output_path.write(f'Total Votes: {number_of_votes}\n')
for count in range(len(candidates)):
    output_path.write(f'{candidates[count]}: {percentage_of_votes[count]}% ({vote_counts[count]})\n')
output_path.write('---------------------\n')
output_path.write(f'Winner: {winner}\n')
output_path.write('---------------------\n')
output_path.write('')
output_path.close