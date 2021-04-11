# import the necessary modules/dependencies
import os
import csv

# identify path for input data
pypoll_file_input = os.path.join("PyPoll","election_data.csv")

# defining variables with their initial values
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
total_votes = 0

# read in the cvs file
with open(pypoll_file_input) as csvFile:
    reader = csv.reader(csvFile, delimiter=",")

    # identify that the file has a header
    header = next(csvFile)
    # print(f"Header:  {header}")

    # looping through the rows
    for row in reader:
        # print(rows[0],rows[1])

        # Calculate number of votes
        total_votes = total_votes + 1

        # if statement to capture votes for each candidate
        if row[2]=="Khan":
            khan_votes +=1 # increment Khal's variable by 1 
        elif row[2]=="Correy":
            correy_votes +=1 # increment Correy's variable by 1 
        elif row[2]=="Li":
            li_votes +=1 # increment Li's variable by 1 
        elif row[2]=="O'Tooley":
            otooley_votes +=1 # increment O'Tooley's variable by 1 


# calculate the vote count percentages for each candidate
vote_per_Khan = round((khan_votes/total_votes)*100 ,2)
vote_per_correy = round((correy_votes/total_votes)*100 ,2)
vote_per_li = round((li_votes/total_votes)*100 ,2)
vote_per_otooley = round((otooley_votes/total_votes)*100 ,2)

# create list variables 
# 1. to store candidates
# 2. to store votes to each candidate
candidates = ["Khan","Correy","Li","O'Tooley"]
num_of_votes = [khan_votes,correy_votes,li_votes,otooley_votes]

# zip together the above lists into data table
find_winner = dict(zip(candidates,num_of_votes))
# print(find_winner) # 

# create a variable and assign to it the winning identifier
the_winner = max(find_winner, key=find_winner.get)

# within election output - syntax for what the final output will look like
election_output = (
    f"Election Results\n"
    f"-------------------------------------\n"
    f"Total Votes : {total_votes}\n"
    f"-------------------------------------\n"
    f"Khan: {vote_per_Khan}% {khan_votes}\n"
    f"Correy: {vote_per_correy}% {correy_votes}\n"
    f"Li: {vote_per_li}% {li_votes}\n"
    f"O'Tooley: {vote_per_otooley}% {otooley_votes}\n"
    f"-------------------------------------\n"
    f"Winner: {the_winner} \n"
    f"-------------------------------------\n"
    

)

# print election output
print(election_output)

# locate path to where to output final results
analysis_file = os.path.join("PyPoll","Analysis.txt")

# push output of financial analysis to output file in location
with open(analysis_file, "w") as final_output:
    final_output.write(election_output)