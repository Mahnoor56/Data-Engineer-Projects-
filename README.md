
🚀 GCP Data Engineering Pipeline Project
This project demonstrates a complete data engineering pipeline built using Google Cloud Platform (GCP) services. The workflow fetches data from an external API, performs data transformation, and loads the clean data into BigQuery using Apache Airflow and Cloud Dataflow. The pipeline is event-driven and fully automated using Cloud Functions and Cloud Storage triggers.

📌 Project Overview
Steps Involved:

Data Ingestion (API to CSV):

Fetch data from an external REST crickbuzz API.

Convert and save the fetched data as a .csv file.

Data Storage (GCS):

Upload the CSV file to a Google Cloud Storage (GCS) bucket.

Data Transformation (Dataflow):

Trigger a Dataflow job (Apache Beam) to clean and transform the raw CSV data.

Event-Driven Automation (Cloud Function):

A Cloud Function is triggered automatically when a new file is uploaded to GCS.

This function starts the Dataflow job for transformation.

Data Orchestration (Apache Airflow):

Use Cloud Composer (Apache Airflow on GCP) to define a DAG that:

Monitors the pipeline.

Loads the cleaned/transformed data into a BigQuery table.

🛠️ Technologies & Tools Used
Google Cloud Platform

Cloud Storage

Cloud Functions

Cloud Dataflow (Apache Beam)

Cloud Composer (Apache Airflow)

BigQuery

Python

Apache Airflow

REST API

CSV
