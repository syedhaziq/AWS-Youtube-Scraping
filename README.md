# AWS-Youtube-Scraping

## Overview

This project is a data pipeline designed to Extract, Transform, and Load (ETL) data from any YouTube channel. It allows you to analyze and visualize channel data to gain insights into its performance.

## Data Flow

- Data Extration:
    - youtube_etl.py:
        - This script utilizes the YouTube Data API to retrieve data from the MrBeast (can be change to other some other) channel.
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

- Data Ingestion::
    - The data extraction process described above feeds directly into data ingestion. As aws_etl_youtube.py uploads the CSV files to the S3 bucket's "raw" folder, the data becomes readily available for subsequent stages in the pipeline.

- Data Orchestration:
    - Apache Airflow is used to orchestrate the entire ETL process, scheduling tasks and managing dependencies.

