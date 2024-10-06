# AWS-Youtube-Scraping

## Overview

This project is a data pipeline designed to Extract, Transform, and Load (ETL) data from any YouTube channel. It allows you to analyze and visualize channel data to gain insights into its performance.

## Architecture

![My Architecture](https://raw.githubusercontent.com/syedhaziq/AWS-Youtube-Scraping/refs/heads/main/youtube%20dasboard.png)

## Data Flow

- Data Extration:
    - youtube_etl.py:
        - This script utilizes the YouTube Data API to retrieve data from the MrBeast (can be change to some other) channel.
        - It extracts information such as:
            - Video-level data:
                - Video titles
                - View counts
                - Like counts
                - Comment counts
            - Channel-level data:
                - Subscriber count
                - Total likes
                - Total views
                - Total comments
        - The extracted data is saved as CSV files in a specified airflow directory which is mounted to the local directory.

- Data Ingestion:
    - The data extraction process described above feeds directly into data ingestion. As **`aws_etl_youtube.py`** uploads the CSV files to the S3 bucket's **`raw`** folder, the data becomes readily available for subsequent stages in the pipeline.

- Data Orchestration:
    - Apache Airflow is used to orchestrate the entire ETL process, scheduling tasks and managing dependencies.It can be deployed locally or in the cloud for scalability and reliability.

- Data Transformation:
    - AWS Glue notebook is employed to transform the raw data. This calculating basic statistics (e.g., average view count, avgerage likes, and average comment) and then merging with one of the spark dataframes.
    - The transformed data is saved as CSV files in the **`transformed`** folder on S3.

- Data Visualization:
    - Various BI tools (Power BI, QuickSight, Tableau, Looker Studio) can be used to visualize the data and create interactive dashboards.

![My dashboard](https://raw.githubusercontent.com/syedhaziq/AWS-Youtube-Scraping/refs/heads/main/youtube%20dasboard.png)

- Technologies:
    - Python
    - YouTube Data API
    - AWS S3
    - Apache Airflow
    - AWS Glue
    - Power BI
