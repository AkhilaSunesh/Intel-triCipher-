# Mini Joy

Mini Joy is a lightweight, modular anomaly detection tool for network traffic analysis using machine learning. It is designed to be simple, extensible, and user-friendly, making it ideal for students, researchers, and developers exploring AI-based cybersecurity solutions.

## Overview

Mini Joy supports both raw PCAP files and preprocessed CSV datasets, enabling flexible input formats for various use cases. It extracts flow-level features and applies unsupervised machine learning models such as Isolation Forest and KMeans to identify anomalous network behavior. A Streamlit-based web interface allows for interactive analysis, and an integrated feedback module generates plain-language explanations for flagged anomalies.

## Features

- Anomaly detection using Isolation Forest and KMeans
- Flow-level feature extraction from PCAP and CSV inputs
- AI-generated feedback for non-technical interpretation
- Streamlit GUI for interactive file upload, model selection, and result visualization
- Export of flagged anomalies in JSON format for further analysis

## File Structure
<img width="340" height="517" alt="image" src="https://github.com/user-attachments/assets/3530ffb4-43d6-4234-95b3-d2d7f4b293bd" />


## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/mini-joy.git
cd mini-joy
```
2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3.Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage
### Using the Streamlit GUI
Run the application with:
```bash
streamlit run app.py
```
<ul>
  <li> Upload a PCAP or CSV file </li>
<li>Choose a model (Isolation Forest or KMeans)</li>
<li>View anomaly scores and explanations</li>
<li>Download flagged flows in JSON format</li>
</ul>

### Using the Command Line
```bash
python main.py --input path/to/file.pcap --model isolation
```

## Dataset
This project uses the CICIDS2017 dataset developed by the Canadian Institute for Cybersecurity. It includes realistic network traffic with labeled attacks such as DoS, DDoS, Brute Force, and Port Scans.

Learn more: (https://www.unb.ca/cic/datasets/ids-2017.html)
CSV version: (https://www.kaggle.com/datasets/ericanacletoribeiro/cicids2017-cleaned-and-preprocessed)

## Acknowledgments
We acknowledge the mentors, institutional heads, and industrial mentors for their guidance and support. We thank Intel Corporation for providing us with such an opportunity.




