from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago
from operators import Multiplicate  # Stellen Sie sicher, dass Sie Ihre eigenen Modul importieren

# Definieren Sie die DAG und legen Sie ihre Einstellungen fest
dag = DAG(
    'multiply_numbers',
    schedule_interval=None,  # Legen Sie die Ausführungszeitpläne fest
    start_date=days_ago(1),
    catchup=False,
)

# DummyOperator als Startpunkt
start = DummyOperator(task_id='start', dag=dag)

# Definieren Sie die Zahlen, die multipliziert werden sollen
num1 = 5
num2 = 7

# Verwenden Sie den Multiplicate Operator, um die Zahlen zu multiplizieren
multiply_task = Multiplicate(
    task_id='multiply_numbers',
    num1=num1,
    num2=num2,
    dag=dag,
)

# DummyOperator als Endpunkt
end = DummyOperator(task_id='end', dag=dag)

# Definieren Sie die Ausführungsreihenfolge der Aufgaben
start >> multiply_task >> end
