import pandas as pd
import matplotlib.pyplot as plt

# Print the minimum value of the Engineering column
print(df['Engineering'].min())

# Print the maximum value of the Engineering column
print(df['Engineering'].max())

# Construct the mean percentage per year: mean
mean = df.mean(axis = 'columns')

# Plot the average percentage per year
_ = mean.plot()

# Display the plot
plt.show()
