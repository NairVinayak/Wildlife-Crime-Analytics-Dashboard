# 🐾 AI Wildlife Crime Analytics Dashboard

**Data-driven analysis of wildlife crime trends, hotspots, and conservation insights.**

## Overview

This Power BI dashboard analyzes 950 wildlife crime seizure records (2015–2024) to surface patterns in 
illegal wildlife trafficking — which species and products are most trafficked, where seizures happen, 
how enforcement outcomes play out, and how trafficking activity has shifted over the past decade.

The goal: turn raw seizure data into a story that's useful to conservation orgs, policymakers, or 
anyone trying to understand where enforcement resources are working — and where they aren't.

## Key Findings

- **$46.3M** in total estimated black-market value seized across 950 recorded incidents
- Trafficking activity dipped sharply during 2020–2021 (COVID-era travel restrictions) and has 
  **rebounded past pre-pandemic levels since 2022**
- **Horn and ivory dominate seizure value** ($22M and part of the top categories combined) despite 
  representing a smaller share of total seizure *counts* — high-value, lower-volume trafficking
- Only **20.1%** of cases result in conviction
- **294 cases (31%) closed with no arrest at all** — a significant accountability gap
- Seaports and international airports are the top two seizure locations, ahead of land borders and markets

## Dashboard Pages

### 1. Executive Overview
KPI summary (total seizures, value, arrests, conviction rate), yearly trend line, and species category breakdown.

### 2. Geographic Hotspots
Interactive map of origin countries by seizure volume, top-countries-by-value table, and seizure location type breakdown.

### 3. Species & Product Analysis
Treemap of product value (ivory, horn, scales, skins...), conservation-status heatmap, and average value per seizure by product.

### 4. Enforcement & Case Outcomes
Case status trends over time, agency-level seizure vs. arrest comparison, and a value-vs-arrests scatter plot by country.

### 5. Predictive Insights
A live Random Forest classifier (via Power BI's Python integration) tests whether seizure 
characteristics — value, product type, region, transport method, enforcement agency — predict 
arrest outcomes. Model performance was close to random (ROC-AUC 0.57), suggesting arrest 
likelihood depends on factors beyond seizure data alone — consistent with real-world patterns 
where investigative capacity and political will often matter more than case specifics. Feature 
importance analysis showed estimated seizure value and quantity as the strongest (though still 
weak) predictors.

## Tools Used

- **Power BI Desktop** — data modeling, DAX measures, dashboard design
- **DAX** — custom measures for conviction rate, YoY growth, and category-level breakdowns
- **Python (scikit-learn, pandas)** — Random Forest classifier for arrest prediction, connected 
  live via Power BI's Python scripting integration (see `ml/arrest_classifier.py`)
- **Excel / SQL** — used for initial data exploration and validation

## About the Dataset

The dataset (`wildlife_crime_seizures.csv`) is a **synthetic-but-realistic** dataset built to reflect 
genuine wildlife trafficking patterns — species mix, trafficking routes, seasonal trends, and a 
COVID-era dip — for portfolio and learning purposes. Real-world equivalents include the 
[CITES Trade Database](https://cites.org/eng/resources/trade-statistics), 
[C4ADS Wildlife Seizure Dashboard](https://wildlifedashboard.c4ads.org), and EIA wildlife trafficking reports.

## Files

- `dashboard.pbix` — the full Power BI file
- `data/wildlife_crime_seizures.csv` — source dataset
- `screenshots/` — page-by-page dashboard previews
