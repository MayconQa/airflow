from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

def print_result(ti):
    task_instance = ti.xcom_pull(task_ids='query_data')
    print('Resultado da Consulta:')
    for row in task_instance:
        print(row)

with DAG(
    dag_id='banco-de-dados',
    description="banco-de-dados",
    schedule=None,
    start_date=datetime(2025, 4, 10),
    catchup=False,
) as dag:

    create_table = PostgresOperator(
        task_id="create_table",
        postgres_conn_id='postgres',
        sql='CREATE TABLE IF NOT EXISTS teste(id INT);'
    )

    insert_dados = PostgresOperator(
        task_id="insert_dados",
        postgres_conn_id='postgres',
        sql='INSERT INTO teste VALUES (1);'
    )

    query_data = PostgresOperator(
        task_id="query_data",
        postgres_conn_id='postgres',
        sql='SELECT * FROM teste;',
        do_xcom_push=True  # necessário para puxar o resultado no PythonOperator
    )

    print_result_task = PythonOperator(
        task_id='print_result_task',
        python_callable=print_result,
    )

    create_table >> insert_dados >> query_data >> print_result_task
