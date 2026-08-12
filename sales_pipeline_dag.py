from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='sales_analytics_pipeline',
    start_date=datetime(2026, 1, 1),
    schedule='@daily',
    catchup=False
) as dag:

    transform = BashOperator(
        task_id='transform_sales_data',
        bash_command='python ~/Desktop/real-time-sales-analytics-pipeline/etl/transform.py'
    )

    transform
