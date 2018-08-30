import pandas as pd

# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(frame = airquality, id_vars = ['Month', 'Day'], var_name = 'measurement', value_name = 'reading')

# Print the head of airquality_melt
print(airquality_melt.head())
