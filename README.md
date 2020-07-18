# **Viral Twitter**
This project aims to scrape and analyze **time stamped** twitter data focusing on hashtags to 
cross reference with COVID-19 data.

I hope to test whether COVID data demonstrates a correlation between the anti-mask, anti-lockdown
sentiments and the spreading of the coronavirus.

As of Jul 17th, I have finished the code for getting the data. The program outputs the data
collected with the rest of the original COVID data for easier comparison.

Gather_Data.py is the main file that completes this task. Splitter is the helper program that
split the COVID data into each county.

This program is likely not very efficient and may take a long time to run. Be advised to tune
up the sleep time on twint should Twitter block further accesses.

Should the code crash due to an internet outage, copy the console output into a text file and 
run recovery.py. Running the code on Google Colab seem to demonstrate significantly better results, although this 
can be due to a lack of updated hardware.
