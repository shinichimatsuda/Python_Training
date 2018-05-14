# Create box plot with Seaborn's default settings
import matplotlib.pyplot as plt
import seaborn as sns
_ = sns.boxplot(x = 'species', y = 'petal length (cm)', data = df)

# Label the axes
_ = plt.xlabel('species')
_ = plt.ylabel('petal length (cm)')

# Show the plot
plt.show()
