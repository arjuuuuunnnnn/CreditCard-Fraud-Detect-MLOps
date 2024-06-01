# A MLOps Project uses MLFlow, Dagshub

Used to track, evaluate models

## Usage:
clone the repo
```bash
git clone https://github.com/arjuuuuunnnnn/CreditCard-Fraud-Detect-MLOps.git
```

### create env 
```bash
conda create -n cred python=3.8 -y
```
### activate env
```bash
conda activate cred
```


### install requirements
```bash
pip install -r requirements.txt
```

### Finally
```bash
python main.py
```

### Dagshub uri:
[https://dagshub.com/arjuuuuunnnnn/CreditCard-Fraud-Detect-MLOps](https://dagshub.com/arjuuuuunnnnn/CreditCard-Fraud-Detect-MLOps)

### dagshub config
Place this somewhere in the model evaluation file

```bash
import dagshub
dagshub.init(repo_owner='arjuuuuunnnnn', repo_name='CreditCard-Fraud-Detect-MLOps', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)
```

### Any bugs?
Feel free to open an issue
