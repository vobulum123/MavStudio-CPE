{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # MavStudio \'96 CPE Signal Strength vs Time\
\
Streamlit app for visualizing CPE signal strength metrics (RSRP, RSRQ, SINR, RSSI) over time from CSV exports. Each CPE appears as a separate line, with interactive filters for metric, CPEs, and time window.\
\
## Features\
\
- Upload CSV with columns: `net_device__router__desc`, `created_ts`, `rsrp`, `rsrq`, `sinr`, `rssi`\
- Interactive filters:\
  - Y-axis metric dropdown: RSRP / RSRQ / SINR / RSSI\
  - Multi-select CPE list (`net_device__router__desc`)\
  - Date + hour range slider on `created_ts`\
- Plotly line chart:\
  - X-axis: `created_ts` (UTC)\
  - Y-axis: selected metric\
  - Color: CPE (`net_device__router__desc`)\
  - Hover with unified time cursor\
\
## Installation\
\
### Prerequisites\
\
- Python 3.8+ installed and on your PATH\
- Git (optional, if you clone from GitHub) [web:48][web:51]\
\
### macOS\
\
}