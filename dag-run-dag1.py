from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.operators.dagrun_operator import TriggerDagRunOperator

dag = DAG('dag-run-dag1', description="Dag RUN DAG1", 
           schedule_interval=None, 
           start_date=datetime(2025, 4, 10),
           catchup=False)

task1 = BashOperator(task_id='tsk1', bash_command='sleep 5', dag=dag) 
task2 = TriggerDagRunOperator(task_id='tsk2', trigger_dag_id="dag-run-dag2", dag=dag)


task1 >> task2 

<<<<<<< HEAD
=======






>>>>>>> 88fc376 (subindo o projeto inteiro)
