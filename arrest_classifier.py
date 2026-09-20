import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.preprocessing import LabelEncoder

# UPDATE THIS PATH to where you saved the CSV on your computer
df = pd.read_csv(r"C:\Users\YourName\Documents\wildlife-dashboard\wildlife_crime_seizures.csv")

df["arrest_made"] = (df["arrests_made"] > 0).astype(int)

feature_cols_cat = ["species_category", "product_type", "iucn_status", "origin_region",
                     "transport_method", "seizure_location_type", "enforcement_agency"]
feature_cols_num = ["quantity", "estimated_value_usd"]

X = df[feature_cols_cat + feature_cols_num].copy()
y = df["arrest_made"]

for col in feature_cols_cat:
    X[col] = LabelEncoder().fit_transform(X[col])

model = RandomForestClassifier(n_estimators=300, max_depth=6, min_samples_leaf=10,
                                random_state=42, class_weight="balanced")

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
oof_proba = cross_val_predict(model, X, y, cv=cv, method="predict_proba")[:, 1]

model.fit(X, y)
importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)

predictions_df = df[["case_id", "seizure_date", "origin_country", "destination_country",
                      "species", "product_type", "estimated_value_usd",
                      "enforcement_agency", "case_status", "arrest_made"]].copy()
predictions_df["predicted_arrest_probability"] = np.round(oof_proba, 4)
predictions_df["predicted_arrest"] = (oof_proba >= 0.5).astype(int)

feature_importance_df = importances.reset_index()
feature_importance_df.columns = ["feature", "importance"]
