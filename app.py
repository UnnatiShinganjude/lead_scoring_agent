# app.py
import streamlit as st
import pandas as pd
from data_generator import generate_mock_data

#page config
st.set_page_config(page_title="Lead Gen Agent", layout="wide")

# session state reset function
def reset_filters():
    st.session_state.score_slider = 0
    st.session_state.funding_multiselect = []
    st.session_state.search_input = ""

#load the data
@st.cache_data 
def load_data():
    return generate_mock_data(500)

df = load_data()

#sidebar
st.sidebar.header("Filter Controls")
st.sidebar.button("🔄 Reset All Filters", on_click=reset_filters)
st.sidebar.divider()

# Probability Slider
min_score = st.sidebar.slider(
    "Minimum Probability Score", 
    min_value=0, max_value=100, value=0, key='score_slider'
)

# Funding Filter
selected_funding = st.sidebar.multiselect(
    "Filter by Funding Status", 
    options=df['Funding_Status'].unique(),
    key='funding_multiselect'
)

#Dashboard ui
st.title("3D In-Vitro Lead Scoring Agent")
st.markdown("""
Welcome to the Lead Scoring Agent dashboard! This tool helps you identify and prioritize potential leads in the 3D in-vitro toxicology space. Use the filters on the sidebar to refine your search based on probability scores, funding status, and keywords. The generated list includes mock data for demonstration purposes. Explore the leads, assess their fit, and download the qualified list for your outreach efforts.
""")

# Search Bar
st.subheader("Lead Database")
search_query = st.text_input(
    "Keyword Search", 
    placeholder="Type 'Boston', 'Toxicology', or 'Pfizer'...",
    key='search_input'
)

#filter logic
filtered_df = df.copy()

# use Slider
filtered_df = filtered_df[filtered_df['Score'] >= min_score]

# use Funding
if selected_funding:
    filtered_df = filtered_df[filtered_df['Funding_Status'].isin(selected_funding)]

# use  Search
if search_query:
    filtered_df = filtered_df[
        filtered_df.astype(str).apply(lambda row: row.str.contains(search_query, case=False).any(), axis=1)
    ]

# result display
col1, col2, col3 = st.columns(3)
col1.metric("Leads Found", len(filtered_df))
col2.metric("High Probability (>80)", len(filtered_df[filtered_df['Score'] > 80]))

st.dataframe(
    filtered_df,
    column_config={
        "Score": st.column_config.ProgressColumn("Propensity", format="%d", min_value=0, max_value=100),
        "Email": st.column_config.LinkColumn("Email"),
        "Uses_Similar_Tech": st.column_config.CheckboxColumn("Tech Fit"),
        "Recent_Publication": st.column_config.CheckboxColumn("Paper Pub.")
    },
    use_container_width=True,
    hide_index=True,
    height=600 
)

# Export
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button("Download List (CSV)", data=csv, file_name="qualified_leads.csv", mime="text/csv")