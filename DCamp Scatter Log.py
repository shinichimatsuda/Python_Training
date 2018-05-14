import matplotlib.pyplot as plt

# Change the line plot below to a scatter plot
_ = plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
_ = plt.xscale('log')

# Show plot
plt.show()
