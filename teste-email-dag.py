from airflow import DAG
from airflow.operators.email import EmailOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
}

with DAG(
    dag_id='test_email_dag',
    default_args=default_args,
    schedule_interval=None,  # Só executa manualmente
    catchup=False,
    description='Testa envio de e-mail com EmailOperator',
) as dag:

    send_email = EmailOperator(
        task_id='send_test_email',
        to='mayconfabrcio2009@gmail.com',  # Pode colocar mais de um separado por vírgula
        subject='✅ Teste de e-mail com Airflow',
        html_content="""
        <h3>Funcionou!</h3>
        <p>Este é um teste de envio de e-mail usando Airflow + Gmail SMTP.</p>
        """,
    )
