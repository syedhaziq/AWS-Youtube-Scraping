import s3fs
from utils.constants_v2 import AWS_ACCESS_KEY,AWS_ACCESS_KEY_ID,AWS_ACCESS_TOKEN
import os

def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(
            anon= False,
            key= AWS_ACCESS_KEY_ID,
            secret= AWS_ACCESS_KEY
            
        )

        print('connected successfully to s3')
        return s3
    except Exception as e:
        print(e)

def create_bucket_if_not_exist(s3, bucket):
    try:
        if not s3.exists(bucket):
            s3.mkdir(bucket)

            print("bucket created successfully")
        else:
            print("bucket already exist")
    except Exception as e:
        print(e)

def upload_to_s3(s3, file_path,bucket):
    try:
        # file_name=[]
        # for file in os.listdir(file_path):
        #     file_name.append(file)
        # return file_name   

        for file in os.listdir(file_path):
            destination_path = os.path.join(bucket,'raw/',file)
            
            source_path = os.path.join(file_path,file)
            print(source_path)
            print(f'destination is {destination_path}')
            s3.put(source_path, destination_path)
            print('file uploaded successfully')

    except Exception as e:
        print(e)