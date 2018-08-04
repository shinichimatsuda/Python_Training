import pandas as pd
import matplotlib.pyplot as plt

# Create a plot with color='red'
_ = df.plot(color='red')

# Add a title
_ = plt.title('Temperature in Austin')

# Specify the x-axis label
_ = plt.xlabel('Hours since midnight August 1, 2010')

# Specify the y-axis label
_ = plt.ylabel('Temperature (degrees F)')

# Display the plot
_ = plt.show()
