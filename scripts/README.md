# Scripts Directory

This directory contains scripts and documentation for the Streamlit dashboard development.

## Development Process
- Created `dashboard-dev` branch to isolate dashboard work.
- Set up folder structure: `app/` for Streamlit app, `scripts/` for documentation.
- Developed `app/main.py` with a basic UI: country selection widget, GHI boxplot, and top regions table.
- Added utility functions in `app/utils.py` for data loading and plotting.

## Usage Instructions
1. Ensure dependencies are installed: `pip install -r requirements.txt`.
2. Run the app: `streamlit run app/main.py`.
3. Select countries from the dropdown to view the GHI boxplot and top regions table.