import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

# Create a plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Data Line')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sample Plot')
plt.legend()

# Save the plot as a file
plt.savefig('output_plot.png')  # Saves the plot to a file
