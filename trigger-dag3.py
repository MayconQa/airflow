from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


dag = DAG('trigge-dag3', description="Trigger 3 DAG", 
           schedule_interval=None, 
           start_date=datetime(2025, 4, 10),
           catchup=False)


task1 = BashOperator(task_id='tsk1', bash_command='exit 1', dag=dag) 
task2 = BashOperator(task_id='tsk2', bash_command='exit 1', dag=dag)
task3 = BashOperator(task_id='tsk3', bash_command='sleep 5', dag=dag,
            trigger_rule='all_failed')


[task1, task2] >> task3