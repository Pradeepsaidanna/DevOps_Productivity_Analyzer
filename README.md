# DevOps Team Productivity and Bottleneck Analyzer

This project analyzes GitHub development and deployment metrics to identify productivity bottlenecks and suggest actionable improvements. It collects pull request data, calculates workflow durations, detects delays, and visualizes insights through an interactive dashboard.

## Objectives

- Analyze software team productivity using GitHub PR data
- Detect bottlenecks in the development lifecycle
- Suggest areas for improvement using workflow trends
- Provide visual analytics via Streamlit

## Key Features

- GitHub PR data fetching using GitHub REST API
- Duration computation from PR created-to-closed timestamps
- Modular scripts for data collection and analysis
- Streamlit-based dashboard for data visualization
- Clean code structure for extension and deployment

## Technologies Used

- Python
- Pandas
- Requests
- Streamlit
- GitHub API

## Folder Structure

```
DevOpsAnalyzer/
├── data/                         # Stores fetched and processed CSVs
├── scripts/                      # Python scripts for fetch and analysis
│   ├── fetch_github.py
│   └── analyze_workflow.py
├── dashboard/
│   └── app.py                    # Streamlit app
├── requirements.txt
└── README.md
```

## How It Works

1. `fetch_github.py` pulls PR data using GitHub API and saves to `data/github_prs.csv`
2. `analyze_workflow.py` calculates duration of each PR and saves to `data/github_prs_with_duration.csv`
3. `app.py` visualizes PR metrics and bottlenecks in a Streamlit dashboard

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/YourUsername/DevOps_Productivity_Analyzer.git
cd DevOps_Productivity_Analyzer
```

2. Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set GitHub repo and token in `fetch_github.py`, then run:
```bash
python scripts/fetch_github.py
python scripts/analyze_workflow.py
```

5. Launch dashboard:
```bash
streamlit run dashboard/app.py
```

## Output Files

- `data/github_prs.csv` — raw pull request data
- `data/github_prs_with_duration.csv` — processed data with PR durations

## License

This project is licensed under the MIT License.
