# End-to-End-MLOps-Project: Wine Quality Prediction

This repository demonstrates a complete end-to-end MLOps workflow for a **Wine Quality Prediction** web application. The project covers all stages of the machine learning lifecycle, from data ingestion and validation to model training, evaluation, deployment, and CI/CD automation.

## Features

- **Data Ingestion:** Downloads and unzips the wine quality dataset automatically.
- **Data Validation:** Ensures data schema and integrity before processing.
- **Data Transformation:** Splits data into training and testing sets.
- **Model Training:** Trains an ElasticNet regression model to predict wine quality.
- **Model Evaluation:** Evaluates model performance and logs metrics to MLflow (integrated with DagsHub).
- **Prediction API:** Flask web app for real-time wine quality prediction based on user input.
- **Experiment Tracking:** Uses MLflow for experiment tracking and model registry.
- **CI/CD Pipeline:** Automated workflows using GitHub Actions for building, testing, and deploying the application.
- **Docker & AWS Ready:** Instructions and scripts for containerization and deployment on AWS EC2/ECR.

## Tech Stack

- Python (Flask, scikit-learn, pandas, numpy)
- MLflow & DagsHub (experiment tracking)
- GitHub Actions (CI/CD)
- Docker (containerization)
- AWS EC2 & ECR (cloud deployment)
- HTML/CSS/Bootstrap (frontend)

## Project Structure

```
├── config/                # YAML configuration files
├── src/mlopsProject/      # Core Python package (pip installable)
│   ├── pipeline/          # Training and prediction pipelines
│   ├── utils/             # Utility functions (YAML, JSON, logging, etc.)
│   └── ...                # Other modules
├── research/              # Jupyter notebooks for each pipeline stage
├── artifacts/             # Generated artifacts (data, models, logs)
├── static/                # Static assets (CSS, JS, images)
├── templates/             # HTML templates for Flask app
├── app.py                 # Flask web application
├── main.py                # Pipeline runner script
├── requirements.txt       # Python dependencies
├── .github/workflows/     # GitHub Actions CI/CD workflows
└── README.md              # Project documentation
```

## How to run?
### STEPS:

Clone the repository

```bash
https://github.com/sudhanvabharadwaj/End-to-End-MLOps-Project
```
#### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlopsproj python=3.8 -y
```

```bash
conda activate mlopsproj
```


#### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
Open up your local host and port.
```

## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=<URI> \
MLFLOW_TRACKING_USERNAME=<username> \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=[URI]

export MLFLOW_TRACKING_USERNAME=[Username]

```

## AWS-CI/CD-Deployment-with-Github-Actions

### 1. Login to AWS console.

### 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
### 3. Create ECR repo to store/save docker image
    - Save the URI: 905418092965.dkr.ecr.eu-north-1.amazonaws.com/mlopsproj

	
### 4. Create EC2 machine (Ubuntu) 

### 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optional

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
### 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


### 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app