import numpy as np
import pandas as pd

def extract_features_from_flows(flows):
    def extract(flow):
        pkts = flow["packets"]
        lengths = [len(p) for p in pkts]
        times = [p.time for p in pkts]
        iats = np.diff(sorted(times)) if len(times) > 1 else [0]

        return {
            "pkt_count": len(pkts),
            "total_bytes": sum(lengths),
            "len_avg": np.mean(lengths),
            "len_min": np.min(lengths),
            "len_max": np.max(lengths),
            "iat_mean": float(np.mean(iats)),
            "iat_std": float(np.std(iats)),
        }

    return pd.DataFrame([extract(f) for f in flows.values()])
