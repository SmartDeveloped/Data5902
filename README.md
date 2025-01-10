London Underground Quality Report

This project analyses the London Underground’s performance data from 2004 to 2017, covering various categories such as power failures, signal issues, and staff shortages. The objective is to identify trends and assess whether the quality of services has improved over the years, addressing the key question:
Has the London Underground’s service quality improved over time?

How to Run the Project

1. Clone the Repository

First, clone the repository to your local machine:

git clone https://github.com/SmartDeveloped/Data5902
cd Data5902

2. Install Dependencies

Ensure Python is installed on your system. Then, install the required dependencies:

pip install -r requirements.txt

The requirements.txt includes:
	•	pandas
	•	numpy
	•	pytest
	•	matplotlib
	•	scipy

3. Run the Main Script

To analyse the data and generate visualisations, run:

python analyse_data.py

This script will:
	•	Load and preprocess the dataset.
	•	Perform data analysis.
	•	Generate visualisations, including:
	•	Line graphs (for trends).
	•	Boxplots (for distributions).
	•	Linear regression plots (for relationships).

How to Test

Run the unit tests to validate the functionality of the project:

python test_analyse_data.py

Tests include:
	•	Loading and filtering the dataset.
	•	Generating line graphs, boxplots, and regression plots.
	•	Ensuring outputs align with expected results.

Results

This project provides a detailed analysis of London Underground performance data, offering insights through the following visualisations:

1. Line Graphs
	•	Track trends over time for categories like “Power Failure” and “Signals.”

2. Boxplots
	•	Compare distributions across categories over 12 years, highlighting variability and outliers.

3. Linear Regression
	•	Examine relationships, such as between “Staff Absence” and “London Underground Operations,” to identify underlying patterns.

These findings offer valuable perspectives on the effectiveness of investments in maintaining and improving the London Underground.

Contributors
	•	Timothy Smart Omoruyi

