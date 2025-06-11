from preswald import get_df, plotly, slider, table, text, query, selectbox
import pandas as pd
import plotly.express as px

df = get_df("Air_Quality")

text("# Air Quality Analytics Dashboard")
text("##### Select a value in below slider to view number of entries with more AQI and the cities")

min_aqi = slider("Minimum AQI", min_val=0.0, max_val=500.0, default=100.0)
df["AQI"] = pd.to_numeric(df["AQI"], errors="coerce")
text(f"## Finding cities with AQI ≥ {min_aqi}")
filtered_df = df[df["AQI"] >= float(min_aqi)]
text(f"##### Number of Entries with given  Minimum AQI:{len(filtered_df)}.\n Cities with given  Minimum AQI:{filtered_df['City'].unique()} ")
text(f"##### We can see the Average AQI, Distribution of AQI over years, AQI Trend over years PM2.5 vs PM10 Scatter Plot")

text("## Average AQI per City")
city_stats_df = df.groupby("City")["AQI"].agg(avg_aqi="mean", max_aqi="max", high_aqi_days=lambda x: (x >= 100).sum()).reset_index()

fig_city_aqi = px.bar(
    city_stats_df.sort_values("avg_aqi", ascending=False),
    x="City",
    y="avg_aqi",
    title="Average AQI per City"
)
plotly(fig_city_aqi)

text("## Distribution of AQI")

fig_hist_aqi = px.histogram(
    df,
    x="AQI",
    nbins=30,
    title="Distribution of AQI"
)
plotly(fig_hist_aqi)

text("## PM2.5 vs PM10 Scatter Plot")

fig_scatter_pm = px.scatter(
    df,
    x="PM2.5",
    y="PM10",
    color="City",
    title="PM2.5 vs PM10 — Correlation by City"
)
plotly(fig_scatter_pm)

text("### City Distribution By Metric ")

city_options = df["City"].unique().tolist()
text("##### Select City")
city_choice = selectbox( label="Choose City",
    options=city_options)
text("##### Select Metric") 
metric_options = df.columns.values.tolist()

metric_options.remove("City")

metric_choice = selectbox(label="Choose Metric", options=metric_options)

filtered_city_df = df[df["City"] == city_choice]
fig_line_plot = px.line(
    filtered_city_df,
    x=filtered_city_df.index,
    y=metric_choice,
    title=f"{metric_choice} over Time for {city_choice}"
)
plotly(fig_line_plot)





