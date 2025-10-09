import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from xgboost import XGBClassifier
import joblib

# Set random seed for reproducibility
np.random.seed(42)
n_samples = 10000

# Generate synthetic features
features = {
    'requests_per_ip_per_min': np.concatenate([
        np.random.normal(50, 10, n_samples // 2),  # Genuine traffic
        np.random.normal(500, 100, n_samples // 2)  # DDoS traffic
    ]),
    'unique_paths_accessed': np.concatenate([
        np.random.normal(10, 2, n_samples // 2),  # Genuine
        np.random.normal(1, 0.5, n_samples // 2)  # DDoS
    ]),
    'avg_interval_ms': np.concatenate([
        np.random.normal(1000, 200, n_samples // 2),  # Genuine
        np.random.normal(50, 20, n_samples // 2)  # DDoS
    ]),
    'user_agent_variance': np.concatenate([
        np.random.normal(15, 5, n_samples // 2),  # Genuine
        np.random.normal(2, 1, n_samples // 2)  # DDoS
    ])
}

# Labels: 0 = genuine, 1 = DDoS
labels = np.concatenate([
    np.zeros(n_samples // 2),
    np.ones(n_samples // 2)
])

# Create DataFrame
df = pd.DataFrame(features)
df['label'] = labels

# Train-test split
X = df.drop('label', axis=1)
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Random Forest model
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

# Evaluate Random Forest model
print("=== Random Forest ===")
print("Accuracy:", accuracy_score(y_test, y_pred_rf))
print("Precision:", precision_score(y_test, y_pred_rf))
print("Recall:", recall_score(y_test, y_pred_rf))
print("F1 Score:", f1_score(y_test, y_pred_rf))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred_rf))
print("\nClassification Report:\n", classification_report(y_test, y_pred_rf))

# Export Random Forest model
joblib.dump(rf, 'random_forest_ddos_model.pkl')

# Train XGBoost model
xgb = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
xgb.fit(X_train, y_train)
y_pred_xgb = xgb.predict(X_test)

# Evaluate XGBoost model
print("\n=== XGBoost ===")
print("Accuracy:", accuracy_score(y_test, y_pred_xgb))
print("Precision:", precision_score(y_test, y_pred_xgb))
print("Recall:", recall_score(y_test, y_pred_xgb))
print("F1 Score:", f1_score(y_test, y_pred_xgb))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred_xgb))
print("\nClassification Report:\n", classification_report(y_test, y_pred_xgb))

# Export XGBoost model
joblib.dump(xgb, 'xgboost_ddos_model.pkl')
