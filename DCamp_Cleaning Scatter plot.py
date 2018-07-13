# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# Create and display the first scatter plot
_ = df.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()

# Create and display the second scatter plot
_ = df_subset.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()
