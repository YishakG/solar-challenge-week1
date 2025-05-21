import streamlit as st
import pandas as pd
from utils import load_data, plot_boxplot, get_top_regions

st.title("Solar Potential Dashboard")

# Country selection
countries = ['Benin', 'Sierra Leone', 'Togo']
selected_countries = st.multiselect("Select Countries", countries, default=countries)

if selected_countries:
    # Load data
    df = load_data(selected_countries)

    # Boxplot for GHI
    st.subheader("GHI Boxplot")
    fig = plot_boxplot(df, 'GHI', selected_countries)
    st.pyplot(fig)

    # Top regions table
    st.subheader("Top Regions by Average GHI")
    top_regions = get_top_regions(df, 'GHI')
    st.table(top_regions)