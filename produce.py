from airflow import DAG
from airflow import Dataset
from airflow.operators.python import PythonOperator
<<<<<<< HEAD
import pandas as pd 
from datetime import datetime

mydataset = Dataset('/opt/airflow/data/Churn_new.csv')  # Corrigido aqui

dag = DAG(
    'consumer',
    description="consumer",
    schedule=[mydataset],
    start_date=datetime(2025, 4, 10),
    catchup=False
)

def my_file():
    dataset = pd.read_csv('/opt/airflow/data/Churn.csv', sep=';')
    dataset.to_csv('/opt/airflow/data/Churn_new2.csv', sep=";") 

t1 = PythonOperator(task_id='t1', python_callable=my_file, dag=dag)
=======
from datetime import datetime
import pandas as pd

dag = DAG(
    'procedure',
    description="procedure",
    schedule_interval=None,
    start_date=datetime(2025, 4, 10),
    catchup=False)

mydataset = Dataset('/opt/airflow/data/Churn_new.csv')

def my_file():
    dataset = pd.read_csv('/opt/airflow/data/Churn.csv', sep=";")
    dataset.to_cvs('/opt/airflow/data/Churn_new.csv', sep=";")

t1 = PythonOperator(
     task_id='t1', 
     python_callable=my_file,
     dag=dag,
     outlets=[mydataset])
t1
>>>>>>> 88fc376 (subindo o projeto inteiro)
