# **Viral Twitter**
This project aims to scrape and analyze **time stamped** twitter data focusing on hashtags to 
cross reference with COVID-19 data.

I hope to test whether COVID data demonstrates a correlation between the anti-mask, anti-lockdown
sentiments and the spreading of the coronavirus.

As of Jul 17th, I have finished the code for getting the data. The program outputs the data
collected with the rest of the original COVID data for easier comparison.

`Gather_Data.py` is the main file that completes this task. `Splitter.py` is the helper program that
split the COVID data into each county.

This program is likely not very efficient and may take a long time to run. Be advised to tune
up the sleep time on twint should Twitter block further accesses.

Since the program documents _daily_ twitter hashtags, it makes sense for the cases to also be
similarly altered.`Tweet_adder.py` does this by subtracting the previous day's total cases
from the cumulative count to get daily cases.

Should the code crash due to an internet outage, copy the console output into a text file and 
run `recovery.py`. This program digs through the console output and creates a csv file as if
the crash never happened. 

To avoid such crashes, consider running the code on Google Colab, which seems to be a very
 good alternative.