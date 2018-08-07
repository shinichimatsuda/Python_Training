import pandas as pd
import matplotlib.pyplot as plt

# Print summary statistics of the fare column with .describe()
print(df['fare'].describe())

# Generate a box plot of the fare column
_ = df['fare'].plot(kind = 'box')

# Show the plot
plt.show()
