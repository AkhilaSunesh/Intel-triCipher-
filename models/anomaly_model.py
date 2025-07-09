from sklearn.ensemble import IsolationForest
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import joblib
import json
import os

MODEL_PATH = "outputs/model.joblib"
PLOT_PATH = "outputs/anomaly_plot.png"

def run_anomaly_model(df, model_type="iso"):
    print(f"Training model: {model_type.upper()}")

    y_true = None
    if "Label" in df.columns:
        y_true = df["Label"].apply(lambda x: 1 if x == "Anomaly" else 0)
        df = df.drop(columns=["Label"])

    X_train, X_test = train_test_split(df, test_size=0.2, random_state=42)

    if model_type == "iso":
        model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    elif model_type == "kmeans":
        model = KMeans(n_clusters=2, random_state=42)
    else:
        raise ValueError("Unsupported model type")

    model.fit(X_train)
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

    if model_type == "iso":
        scores = -model.decision_function(X_test)
        y_pred = (scores > np.percentile(scores, 95)).astype(int)
    elif model_type == "kmeans":
        scores = np.min(model.transform(X_test), axis=1)
        y_pred = (scores > np.percentile(scores, 95)).astype(int)

    flagged = X_test[y_pred == 1]
    flagged["anomaly_score"] = scores[y_pred == 1]
    flagged.to_json("outputs/flagged_flows.json", orient="records", indent=2)
    print("Flagged flows saved to outputs/flagged_flows.json")

    # Plot
    plt.figure()
    plt.hist(scores, bins=30)
    plt.title(f"{model_type.upper()} Anomaly Score Distribution")
    plt.xlabel("Score")
    plt.ylabel("Count")
    plt.savefig(PLOT_PATH)
    print(f"Anomaly plot saved to {PLOT_PATH}")

    if y_true is not None:
        y_true_split = y_true.iloc[X_test.index]
        print("\n--- Evaluation Report ---")
        print(classification_report(y_true_split, y_pred))
        try:
            print("ROC AUC:", roc_auc_score(y_true_split, scores))
        except:
            print("ROC AUC calculation failed (possibly due to label imbalance)")
