#graph plotter
#draw a chart
#install lib: matplotlib


import matplotlib.pyplot as plt

x1 = [2, 4, 5]
y1 = [2, 3, 6]

plt.plot(x1, y1, label = "Line 1")

x2 = [1, 2, 3]
y2 = [3, 4, 5]

plt.plot(x2, y2, label = "Line 2")

plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.title("Demo Graph - Two Lines")

plt.legend()
plt.show()

#another type for customizations

import matplotlib.pyplot as plt

x = [2, 4, 5]
y = [2, 3, 6]

plt.plot(x, y, color="green", linestyle="dashed", linewidth=3, marker="o", markerfacecolor="blue", markersize=12)

plt.ylim(1,8)  #the ranges
plt.xlim(1,8)


plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.title("Demo Graph - Customization")

plt.show()


#to draw a bar chart

import matplotlib.pyplot as plt

left = [2, 4, 5]
height = [12,13, 16]

tick_label = ["two", "four", "five"]

plt.bar(left, height, tick_label = tick_label, width = 0.8, color = ["blue", "orange"])


plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.title("Demo Graph - Bar Chart")

plt.show()
