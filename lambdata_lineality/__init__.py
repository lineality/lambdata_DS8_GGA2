"""
lambdata - a collection of data science helper functions
"""

import pandas as pd
import numpy as np

#sample code

#sample datasets
ONES = pd.DataFrame(np.ones(5))
ZEROS = pd.DataFrame(np.zeros(20))

#sample functions
def decriment(x):
    return (x - 1)
