import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv


# with open('iris.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["SN", "Name", "Contribution"])
#     writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
#     writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
#     writer.writerow([3, "Guido van Rossum", "Python Programming"])

iris = pd.read_csv('iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
print(iris.head())


# create a figure and axis
fig, ax = plt.subplots()

# scatter the sepal_length against the sepal_width
ax.scatter(iris['sepal_length'], iris['sepal_width'])
# set a title and labels
ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')
