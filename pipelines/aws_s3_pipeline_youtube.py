from etls.aws_etl_youtube import connect_to_s3,create_bucket_if_not_exist,upload_to_s3
from utils.constants_v2 import AWS_BUCKET_NAME

def upload_s3_pipeline(ti):
    file_path = ti.xcom_pull(task_ids = 'youtube_extration', key='return_value')
    # file_path ='/opt/airflow/data/output'
    s3 = connect_to_s3()

    create_bucket_if_not_exist(s3, AWS_BUCKET_NAME)
    upload_to_s3(s3, file_path,AWS_BUCKET_NAME)

    return file_path

    