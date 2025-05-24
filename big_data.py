from airflow import DAG
from datetime import datetime
from big_data_operator import BigDataOperator

with DAG(
    dag_id='big-data',
    description="bigdata",
    schedule_interval=None,  # Correto
    start_date=datetime(2025, 4, 10),
    catchup=False
) as dag:

    big_data = BigDataOperator(
        task_id="big_data",
        path_to_csv_file='/opt/airflow/data/Churn.csv',
        path_to_save_file='/opt/airflow/data/Churn_new.json',
        file_type='json'
    )

    big_data  # Não tem problema deixar assim: Airflow entende a DAG pelo contexto.
