Lab 1 - Enron Data Analysis
==========================

This is repo for the first lab in Gov 2430 (Fall 2013).

Setup
==========================

1. Download and unpack the "Metadata by Users - CSV files, one for each User" from [here](http://foreverdata.org/1009/index.html)
2. The .csv files need to live in the same directory as process.py

Usage
==========================
`./process.py` - spits out the top 30 most common words and create a file
`sortedCounts.txt` that contains a full, sorted list of all words

`./process.py FILENAME` - this will read in FILENAME (which contains words, one
per line) and spit out the top 10 users for each word

