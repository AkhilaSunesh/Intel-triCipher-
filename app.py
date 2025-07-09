import streamlit as st
import pandas as pd
import tempfile
import os

from utils.pcap_processor import extract_flows_from_pcap
from utils.csv_loader import load_csv_as_df
from utils.feature_extractor import extract_features_from_flows
from models.anomaly_model import run_anomaly_model
from feedback_generator import generate_feedback


st.title("Mini Joy: Network Anomaly Detector")

uploaded_file = st.file_uploader("Upload a PCAP or CSV file", type=["pcap", "csv"])
model_type = st.selectbox("Choose Model", ["iso", "kmeans"])
run_button = st.button("Run Detection")

if run_button and uploaded_file:
    file_type = uploaded_file.name.split('.')[-1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_type}") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    if file_type == "csv":
        df = load_csv_as_df(tmp_path)
    elif file_type == "pcap":
        flows = extract_flows_from_pcap(tmp_path)
        df = extract_features_from_flows(flows)
    else:
        st.error("Unsupported file type!")
        st.stop()

    st.write("### Extracted Features (First 10 Rows):")
    st.dataframe(df.head(10))

    st.write("### Running Anomaly Detection...")
    run_anomaly_model(df, model_type=model_type)

    st.success("Detection Complete! Check outputs folder for results.")
    st.image("outputs/anomaly_plot.png", caption="Anomaly Score Distribution")

    import json
    with open("outputs/flagged_flows.json", "r") as f:
        flagged = pd.read_json(f)
        feedback = generate_feedback(flagged, total_flows=len(df))

    st.write("### 🤖 AI Feedback")
    st.markdown(feedback)
