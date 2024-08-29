#!/bin/sh
chmod +x devserver.sh
source .venv/bin/activate
streamlit run main.py --server.port $PORT --server.headless true