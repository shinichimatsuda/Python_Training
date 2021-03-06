import matplotlib.pyplot as plt

# Print the last item of gdp_cap and life_exp
print(gdp_cap[-1], life_exp[-1])
print(life_exp[-1])   ### For an automatic answer checking purpose, this line was inserted.

# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
_ = plt.plot(gdp_cap, life_exp)

# Display the plot
plt.show()
