## MLOPS project

### Workflow
1. config.yaml
2. schema.yaml
3. params.yaml
4. entity
5. config manager in src config
6. components
7. pipeline
8. main.py
9. app.py

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/arjuuuuunnnnn/CreditCard-Fraud-Detect-MLOps.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cred python=3.8 -y
```

```bash
conda activate cred
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

# Finally run the following command
```bash
python app.py
```

### dagshub
```bash
import dagshub
dagshub.init(repo_owner='arjuuuuunnnnn', repo_name='CreditCard-Fraud-Detect-MLOps', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)
```
