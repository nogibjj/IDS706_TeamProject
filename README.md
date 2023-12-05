# ICU Data Service Microservice
[![Python CI](https://github.com/nogibjj/IDS706_TeamProject/actions/workflows/python_app_cicd.yml/badge.svg)](https://github.com/nogibjj/IDS706_TeamProject/actions/workflows/python_app_cicd.yml)

## Team Members

Linke Li (ll442), Yang Xu (yx248), Yunjia Liu (yl794), and Zhichen Guo (zg105)

## Overview
This project is a FastAPI microservice designed to provide information on ICU beds in various Metropolitan and Micropolitan Statistical Areas (MMSA). It includes a data pipeline, load testing, data engineering, and CI/CD integrations, developed using Python.

## Features
- **Microservice for ICU Data**: Provides ICU-related information for specified MMSAs.
- **Data Engineering**: Utilizes a MySQL database to manage ICU data.
- **Load Testing**: Ensures handling of high request volumes.
- **Continuous Integration and Continuous Delivery**: Automated using GitHub Actions.

## Technologies
- Python
- FastAPI
- MySQL
- Docker
- pytest for testing

## Setup and Installation
1. **Clone the repository**:
git clone https://github.com/nogibjj/IDS706_TeamProject.git
2. **Install Dependencies**:
make install


## Running the Application
- **Locally**: python app.py
- **Using Docker**:
docker build -t icu-data-service .
docker run -p 8080:8080 icu-data-service

## Endpoints
- `/`: Welcome message
- `/icu_info/{MMSA}`: ICU info for a specified MMSA
- `/hospitals_info`: Summary info about hospitals which has more than 5 icu beds

## Database Setup
Refer to `schema.sql` for the database schema. The data from `mmsa-icu-beds.csv` should be imported into the database as per this schema.

## File Descriptions
- `app.py`: FastAPI application
- `test_app.py`: Tests for FastAPI endpoints
- `mmsa-icu-beds.csv`: Data file with ICU bed information
- `schema.sql`: SQL schema for the ICU data
- `dblib/dbquery.py`: Database query utility
- `Makefile`: Contains commands for setting up the environment, testing, linting, and formatting
- `Dockerfile`: For containerizing the application

## CI/CD
CI/CD is implemented using GitHub Actions for automated testing and deployment.

