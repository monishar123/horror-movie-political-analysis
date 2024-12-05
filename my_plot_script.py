import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create plot
plt.plot(x, y)
plt.title("Sample Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Save the chart as a PNG file
plt.savefig("chart_name.png")

# Optional: Display the chart
plt.show()
import plotly.express as px

# Sample data
df = px.data.iris()

# Create plot
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 title="Sample Scatter Plot")

# Save the chart as a PNG file
fig.write_image("scatter_plot.png")

# Optional: Display the chart
fig.show()
