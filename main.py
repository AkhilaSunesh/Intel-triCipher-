import argparse
from utils.pcap_processor import extract_flows_from_pcap
from utils.csv_loader import load_csv_as_df
from utils.feature_extractor import extract_features_from_flows
from models.anomaly_model import run_anomaly_model
from config import PCAP_FILE, CSV_FILE

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pcap", help="Path to PCAP file", default=None)
    parser.add_argument("--csv", help="Path to CSV file", default=None)
    parser.add_argument("--model", help="Model type: iso or kmeans", choices=["iso", "kmeans"], default="iso")

    args = parser.parse_args()

    if args.csv:
        print("Loading CSV...")
        df = load_csv_as_df(args.csv)
    elif args.pcap:
        print("Processing PCAP...")
        flows = extract_flows_from_pcap(args.pcap)
        df = extract_features_from_flows(flows)
    else:
        print("Please specify --csv or --pcap input.")
        return

    print("Running anomaly model...")
    run_anomaly_model(df, model_type=args.model)

if __name__ == "__main__":
    main()
