# Python-challenge

The purpose of this python challenge is to get familiar using Python for data analysis.

In this challenge, there is analysis of a small data set (PyBank) and a large data set (PyPoll). 

The similarities in both is being able to read and iterate through a csv file and output the result to the termial and a new text file.

It is crucaial to use for loops and conditionals to process the data.

PyBank:

In pybank, it was essential to use the enumerate() function. This allowed us to keep track of the row that was iterated through and extract data. It also allowed us to keep track of the number that the row was on. This is important because one of the calculations necessary to perform was the change in value from row to row, which can only be done after the first iterable row. 

PyPoll:

In pypoll, dictionaries are a key method to producing the correct outcome. Without knowing how many candidates there are, we can add the names to the dictionary as we iterate through the csv file and tally the votes as a key:value pair. For each iterable, the dictionary is checked for the key. If the key is present, the value is increased by one. This dictionary can then be iterated through to perform calculations for the required output.
