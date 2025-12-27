import streamlit as st
import pandas as pd
import plotly.express as px  # interactive line chart

st.set_page_config(page_title="RSRP / SINR vs Time", layout="wide")

st.title("Signal Strength vs Time (TUL Airport PCN-3)")

# 1) Upload CSV --------------------------------------------------------------
uploaded = st.file_uploader(
    "Upload Signal_Strength_-_TUL_Airport_PCN-3.csv",
    type=["csv"],
)

if uploaded is None:
    st.stop()

# Read CSV, parse created_ts as datetime
df = pd.read_csv(
    uploaded,
    parse_dates=["created_ts"],   # uses your created_ts column as datetime [file:101][web:95]
)

# Keep only relevant columns
df = df[
    [
        "net_device__router__desc",  # CPE description (column D) [file:101]
        "created_ts",                # X-axis (column N) [file:101]
        "rsrp",
        "rsrq",
        "sinr",
        "rssi",
    ]
].dropna(subset=["created_ts"])

df = df.sort_values(["net_device__router__desc", "created_ts"])

# 2) Sidebar controls --------------------------------------------------------
st.sidebar.header("Filters")

# Y-axis metric selector
metric_map = {
    "RSRP": "rsrp",
    "RSRQ": "rsrq",
    "SINR": "sinr",
    "RSSI": "rssi",
}
metric_label = st.sidebar.selectbox(
    "Y-axis metric",
    list(metric_map.keys()),
    index=0,
)
y_col = metric_map[metric_label]

# CPE multi-select
all_cpes = sorted(df["net_device__router__desc"].unique())
selected_cpes = st.sidebar.multiselect(
    "Select one or more CPEs",
    all_cpes,
    default=all_cpes[:3],   # first few selected by default
)

if not selected_cpes:
    st.warning("Select at least one CPE in the sidebar.")
    st.stop()

df_sel = df[df["net_device__router__desc"].isin(selected_cpes)]

# 3) Line chart --------------------------------------------------------------
fig = px.line(
    df_sel,
    x="created_ts",
    y=y_col,
    color="net_device__router__desc",     # one line per CPE [web:87]
    markers=True,
    labels={
        "created_ts": "created_ts (UTC)",
        y_col: metric_label,
        "net_device__router__desc": "CPE (router_desc)",
    },
    title=f"{metric_label} vs created_ts per CPE",
)

fig.update_layout(
    hovermode="x unified",
    legend_title_text="CPE",
)

st.plotly_chart(fig, use_container_width=True)
