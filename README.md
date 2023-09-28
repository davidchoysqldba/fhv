# fhv

## Part 1: File fhv_dag.py is the Python Dag that does the following:
Download content into memory.
Transform json content format to be queriable by BigQuery external table.
Uploading final product into Google Storage.


## Part 2: File bq.sql
DDL for BigQuery External table into json files in Google Storage

## Part 3: File query.sql
SQL Statement to answer questions from part 3



## What would I do differently
The most challenging area of this task was creating the BigQuery external table.
The downloading json content had to be reproduced in order to be accepted into BigQuery.
So a few hours of research was required to resolve this issue.

Next time, I would look into converting the json file into parquet files, which might be easier integrate with BigQuery.


This is the downloaded json content
[{"active":"YES","vehicle_license_number":"5128748","name":"NELO,ENTERPRISES,CORP.","license_type":"FOR HIRE VEHICLE","expiration_date":"2024-11-14T00:00:00.000","permit_license_number":"AA004","dmv_license_plate_number":"T499091C","vehicle_vin_number":"JTNBB46K373012490","certification_date":"2017-03-17T00:00:00.000","hack_up_date":"2017-03-24T00:00:00.000","vehicle_year":"2007","base_number":"B03407","base_name":"ZOOM TRANSIT INC","base_type":"BLACK-CAR","veh":"HYB","base_telephone_number":"(718)583-9100","base_address":"2078 CROSS BRONX EXPRESSWAY BRONX NY 10472","reason":"G","last_date_updated":"2023-09-27T00:00:00.000","last_time_updated":"13:25"},

,{"active":"YES","vehicle_license_number":"6032728","name":"UPPAL, ARSHDEEP","license_type":"FOR HIRE VEHICLE","expiration_date":"2025-06-30T00:00:00.000","permit_license_number":"AA005","dmv_license_plate_number":"T117661C","vehicle_vin_number":"KMHLM4AJ2NU023825","wheelchair_accessible":"PILOT","vehicle_year":"2022","base_number":"B02390","base_name":"TEL AVIV CAR & LIMOUSINE SERVICE INC.","base_type":"LIVERY","veh":"HYB","base_telephone_number":"(800)222-9888","base_address":"43-23   35 STREET LIC NY 11101","reason":"G","last_date_updated":"2023-09-27T00:00:00.000","last_time_updated":"13:25"}
]


This is the reproduced json content integrating with BigQuery
{"active": "YES", "vehicle_license_number": "5128748", "name": "NELO,ENTERPRISES,CORP.", "license_type": "FOR HIRE VEHICLE", "expiration_date": "2024-11-14T00:00:00.000", "permit_license_number": "AA004", "dmv_license_plate_number": "T499091C", "vehicle_vin_number": "JTNBB46K373012490", "certification_date": "2017-03-17T00:00:00.000", "hack_up_date": "2017-03-24T00:00:00.000", "vehicle_year": "2007", "base_number": "B03407", "base_name": "ZOOM TRANSIT INC", "base_type": "BLACK-CAR", "veh": "HYB", "base_telephone_number": "(718)583-9100", "base_address": "2078 CROSS BRONX EXPRESSWAY BRONX NY 10472", "reason": "G", "last_date_updated": "2023-09-27T00:00:00.000", "last_time_updated": "13:25"}
{"active": "YES", "vehicle_license_number": "6032728", "name": "UPPAL, ARSHDEEP", "license_type": "FOR HIRE VEHICLE", "expiration_date": "2025-06-30T00:00:00.000", "permit_license_number": "AA005", "dmv_license_plate_number": "T117661C", "vehicle_vin_number": "KMHLM4AJ2NU023825", "wheelchair_accessible": "PILOT", "vehicle_year": "2022", "base_number": "B02390", "base_name": "TEL AVIV CAR & LIMOUSINE SERVICE INC.", "base_type": "LIVERY", "veh": "HYB", "base_telephone_number": "(800)222-9888", "base_address": "43-23   35 STREET LIC NY 11101", "reason": "G", "last_date_updated": "2023-09-27T00:00:00.000", "last_time_updated": "13:25"}

{"active": "YES", "vehicle_license_number": "5953896", "name": "ELIHORI,ASIM,SALIH", "license_type": "FOR HIRE VEHICLE", "expiration_date": "2023-11-07T00:00:00.000", "permit_license_number": "AA006", "dmv_license_plate_number": "T790912C", "vehicle_vin_number": "4T4BF1FK4FR457564", "certification_date": "2019-11-07T00:00:00.000", "hack_up_date": "2019-11-07T00:00:00.000", "vehicle_year": "2015", "base_number": "B03036", "base_name": "ZYNC INC", "base_type": "BLACK-CAR", "base_telephone_number": "(718)482-1818", "base_address": "12-04   44 AVENUE LIC NY 11101", "reason": "G", "last_date_updated": "2023-09-27T00:00:00.000", "last_time_updated": "13:25"}
{"active": "YES", "vehicle_license_number": "5729129", "name": "LORENZO,MARTIN", "license_type": "FOR HIRE VEHICLE", "expiration_date": "2024-10-12T00:00:00.000", "permit_license_number": "AA010", "dmv_license_plate_number": "T708186C", "vehicle_vin_number": "4T1B11HK3JU032982", "certification_date": "2018-02-14T00:00:00.000", "hack_up_date": "2018-02-16T00:00:00.000", "vehicle_year": "2018", "base_number": "B03407", "base_name": "ZOOM TRANSIT INC", "base_type": "BLACK-CAR", "base_telephone_number": "(718)583-9100", "base_address": "2078 CROSS BRONX EXPRESSWAY BRONX NY 10472", "reason": "G", "last_date_updated": "2023-09-27T00:00:00.000", "last_time_updated": "13:25"}
{"active": "YES", "vehicle_license_number": "6035913", "name": "GULYAMOV, AMINJON", "license_type": "FOR HIRE VEHICLE", "expiration_date": "2025-06-30T00:00:00.000", "permit_license_number": "AA013", "dmv_license_plate_number": "T118710C", "vehicle_vin_number": "JTDKN3DU5D0352182", "wheelchair_accessible": "PILOT", "vehicle_year": "2013", "base_number": "B02453", "base_name": "MCW CAR & LIMO INC.", "base_type": "BLACK-CAR", "veh": "HYB", "base_telephone_number": "(718)387-0700", "base_address": "355 UNION AVENUE BROOKLYN NY 11211", "reason": "G", "last_date_updated": "2023-09-27T00:00:00.000", "last_time_updated": "13:25"}



