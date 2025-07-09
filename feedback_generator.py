def generate_feedback(flagged_df, total_flows):
    num_anomalies = len(flagged_df)

    if num_anomalies == 0:
        return "Everything looks normal in the network traffic. No suspicious activity was found."

    feedback = f"We found **{num_anomalies} anomalous flows** out of {total_flows} total.\n\n"

    # Optional: Try to explain why (based on features)
    reasons = []
    if "total_bytes" in flagged_df.columns:
        if flagged_df["total_bytes"].mean() > 5000:
            reasons.append("Some flows have very high data transfer sizes.")
    if "pkt_count" in flagged_df.columns:
        if flagged_df["pkt_count"].mean() > 50:
            reasons.append("Some connections had unusually many packets.")
    if "iat_std" in flagged_df.columns:
        if flagged_df["iat_std"].mean() < 1.0:
            reasons.append("Flows were tightly packed in time, which may indicate a bursty or automated attack.")

    if reasons:
        feedback += "**Potential reasons:**\n- " + "\n- ".join(reasons)
    else:
        feedback += "The model detected these as unusual, but no specific reason was found from feature patterns."

    return feedback
