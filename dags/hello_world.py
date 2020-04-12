from pprint import pprint

import airflow.utils.dates
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

dag = DAG(
    dag_id="hello_world",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval="@daily",
)


def _python_context(**context):
    pprint(context)


hello = BashOperator(task_id="hello", bash_command="echo 'hello'", dag=dag)
world = PythonOperator(task_id="world", python_callable=lambda: print("world"), dag=dag)

hello >> world
