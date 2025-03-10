import matplotlib.pyplot as plt

# Data for the plot
x = [1, 2, 3, 4, 5]  # X-axis values
y = [2, 3, 5, 7, 11]  # Y-axis values

# Create the plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Prime Numbers')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Matplotlib Example')

# Add a legend
plt.legend()

# Show the plot
plt.show()