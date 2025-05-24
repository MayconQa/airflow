from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import statistics as sts

dag = DAG(
<<<<<<< HEAD
    'pythonOperator',
    description="pythonOperator",
=======
    'python-operator',
    description="Python Operator",
>>>>>>> 88fc376 (subindo o projeto inteiro)
    schedule_interval=None,
    start_date=datetime(2025, 4, 10),
    catchup=False
)

def data_cleaner():
    dataset = pd.read_csv('/opt/airflow/data/Churn.csv', sep=';')
    dataset.columns = ['Id', 'Score', 'Genero','Estado', 'Idade', 'Patrimonio', 'Saldo', 'Produtos', 'TemCartCredito', 'Ativo', 'Salario', 'Saiu']

<<<<<<< HEAD
    mediana = sts.median(dataset['Salario'].dropna())
=======
    mediana = sts.median(dataset['Salario'])
>>>>>>> 88fc376 (subindo o projeto inteiro)
    dataset['Salario'].fillna(mediana, inplace=True)

    dataset['Genero'].fillna('Masculino', inplace=True)

    mediana = sts.median(dataset['Idade'])
    dataset.loc[(dataset['Idade'] < 0) | (dataset['Idade'] > 120), 'Idade'] = mediana

    dataset.drop_duplicates(subset='Id', keep='first', inplace=True)

    dataset.to_csv('/opt/airflow/data/Churn_clean.csv', sep=';', index=False)

# Task fora da função!
t1 = PythonOperator(
<<<<<<< HEAD
    task_id='data_clean_task',
    python_callable=data_cleaner,
    dag=dag
)
=======
    task_id='t1',
    python_callable=data_cleaner,
    dag=dag)
>>>>>>> 88fc376 (subindo o projeto inteiro)
t1