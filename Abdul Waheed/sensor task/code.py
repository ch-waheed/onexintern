import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Task 1: Load the CSV file into a pandas dataframe
data = pd.read_csv("C:\\Users\\Mega Computers\\Desktop\\sensor task\\Sensor.csv")

# Task 2: Preprocess the data by checking for null values and removing duplicates
data.drop_duplicates(inplace=True)
data.dropna(inplace=True)

# Task 3: Calculate summary statistics for temperature and humidity
summary_stats = data[['Temperature', 'Humidity']].describe()

print(summary_stats,data)

# Task 4: Visualize temperature and humidity over time in a line chart
fig = px.line(data, x='Timestamp', y=['Temperature', 'Humidity'], color_discrete_sequence=px.colors.qualitative.Plotly)
fig.show()

# Task 5: Create a scatter plot with temperature on the x-axis and humidity on the y-axis
data['TimeOfDay'] = pd.to_datetime(data['Timestamp']).dt.hour.apply(lambda x: 'Morning' if 5 <= x < 12 else
                                                                   'Afternoon' if 12 <= x < 18 else
                                                                   'Evening' if 18 <= x < 22 else 'Night')
scatter_fig = px.scatter(data, x='Temperature', y='Humidity', color='TimeOfDay')
scatter_fig.show()

# Task 6: Create a heatmap
heatmap_fig = go.Figure(data=go.Heatmap(
    x=data['Temperature'],
    y=data['Humidity'],
    z=data['TimeOfDay'].astype('category').cat.codes,
    colorscale='Viridis'))

heatmap_fig.update_layout(
    title='Temperature and Humidity Heatmap',
    xaxis=dict(title='Temperature'),
    yaxis=dict(title='Humidity'))

heatmap_fig.show()            


