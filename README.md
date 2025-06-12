# Air Quality Analytics Dashboard (Preswald App)

This is a simple interactive **Air Quality Analytics Dashboard** built using **Preswald** and **Plotly**.

It provides an easy way to explore air quality metrics across different cities and visualize trends and distributions in the dataset.

---

## Features

**Interactive AQI Filter**  
**Average AQI per City (Bar Chart)**  
**AQI Distribution (Histogram)**  
**PM2.5 vs PM10 Scatter Plot**  
**City-wise Metric Trend (Line Chart)**  

---

## How it works

### 1️ AQI Filter and Summary

- User can select a **minimum AQI** value via a slider.
- The app displays the number of entries and cities with AQI greater than or equal to the selected value.

### 2️ Visualizations

- **Average AQI per City** → Bar chart.
- **Distribution of AQI** → Histogram.
- **PM2.5 vs PM10** → Scatter plot showing correlation.
- **City-wise Metric Trends**:
  - User selects a **City** and a **Metric** (column) to visualize trends for that metric over time.
 
- The app allows users to quickly explore:

    - Which cities consistently have high AQI.

    - How AQI is distributed across all observations.

    - The relationship between PM2.5 and PM10.

How various air quality metrics behave over time for a given city.


---

## How to run locally

### Prerequisites

- Python 3.7+
- Preswald
- Pandas
- Plotly

### Install dependencies

```bash
pip install preswald pandas plotly

#### Run using
python hello.py
```

