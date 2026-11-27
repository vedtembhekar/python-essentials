# Assignment 10: Data Visualization using Matplotlib

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

# Line Plot
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# Scatter Plot
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# Box Plot
plt.boxplot(y)
plt.title("Box Plot")
plt.show()

# Bar Chart
plt.bar(x, y)
plt.title("Bar Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# Pie Chart
plt.pie(y, labels=x, autopct="%1.1f%%")
plt.title("Pie Chart")
plt.show()
