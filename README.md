# End-to-End-MLOps-Project

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