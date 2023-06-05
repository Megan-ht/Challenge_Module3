# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# add our dependencies:
import csv
import os

# Assign a variable to load a file from a path:
file_to_load=os.path.join('Resources','election_results.csv')
# Assign a variable to save a file to a path:
file_to_save=os.path.join('analysis','election_analysis.txt')

# Initialize the total vote counter:
total_votes=0

# Candidate options and candidate votes:
candidate_options=[]
candidate_votes={}

# Create a county list and county votes dictionary:
county_names=[]
county_votes={}

# Track the winning candidate, vote count, and percentage:
winning_candidate=''
winning_count=0
winning_percentage=0

# Track the county with the largest voter turnout:
largest_county_turnout=''
largest_county_vote=0

# open the election_results.csv and read the file:
with open (file_to_load) as election_data:
    file_reader=csv.reader(election_data)

    # read the header:
    header=next(file_reader)

    # For each row in the csv file:
    for row in file_reader:

        # Add to total vote count:
        total_votes+=1

        # Get the candidate's name from each row:
        candidate_name=row[2]

        # Extract the county's name from each row:
        county_name=row[1]

        if candidate_name not in candidate_options:
            # If true, add candidate's name to the candidate list
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count
            candidate_votes[candidate_name]=0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name]+=1

        if county_name not in county_names:
            # If true, add the existing county to the list of counties:
            county_names.append(county_name)

            # And begin tracking the county's vote count:
            county_votes[county_name]=0

        # Add a vote to that county's vote count:
        county_votes[county_name]+=1

# Save the results to our text file:
with open (file_to_save,'w') as txt_file:

    election_results=(
        f'\nElection Results\n'
        f'-------------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'-------------------------\n\n'
        f'County Votes:\n')

    # print election_results to terminal:
    print(election_results, end="")

    # print election_results to text file:
    txt_file.write(election_results) 

    # Write a for loop to get the county from the county dictionary:
    for county in county_votes:
        # Retrieve the county vote count:
        county_vote=county_votes[county]
        # Calculate percentage of votes of the county:
        county_percentage=float(county_vote)/float(total_votes)*100

        county_results=(
            f'{county}: {county_percentage:.1f}% ({county_vote:,})\n')

        # Print the county results to terminal:
        print(county_results)

        # Save the county results to text file:
        txt_file.write(county_results)

        # Determine the largest turnout county:
        if (county_vote > largest_county_vote):
            largest_county_vote=county_vote
            largest_county_turnout=county
    
    largest_county_turnout=(
        f'\n-------------------------\n'
        f'Largest County Turnout: {largest_county_turnout}\n'
        f'-------------------------\n')

    # Print the county with the largest turnout to terminal:
    print(largest_county_turnout)

    # Print the county with the largest turnout to the text file:
    txt_file.write(largest_county_turnout)

    # Write a for loop to get the candidate's name from the candidate dictionary
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage
        votes=candidate_votes[candidate_name]
        vote_percentage=float(votes)/float(total_votes)*100
        
        candidate_results=(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

        # Print that candidate's voter count and percentage to the terminal
        print(candidate_results)

        # Save the candidate results to our text file
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count=votes
            winning_percentage=vote_percentage
            winning_candidate=candidate_name

    winning_candidate_summary=(
        f'-------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'-------------------------\n')

    # Print the winning candidate to terminal
    print(winning_candidate_summary)

    # Save the winning candidate's name to our text file
    txt_file.write(winning_candidate_summary)