# AURA

AI-powered trend intelligence platform that discovers emerging trends, analyzes signals using AI, stores insights in a database, and tracks experiments for future research and forecasting.

---

## Overview

AURA is a multi-agent intelligence system being built to discover, analyze, and forecast trends.

The first completed component is the **Trend Scout Agent**, which:

* Collects Google Trends data
* Detects emerging or declining trends
* Uses AI to generate insights
* Stores results in Supabase
* Tracks experiments using Weights & Biases (W&B)

The long-term vision is to build a complete intelligence platform with multiple specialized AI agents working together.

---

## Features
### Trend Scout Agent (Phase 1)

✅ Google Trends Data Collection

✅ Trend Detection Engine

✅ 7-Day Trend Comparison

✅ AI-Powered Analysis (Groq + Llama)

✅ JSON Report Generation

✅ Supabase Database Storage

✅ Weights & Biases Experiment Tracking

✅ One-Command Pipeline Execution

---

## Architecture

Google Trends

↓

Trend Collector

↓

Trend Detector

↓

Groq AI Analysis

↓

JSON Reports

↓

Supabase Database

↓

W&B Experiment Tracking

---

## Tech Stack

### Backend

* Python

### Data Processing

* Pandas

### AI Model

* Groq
* Llama 3

### Database

* Supabase

### Experiment Tracking

* Weights & Biases (W&B)

### Version Control

* Git
* GitHub

---

## Project Structure

```text
AURA/

├── data/
│   ├── google_trends.csv
│   ├── trend_report.json
│   └── analysis_report.txt
│
├── src/
│   ├── google_trends_collector.py
│   ├── trend_detector.py
│   ├── trend_analyst.py
│   ├── save_to_supabase.py
│   └── run_trend_scout.py
│
├── .env
├── .gitignore
└── README.md
```

## How To Run

Activate virtual environment:

```bash
source .venv/bin/activate
```

Run the full pipeline:

```bash
python run_trend_scout.py
```

The pipeline will:

1. Collect Google Trends data
2. Detect trend changes
3. Generate AI analysis
4. Save results to Supabase
5. Log experiment metrics to W&B

---

## Current Progress

### Phase 1 — Trend Scout

* [x] Data Collection
* [x] Trend Detection
* [x] AI Analysis
* [x] Supabase Integration
* [x] W&B Integration
* [x] One-Command Pipeline

### Phase 2 — Sentiment Analyst

* [ ] News Collection
* [ ] Sentiment Detection
* [ ] Sentiment Database Storage

### Phase 3 — Cultural Radar

* [ ] Cultural Event Detection
* [ ] Signal Extraction
* [ ] Impact Scoring

### Phase 4 — Forecast Synthesizer

* [ ] Multi-Agent Coordination
* [ ] Forecast Generation
* [ ] Confidence Scoring

---

## Future Vision

AURA aims to evolve into a full multi-agent intelligence platform capable of:

* Trend Discovery
* Sentiment Analysis
* Cultural Signal Detection
* Forecasting
* Research Experimentation
* Executive Intelligence Reporting

---

## Author

Vaani Singh


