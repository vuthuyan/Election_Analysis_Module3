#from abc import abstractmethod
from typing import cast


#print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == 'Denver':
    print(counties[1])


candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")
print(message_to_candidate)
