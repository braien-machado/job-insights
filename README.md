
# Jobs Insights
In this project I implemented analyzes from a dataset about jobs. Implementations are built into a web application powered by Flask (a very popular web framework in the Python community). I also had the opportunity to write tests for implementing a data analysis. Finally, as a bonus, I was challenged to write a route and view for a new feature using Flask!

## Sumary
- [Description](#jobs-insights)
- [Explanations](#explanations)
- [Getting started](#getting-started)
- [Tests](#tests)
- [Web Page](#web-page)

## Explanations
This project was carried out during the computer science module of the Trybe full stack web development course and, therefore, it is necessary to clarify what was done by me and what was done by the institution.
- Provided by Trybe
	- Images
	- Setup files
	- Docker related files
	- Templates
	- `app.py`, `counter.py`, `brazilian_jobs.py`, `sorting.py` `jobs.csv`, `more_insights.py`, all functions from `routes_and_views` but `job(index)` and route `"/job/<index>"` setup.
- Developed during project
	- Tests for `brazilian_jobs.py`, `counter.py` and `sorting.py`
	- `insights.py` and `jobs.py`
	- Implementation of route `"/job/<index>"` with flask

## Getting Started
1. Clone the repository
-  `git clone git@github.com:braien-machado/job-insights.git`

 2. Go to the cloned repository
-  `cd job-insights`
 
 3. Create the virtual environment to the project
 -   `python3 -m venv .venv && source .venv/bin/activate`

4.   Install the dependencies

-   `python3 -m pip install -r dev-requirements.txt`

## Tests
To execute tests, run
- `python3 -m pytest`

## Web Page
1. Run **Flask**
- `flask run`
2. Access **localhost:5000**
- `http://localhost:5000/jobs`
