# This Python script is used for web scraping COVID-19 data from WorldOMeter.
# The data is then saved as a csv file.
# The hardest hit countries with the most deaths is visualized as a bar chart using Plotly.
# COVID-19 data is updated daily. See WorldOMeter documentation for primary data sources.
# Website: https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/

# Import relevant modules to be used.
import requests
import pandas as pd
import plotly.express as px

# The url of the website used to scrape the data.
url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'

# Pandas module used to request and read the url and store as dataframe.
request = requests.get(url)
dfs = pd.read_html(request.text)

# Extract the relevant dataframe used for analysis from the list of dataframes.
the_df = dfs[0]

# Save the relevant dataframew as a csv.
the_df.to_csv('Covid Data.csv')

# Use Plotly Express to visualize and display the COVID-19 deaths by country.
fig = px.bar(the_df.head(30), x='Country', y='Deaths', title="Countries with the highest COVID-19 deaths (Source: Worldometer, updated daily)")
fig.show()

# Source: WorldOMeter, data is updated daily.
# See documentation on WorldOMeter for primary data sources.


