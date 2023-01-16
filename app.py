import streamlit as st
import pandas as pd
import plotly.express as px

# Read data
df = pd.read_excel('data/processed_data.xlsx')

# Page config
st.set_page_config(
    page_title="Country Olympic Games and Population data",
    page_icon="🥇",
    layout="wide"
)

# Sidebar
st.sidebar.header('Country Olympic Games and Population data')
year_input = st.sidebar.selectbox('Pick a year', df['year'].unique())
country_input = st.sidebar.multiselect(
    'Pick a country for lineplot',
    df['country_name'].unique(), df['country_name'].head(1))

# Filtered data
scatter_data = df.query("year == {}".format(year_input))
line_data = df.query("country_name == {}".format(country_input))

# Plot definitions
fig_scatter = px.scatter(scatter_data, x="midyear_population", y="total", color="country_name",
                 size='midyear_population', hover_data=['gold', 'silver', 'bronze'], title='Olympic Medals Tally vs Midyear Population')

fig_line = px.line(line_data, x="year", y="total", color="country_name", title='Olympic Medal Tally over the years')

fig_bar = px.bar(scatter_data, x='growth_rate', y='country_name', color="country_name")

fig_pie = px.pie(scatter_data, values='total', names='country_name')

st.header("Dashboard")

col1, col2 = st.columns(2)

with col1:
   st.plotly_chart(fig_scatter)

with col2:
   st.plotly_chart(fig_line)

col3, col4 = st.columns(2)

with col3:
   st.plotly_chart(fig_bar)

with col4:
   st.plotly_chart(fig_pie)
