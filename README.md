# AWS-Youtube-Scraping

## Overview

This project is a data pipeline designed to Extract, Transform, and Load (ETL) data from any YouTube channel. It allows you to analyze and visualize channel data to gain insights into its performance.

## Data Flow

- Data Extration:
    - youtube_etl.py:
        - This script utilizes the YouTube Data API to retrieve data from the MrBeast channel.
        - It extracts information such as:
            - Video-level data:
                - Video titles
                - Descriptions
                - Publication dates
                - View counts
                - Like counts
                - Comment counts
            - Channel-level data:
                - Subscriber count
                - Total likes
                - Total views
                - Total comments
        - The extracted data is saved as CSV files in a specified local directory.