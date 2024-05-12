#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

# Fruit names and colors
fruits = ['apples', 'bananas', 'oranges', 'peaches']
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']

# Plotting stacked bar graph
plt.bar(np.arange(3), fruit[0], color=colors[0], label=fruits[0])
for i in range(1, len(fruits)):
    plt.bar(np.arange(3), fruit[i], bottom=np.sum(fruit[:i], axis=0), color=colors[i], label=fruits[i])

# Labels and title
plt.xlabel('Person')
plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')

# y-axis range and ticks
plt.ylim(0, 80)
plt.yticks(np.arange(0, 81, 10))

# legend
plt.legend()

# Showing plot
plt.show()
