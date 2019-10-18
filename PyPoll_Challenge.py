#Module 3 Challenge: Election Analysis
#Determine the number of votes cast from each county and the percentage of votes each county contributed to the election
#Use for loops and conditional statements to calculate the voter turnout for each county as well as each county's vote contribution percentage
#Then determine which county had the largest turnout
#Save results to election_results.txt

#Steps:
#1: Create a list for the counties
#2: Create a dicitonary where the county is the key and the votes cast for each county in the election are values
#3: Create an empty string that will hold the county name that hadt the largest turnout
#4: Declare a variable that represents the number of votes that a county received

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file
with open(file_to_load) as election_data:

	# Print the file object.
     print(election_data)


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World")