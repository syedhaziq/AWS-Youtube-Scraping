############## importing libraries ##############
import sys
import os

from airflow import DAG
from airflow.operators.python import PythonOperator
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pipelines.youtube_pipeline import youtube_extration
from pipelines.aws_s3_pipeline_youtube import upload_s3_pipeline

from datetime import datetime




###### Defining dag structure #############



default_args = {
    'owner': 'Haziq',
    'start_date': datetime(2024, 9,  29)  # type: ignore
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id = 'youtube_pipeline',
    default_args = default_args,
    schedule_interval = '@daily',
    catchup = False,
    tags = ['youtube','etl','pipeline']
)

######## Extraction from reddit ##########

extract = PythonOperator(
    task_id = 'youtube_extration',
    python_callable= youtube_extration,
    # op_kwargs = {
    #     'file_name': f'reddit_{file_postfix}',
    #     'subreddit': 'dataengineering',
    #     'time_filter': 'day',
    #     'limit': 100
    # },
    dag=dag
)

# ####### upload to s3 ##################

upload_s3 = PythonOperator(
    task_id = 's3_upload',
    python_callable= upload_s3_pipeline,
    dag=dag
)

extract >> upload_s3
