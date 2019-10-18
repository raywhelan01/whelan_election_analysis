#Module 3 Challenge: Election Analysis
#Determine the number of votes cast from each county and the percentage of votes each county contributed to the election
#Use for loops and conditional statements to calculate the voter turnout for each county as well as each county's vote contribution percentage
#Then determine which county had the largest turnout
#Save results to election_results.txt

#Steps:
#1: Create a list for the counties -- Line 35
#2: Create a dicitonary where the county is the key and the votes cast for each county in the election are values -- Line 36
#3: Create an empty string that will hold the county name that hadt the largest turnout -- Line 44
#4: Declare a variable that represents the number of votes that a county received -- Lines 78-87
#5: Inside the with open() funtcion:
#	-Create three if statements to print voter turnout -- Line 123
#	-Add the results to the output file -- Line 168
#	-Print the results to the command line -- Line 165

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options list and candidate votes dictionary
candidate_options = []
candidate_votes = {}

# Counties list and county votes dictionary
counties = []
county_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the county with the largest turnout
largest_county = ""
largest_county_vote = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count.
        total_votes += 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate, add the name to the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # Get the county name from each row
        county_name = row[1]

        # If the county is not already recorded, add the name to the county list
        if county_name not in counties:

        	#Add the county to the county list
        	counties.append(county_name)

        	# Begin tracking that county's voter turnout
        	county_votes[county_name] = 0

        #Add a vote to that county's turnout
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #Process county vote data
    print("\nCounty Votes:")
    txt_file.write("\nCounty Votes:\n")

    for county in county_votes:

    	#Retrieve vote count and percentage
    	votes = county_votes[county]
    	vote_percentage = float(votes) / float(total_votes) * 100
    	county_results = (
    		f"{county}: {vote_percentage:.1f}% ({votes:,})\n")

    	# Print each county's voter turnout and percentage to the terminal
    	print(county_results)

    	# Save the county results to the text file
    	txt_file.write(county_results)

    	# Determine the largest county
    	if (votes > largest_county_vote):
    		largest_county_vote = votes
    		largest_county = county

    # Print the largest county to the terminal
    county_summary = (
    	f"\n-------------------------\n"
    	f"Largest County Turnout: {largest_county}\n"
    	f"-------------------------\n")
    print(county_summary)

    # Write the largest county to the terminal
    txt_file.write(county_summary)

    #Process candidate vote data
    for candidate in candidate_votes:

        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)