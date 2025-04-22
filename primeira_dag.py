from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG(
    dag_id='peimeira_dag', description="Minha primeira Dag",
    schedule_interval=None,
    start_date=datetime(2025,4,10),
    catchup=False)

task1 = BashOperator(task_id="tsk1", bash_command="sleep 5", dag=dag)
task2 = BashOperator(task_id="tsk2", bash_command="sleep 5", dag=dag)
task3 = BashOperator(task_id="tsk3", bash_command="sleep 5", dag=dag)


task1 >> task2 >> task3

# ) as dag:    # <- Add "as dag" here
#     start = EmptyOperator(task_id='start')
#     hello = BashOperator(task_id="hello", bash_command='echo "hello world"', dag=dag)  # <- Change DAG to dag
#     end = EmptyOperator(task_id='end')

# (start >> hello >> end)
