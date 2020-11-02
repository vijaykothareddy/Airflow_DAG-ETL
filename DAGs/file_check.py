"""
DAG is implemented to self check S3 for the existence of
uploaded files

Function file_check_S3hk is called using Python Operator
returns TRUE if the file exists

"""



# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator


# Datetime and other 
from datetime import datetime
import boto3, logging

# Importing airflow hook
from airflow.contrib.hooks.aws_lambda_hook import AwsLambdaHook
import airflow.hooks.S3_hook

# Default arguments and can be overwritten at operator initialization
default_args = {
        'owner': 'kotharv',
        'depends_on_past': False,
        'start_date': datetime(2020,10,31),
        'email': ['@gmail.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 0,
}

# Function

def file_check_S3hk(**kwargs):
    log = logging.getLogger(__name__)
    hook = airflow.hooks.S3_hook.S3Hook('my_lambda')
    log.info('Poking for key : s3://%s/%s', kwargs['bucket_name'], kwargs['key'])
    return hook.check_for_key(kwargs['key'], kwargs['bucket_name'])

# Using the context manager alllows you not to duplicate the dag parameter in each operator

with DAG('s3_file_check', default_args=default_args, description='check the uploaded file exists') as dag:

    start = DummyOperator(task_id='Begin_execution_hook')

    t1 = PythonOperator(
                        task_id="file_check",
                        python_callable=file_check_S3hk,
                        op_kwargs={'key': 'asset_transformed/asset1.csv','bucket_name': 'nyc-raw-data'},
                        provide_context=True
                    )

   
    


start >> t1 
