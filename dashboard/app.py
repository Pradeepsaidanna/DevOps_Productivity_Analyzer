import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(layout="wide")

st.title(" DevOps Team Productivity & Bottleneck Analyzer")

DATA_PATH = "../data/github_prs_with_duration.csv"

if not os.path.exists(DATA_PATH):
    st.error("CSV file not found. Please run the analysis step first.")
else:
    df = pd.read_csv(DATA_PATH)
    df['duration_hours'] = df['duration_hours'].fillna(0)

    st.subheader(" Pull Request Duration Summary")
    st.dataframe(df[['number', 'title', 'duration_hours']])

    st.write("### Duration Statistics")
    st.write(df['duration_hours'].describe())

    fig = px.histogram(df, x='duration_hours', nbins=15, title="Distribution of PR Durations")
    st.plotly_chart(fig, use_container_width=True)

    threshold = df['duration_hours'].mean() + df['duration_hours'].std()
    bottlenecks = df[df['duration_hours'] > threshold]

    st.write("### Bottleneck PRs (above normal duration)")
    st.dataframe(bottlenecks[['number', 'title', 'duration_hours']])

    # Export option
    st.download_button(" Download Full Data (CSV)", data=df.to_csv(index=False), file_name="pr_analysis.csv")
