from data_ingestion import create_data
from create_model import train_model
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# default arguments - owner other details
default_args = {
        'owner': 'kkn',
        'start_date':datetime(2025,10, 9)
}
dag = DAG('ml_pipeline',default_args=default_args,schedule_interval=None)
data_op = PythonOperator(
    task_id = 'data',
    python_callable = create_data,
    dag = dag
)
train_op = PythonOperator(
    task_id = 'model',
    python_callable = train_model,
    dag = dag
)
# now we need define the dependency - which order the code will execute
data_op >> train_op # 1st data operation then train operation
