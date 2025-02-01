import numpy as np
import matplotlib.pyplot as plt

# Define two arrays
array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([5, 15, 25, 35, 45])

# Create subplots
fig, axs = plt.subplots(3, 2, figsize=(12, 10))

# Line Chart
axs[0, 0].plot(array1, label='Array 1', marker='o')
axs[0, 0].plot(array2, label='Array 2', marker='x')
axs[0, 0].set_title('Line Chart')
axs[0, 0].set_xlabel('Index')
axs[0, 0].set_ylabel('Value')
axs[0, 0].legend()

# Bar Chart
bar_width = 0.35
index = np.arange(len(array1))
axs[0, 1].bar(index, array1, bar_width, label='Array 1')
axs[0, 1].bar(index + bar_width, array2, bar_width, label='Array 2')
axs[0, 1].set_title('Bar Chart')
axs[0, 1].set_xlabel('Index')
axs[0, 1].set_ylabel('Value')
axs[0, 1].set_xticks(index + bar_width / 2)
axs[0, 1].set_xticklabels(index)
axs[0, 1].legend()

# Pie Chart
labels = ['Array 1', 'Array 2']
sizes = [np.sum(array1), np.sum(array2)]
axs[1, 0].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
axs[1, 0].set_title('Pie Chart')

# Scatter Plot
axs[1, 1].scatter(array1, array2, color='r')
axs[1, 1].set_title('Scatter Plot')
axs[1, 1].set_xlabel('Array 1')
axs[1, 1].set_ylabel('Array 2')

# Histogram
axs[2, 0].hist(array1, bins=5, alpha=0.5, label='Array 1')
axs[2, 0].hist(array2, bins=5, alpha=0.5, label='Array 2')
axs[2, 0].set_title('Histogram')
axs[2, 0].set_xlabel('Value')
axs[2, 0].set_ylabel('Frequency')
axs[2, 0].legend()

# Hide the empty subplot
axs[2, 1].axis('off')

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()
