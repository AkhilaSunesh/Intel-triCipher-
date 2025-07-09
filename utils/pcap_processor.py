from scapy.all import rdpcap
from collections import defaultdict
from config import FLOW_TIMEOUT

def extract_flows_from_pcap(pcap_path):
    pkts = rdpcap(pcap_path)
    flows = {}

    for pkt in pkts:
        if not pkt.haslayer("IP"):
            continue
        ip = pkt["IP"]
        proto = ip.proto
        l4 = pkt.payload

        if not hasattr(l4, "sport") or not hasattr(l4, "dport"):
            continue

        key = (ip.src, ip.dst, l4.sport, l4.dport, proto)
        rev_key = (ip.dst, ip.src, l4.dport, l4.sport, proto)
        now = pkt.time

        if key in flows and now - flows[key]["last_seen"] <= FLOW_TIMEOUT:
            flow = flows[key]
        elif rev_key in flows and now - flows[rev_key]["last_seen"] <= FLOW_TIMEOUT:
            flow = flows[rev_key]
        else:
            flow = {"packets": [], "first_seen": now}
            flows[key] = flow

        flow["packets"].append(pkt)
        flow["last_seen"] = now

    return flows
