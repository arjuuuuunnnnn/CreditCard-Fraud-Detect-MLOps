import dagshub
dagshub.init(repo_owner='arjuuuuunnnnn', repo_name='CreditCard-Fraud-Detect-MLOps', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)
