Solar Challenge Week 1
This repository contains the setup for the Solar Challenge Week 1 project. It includes a Python virtual environment setup, a GitHub Actions CI pipeline, and a structured project layout.
Project Structure
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
├── notebooks/
│   ├── __init__.py
│   └── README.md
├── tests/
│   ├── __init__.py
├── scripts/
│   ├── __init__.py
│   └── README.md

Setup Instructions

Clone the Repository
git clone https://github.com/your-username/solar-challenge-week1.git
cd solar-challenge-week1


Set Up Python Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


Verify Setup

Ensure the dependencies listed in requirements.txt are installed.
Run python --version to confirm the Python version.


Run Tests (Optional)

Tests can be added to the tests/ directory and executed as needed.



Development Workflow

Create a new branch for your work: git checkout -b feature/your-feature.
Commit changes with clear messages, e.g., git commit -m "feat: add new feature".
Push changes to GitHub and create a Pull Request to merge into main.

CI Pipeline

A GitHub Actions workflow (.github/workflows/ci.yml) runs on every push and pull request to main or setup-task branches.
It sets up Python, installs dependencies, and checks the Python version.

