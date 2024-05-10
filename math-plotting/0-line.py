#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

# x values ranging from 0 to 10
x = np.arange(0, 11)

# Plot y as a solid red line
# 'r-' specifies solid red line
plt.plot(x, y, 'r-')

# x-axis range from 0 to 10
plt.xlim(0, 10)

# labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot of Y')

# Display the plot
plt.show()

