AI Lead Scoring Agent
Live Demo Application:(https://leadscoringagent-qxe6hfdp3ufj9cdahudbmg.streamlit.app/)

#Project Overview
This project is an AI-powered Sales Agent designed to identify, enrich, and rank potential B2B leads. 
It automates the process of finding the "perfect customer" by analyzing data points like Job Title, Company Funding, and Scientific Activity.

The tool processes a list of 500+ potential candidates and assigns a "Propensity to Buy" score (0-100) to help Business Development teams prioritize their outreach.

Key Features
* Automated Scoring Engine: Ranks leads based on weighted criteria (Role Fit, Funding, Tech Stack).
* Real-time Filtering: Instantly filter by Probability Score, Funding Status (Series A/B), or Keywords.
* Data Simulation: Generates 500+ realistic mock profiles (simulating LinkedIn/Crunchbase data) to demonstrate scalability.
* Export Ready: Download the prioritized list as a CSV for immediate use.

Installation & Setup
To run this project locally, follow these steps:

1. Clone the Repository
   git clone (https://github.com/UnnatiShinganjude/lead-scoring-agent.git)
   cd lead-scoring-agent


2.Create a Virtual Environment
  python -m venv venv
  source venv/bin/activate  # On Windows use: venv\Scripts\activate


3.Install Dependencies
  pip install -r requirements.txt


4.Run the Application
  streamlit run app.py

Project Structure
This project is modularized for readability and scalability:

app.py: The main entry point containing the Streamlit Dashboard UI.

scoring_logic.py: The core algorithm that calculates the "Propensity to Buy" score.

data_generator.py: Generates realistic mock data (Names, Companies, Locations) for testing.

requirements.txt: List of Python dependencies.

👤 Author
Unnati Shinganjude

Role: AI Engineer Intern Applicant

Focus: Building intelligent data pipelines and user-friendly web agents.

Submitted as part of the EuPrime Internship Assessment.

