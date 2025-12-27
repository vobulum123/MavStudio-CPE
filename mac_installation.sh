{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 #!/bin/bash\
# Setup script for MavStudio-CPE Signal Strength app on macOS\
\
set -e\
\
echo "=== Setting up Python virtual environment (macOS) ==="\
\
# Create virtual environment (folder: venv)\
python3 -m venv venv\
\
# Activate it\
source venv/bin/activate\
\
# Upgrade pip and install dependencies\
pip install --upgrade pip\
pip install -r requirements.txt\
\
echo "=== Setup complete ==="\
echo "To run the app:"\
echo "  source venv/bin/activate"\
echo "  streamlit run app.py"\
echo\
echo "When done, deactivate with: deactivate"\
}