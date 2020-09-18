import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib

import numpy as np
import pandas as pd
import csv

data = pd.read_csv('Output/COMPLETE_FL.csv', parse_dates=["Date"])
data.set_index('Date',inplace=True)

target = ["Cases", "Deaths", "#NoMasks", "#BurnYourMask", "#IWillNotComply",  "#OpenAmerica", "#OpenSchools", "#WearAMask", "#WearADamnMask"]

fig, ax = plt.subplots(nrows=4)

ax[0].bar(data.index, data['#BurnYourMask'], color = "Blue")
ax[1].bar(data.index, data['#IWillNotComply'], color = "Orange")
ax[2].bar(data.index, data['#OpenAmerica'], color = "Black")
ax[3].bar(data.index, data['#OpenSchools'], color = "Green")

ax[0].set_title("#BurnYourMask")
ax[1].set_title("#IWillNotComply")
ax[2].set_title("#OpenAmerica")
ax[3].set_title("#OpenSchools")

plt.show()
