import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("data/processed/cleaned_sales_data.csv")

print(df.head())

# Sales by Category
df.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.show()

# Profit by Region
df.groupby("Region")["Profit"].sum().plot(kind="bar")
plt.title("Profit by Region")
plt.show()
