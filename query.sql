# Q1
with vw_median_age as (
select distinct extract(year from current_date)-vehicle_year age from gcp_data_work_ds.fhv
)
select distinct percentile_cont(age, 0.5) over () median_age from vw_median_age


# Q2
with base as (
select substring(vehicle_vin_number, 1, 3) vehicle_vin_number_manu_code, 
count(*) num_of_vehicles
from gcp_data_work_ds.fhv
group by substring(vehicle_vin_number, 1, 3)
)
select * from base

# The vehicle_vin_number_manu_code (first three letters of vehicle_vin_number) can be used to identify the actual manufacture's code.
We can create a mapping table between vehicle_vin_number_manu_code to the manufacturer to finally answer Q2.


