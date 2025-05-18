**Solar Challenge Week 1**

This repository contains the setup for the Solar Challenge Week 1 project. It includes a Python virtual environment configuration, a GitHub Actions CI pipeline, and a structured project layout.

**Project Structure**

    ├── .vscode/
    
      └── settings.json
    
    ├── .github/
    
      └── workflows/
    
      └── ci.yml
    
    ├── .gitignore
    
    ├── requirements.txt
    
    ├── README.md
    
    ├── src/
    
    ├── notebooks/
    
      ├── __init__.py
    
      └── README.md
    
    ├── tests/
    
      ├── __init__.py
    
    ├── scripts/
    
       ├── __init__.py
    
       └── README.md

**Setup Instructions**

    Clone the Repository
    git clone https://github.com/YishakG/solar-challenge-week1.git
    
    cd solar-challenge-week1
    
    Set Up Python Virtual Environment
    
    Create a virtual environment:
         python -m venv venv
    
    
    Activate the virtual environment:
    
        On Linux/MacOS:
          source venv/bin/activate
    
    
        On Windows:
          venv\Scripts\activate
    
    
    Install dependencies:
      pip install -r requirements.txt


**Verify Setup**

    Ensure all dependencies listed in requirements.txt are installed.
    
    Verify the Python version:
      python --version



**Run Tests (Optional)**
    
    Tests can be added to the tests/ directory and executed as needed.
    
**Development Workflow**

    Create a new branch for your work:
      git checkout -b feature/your-feature
    
    
    Commit changes with clear messages:
        git commit -m "feat: add new feature"
    
    
    Push changes to GitHub and create a Pull Request to merge into the main branch.
    
    
CI Pipeline

    A GitHub Actions workflow (.github/workflows/ci.yml) runs on every push and pull request to the main or setup-task branches.It:
       
        Sets up the Python environment.
        Installs dependencies from requirements.txt.
        Verifies the Python version.
    
