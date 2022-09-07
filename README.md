# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election. 

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes. 
3. Calculate the total number of votes each candidate received. 
4. Calculate the percentage of votes each candidate won. 
5. Determine the winner of the election based on popular vote. 

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
The analyis of the election show that:
- There are 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockholm
  - Diana DeGette
  - Raymon Anthony Doane
  
- The candidate results were:
  - Charles Casper Stockholm received 23% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Candidate 3 recieved 3.1% of the vote and 11,606 number of votes.
  
-The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes. 
  
<br>

## Overview of Election Audit

  * The purpose of this election audit analyis was to convert raw ballot data into clear election result subcategories: votes by candidate and votes by county. Additionally the analysis defined which precinct had the greatest voter turnout and who was the election winner based on number of popular votes received and the percentage of votes received. 

## Election Audit Results

  * There were 369,711 votes cast in the election. 
  * **Results by County:**
      * Jefferson county cast 10.5% of the total votes cast with 38,855 votes.
      * Denver county cast 82.8% of the total votes cast with 306,055 votes.
      * Arapahoe county cast 6.7% of the total votes cast with 24,801 votes. 
    **Denver county had the largest number of votes cast.**
  
  * **Results by Candidate:**
      * Charles Casper Stockholm received 23.0% of the total vote with 85,213 ballots cast.
      * Diana DeGettte received 73.8% of the total vote with 272,892 ballots cast. 
      * Raymon Anthony Doane received 3.1% of the total vote with 11,606 ballots cast. 

  * **Overall Winner**
      * With a total ballot count of 272,892 or 73.8% of the vote, Diana DeGette is the winner. 

*The below text file provides the overall summary as well as calculated by the analysis script:*

###### **Election Summary Text File**

![Screen_Shot_3](https://github.com/dpTuttle/Election_Analysis/blob/main/Resources/Screen_Shot_3.png)

## Election Audit Summary:
  * For the purposes of future elections, I believe this analyis script provides quick and efficient election results for precinct elections. With two modifications, I feel this may be effective for any election. First, adjusting the lists and dictionaries to add a 4th category: cities, would allow the code to drill down on election results in each county. Secondly, to process larger data sets, it would be useful to not use multiple "for..." statements and just use one "for.." statement with nested conditionals to save all categories (cities, counties, and candidates) to a single dictionary. This would dramatically reduce processing time and allow for state or even national election analysis with drill down. 
  
  
