CREATE OR REPLACE EXTERNAL TABLE gcp_data_work_ds.fhv
WITH PARTITION COLUMNS(dt DATE)
OPTIONS (
  uris = ['gs://gcp-data-work-storage/fhv/dt=*'],
  format = 'NEWLINE_DELIMITED_JSON',
  hive_partition_uri_prefix = 'gs://gcp-data-work-storage/fhv/'
  );