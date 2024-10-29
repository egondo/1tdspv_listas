import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Product': ['P1', 'P2', 'P1', 'P2', 'P1', 'P2'],
        'Sales': [100, 150, 200, 180, 120, 140]}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a pivot table
pivot_table = df.pivot_table(index='Category', columns='Product', values='Sales')

print(pivot_table)

# Plot the pivot table as a bar chart
pivot_table.plot(kind='bar')
plt.title('Sales by Category and Product')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.xticks(rotation=0)
plt.show()