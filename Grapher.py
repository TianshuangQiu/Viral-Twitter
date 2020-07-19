import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

import numpy as np
import pandas as pd

msft = pd.read_csv('Output/COMPLETE_AZ.csv')
fname = cbook.get_sample_data('msft.csv', asfileobj=False)
with cbook.get_sample_data('msft.csv') as file:
    msft = pd.read_csv(file)