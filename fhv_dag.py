import requests
import pendulum
import json

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from google.cloud import bigquery
from google.cloud import storage


properties = {
    "project_id": "gcp-data-work",
    "dataset_id": "gcp_data_work_ds",
}

def get_json_data(url):
    session = requests.get(url)
    return session.json()
    


def get_url_by_last_date_updated(execution_date):
    # return f"https://data.cityofnewyork.us/resource/8wbx-tsch.json?last_date_updated={execution_date}"
    return "https://data.cityofnewyork.us/resource/8wbx-tsch.json?active=YES"


def fetch_data_to_storage(**kwargs):
    execution_date = kwargs["execution_date"]
    # json_data = get_json_data(get_url_by_last_date_updated(str(execution_date)[:10]))
    json_dict = get_json_data(get_url_by_last_date_updated(str(execution_date)[:10]))
    
    # json_dict = json.loads(json_data)
    # json_text = json.dumps(json_dict)
    json_string = ""
    for e in json_dict:
        json_string += "\n" + json.dumps(e)


    storage_client = storage.Client(project=properties['project_id'])
    bucket_name = "gcp-data-work-storage"

    bucket = storage_client.bucket(bucket_name)
    destination_blob_name = f"fhv/dt={str(execution_date)[:10]}/fhv_{str(execution_date)[:10].replace('-', '')}.json"
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string(json_string[1:])
    

with DAG(
    dag_id="fhv_dag",
    catchup=True,
    start_date=pendulum.datetime(2023, 9, 25, tz="UTC"),
    schedule="@daily",
    tags=["fhv", "dataset-scheduled"],
) as dag1:
    PythonOperator(task_id="download_fhv", python_callable=fetch_data_to_storage, dag=dag1)