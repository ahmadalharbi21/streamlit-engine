import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Data Visualization App", layout="wide")

# Title
st.title("Data Visualization Dashboard")

# Section 1: Introduction
st.header("Introduction")
st.write("Welcome to the Data Visualization Dashboard! This app is designed to display various graphs and insights.")

# Section 2: Graph 1
st.header("Graph 1: Line Chart")
st.write("Below is a placeholder for a line chart.")
st.image("placeholder_line_chart.png", caption="Line Chart Placeholder", use_column_width=True)

# Section 3: Graph 2
st.header("Graph 2: Bar Chart")
st.write("Below is a placeholder for a bar chart.")
st.image("placeholder_bar_chart.png", caption="Bar Chart Placeholder", use_column_width=True)

# Section 4: Graph 3
st.header("Graph 3: Scatter Plot")
st.write("Below is a placeholder for a scatter plot.")
st.image("placeholder_scatter_plot.png", caption="Scatter Plot Placeholder", use_column_width=True)

# Section 5: Graph 4
st.header("Graph 4: Pie Chart")
st.write("Below is a placeholder for a pie chart.")
st.image("placeholder_pie_chart.png", caption="Pie Chart Placeholder", use_column_width=True)

# Section 6: Conclusion
st.header("Conclusion")
st.write("Thank you for exploring the Data Visualization Dashboard. Add your insights and analysis here.")