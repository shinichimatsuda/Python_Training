import pandas as pd

# Merge the DataFrames: m2o
m2o = pd.merge(left = site, right = visited, on = None, left_on = 'name', right_on = 'site')

# Print m2o
print(m2o)
