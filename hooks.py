from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime

def create_table():
    pg_hook = PostgresHook(postgres_conn_id='postgres')
    pg_hook.run('CREATE TABLE IF NOT EXISTS teste2(id INT);', autocommit=True)

def insert_data():
    pg_hook = PostgresHook(postgres_conn_id='postgres')
    pg_hook.run('INSERT INTO teste2 VALUES (1);', autocommit=True)

def select_data(**kwargs):
    pg_hook = PostgresHook(postgres_conn_id='postgres')
    records = pg_hook.get_records('SELECT * FROM teste2;')  # Melhor para select
    kwargs['ti'].xcom_push(key='query_result', value=records)

def print_data(**kwargs):
    task_instance = kwargs['ti'].xcom_pull(key='query_result', task_ids='select_data_task')
    print('Dados da tabela:')
    for row in task_instance:
        print(row)

with DAG(
    dag_id='hook',
    description="hook",
    schedule_interval=None,  # schedule -> schedule_interval
    start_date=datetime(2025, 4, 10),
    catchup=False,
) as dag:

    create_table_task = PythonOperator(
        task_id='create_table_task',
        python_callable=create_table
    )

    insert_data_task = PythonOperator(
        task_id='insert_data_task',
        python_callable=insert_data
    )

    select_data_task = PythonOperator(
        task_id='select_data_task',
        python_callable=select_data,
        provide_context=True
    )

    print_data_task = PythonOperator(
        task_id='print_table_task',
        python_callable=print_data,
        provide_context=True
    )

    create_table_task >> insert_data_task >> select_data_task >> print_data_task
