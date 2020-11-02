"""
DAG is implemented to orchestrate the workflow for below task
   1. Capture S3 website endpoint GET response and write to S3 as JSON file.
   2. Transform the response and write to S3 as CSV
Function upload_to_S3hk is called using Python Operator

"""



# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

# Datetime and other 
from datetime import datetime
import boto3, json
import requests
import pandas as pd

# Importing airflow hook
from airflow.contrib.hooks.aws_lambda_hook import AwsLambdaHook
import airflow.hooks.S3_hook






# Default arguments and can be overwritten at operator initialization
default_args = {
        'owner': 'Vijayreddy',
        'depends_on_past': False,
        'start_date': datetime(2020,10,31),
        'email': ['@gmail.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 0,
}



# Function

def upload_to_S3hk(**kwargs):
    hook = airflow.hooks.S3_hook.S3Hook('my_lambda')
    resp = requests.get('http://engineering-exam.s3-website.ap-southeast-2.amazonaws.com/')
    hook.load_string(resp.text, kwargs['key1'], kwargs['bucket_name'])
    content = resp.json()
    asset_data = content['payload'] 
    df = pd.DataFrame(asset_data)
    df = df.explode('seasons')
    data = df.to_csv()
    hook.load_string(data, kwargs['key2'], kwargs['bucket_name'])


# Using the context manager alllows you not to duplicate the dag parameter in each operator

with DAG('webresponce_json_s3', default_args=default_args, description='uploading the s3 web endpoint responce as JSON') as dag:

    start = DummyOperator(task_id='Begin_execution_hook')

    t1 = PythonOperator(
                        task_id="response_json_upload_hook",
                        python_callable=upload_to_S3hk,
                        op_kwargs={'key1': 'asset/asset1.json','bucket_name': 'vijaytest12','key2': 'asset_transformed/asset1.csv'},
                        provide_context=True
                    )

   
    end = DummyOperator(task_id='stop_execution_hook')


start >> t1 >> end  
