import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
data = pd.read_csv("students.csv")

# Show dataset
print(data.head())

# Average math score
print("Average Math Score:")
print(data["math score"].mean())

# Graph
data["math score"].plot(kind="hist")

plt.title("Math Score Distribution")
plt.xlabel("Marks")
plt.ylabel("Students")

plt.show()