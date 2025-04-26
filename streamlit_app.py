import streamlit as st
import pandas as pd
import math
from pathlib import Path
import datetime as dt

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Wordle Sibs Dashboard',
    page_icon=':smile:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.

@st.cache_data
def get_wordle_data():
    """Grab Wordle stats data from a CSV file.

    This uses caching to avoid having to read the file every time. If we were
    reading from an HTTP endpoint instead of a file, it's a good idea to set
    a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
    """

    # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
    DATA_FILENAME = Path(__file__).parent/'data/wordle_sibs_data.csv'
    wordle_data = pd.read_csv(DATA_FILENAME)

wordle_stats_df = get_wordle_data()

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
# :earth_americas: GDP dashboard

Browse GDP data from the [World Bank Open Data](https://data.worldbank.org/) website. As you'll
notice, the data only goes to 2022 right now, and datapoints for certain years are often missing.
But it's otherwise a great (and did I mention _free_?) source of data.
'''

# Add some spacing
''
''

st.header('Wordle Sibs Stats', divider='gray')

''

st.line_chart(
    wordle_stats_df,
    x='Date',
    y=('Rob', 'Chris', 'Anthony'),
    color=y,
)

''
''


min_date = dt.to_date('2023', '6', '1')

