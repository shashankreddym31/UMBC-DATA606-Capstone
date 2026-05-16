# Dataset Information

## Dataset Used
This project uses the Chicago Traffic Crashes dataset from the City of Chicago Open Data Portal.

## Dataset Availability
The original dataset file is not uploaded directly to this repository because the dataset is very large in size and exceeds practical GitHub storage limits.

Dataset source:
https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if

If the direct link shows an access restriction or "Forbidden" message, the dataset can be searched manually on the Chicago Open Data Portal using the keyword:
Chicago Traffic Crashes dataset

## Dataset Description
The dataset contains detailed records of reported traffic crashes in Chicago.

Each record includes information such as:
- Crash date and time
- Weather conditions
- Lighting conditions
- Road surface condition
- Speed limit
- Traffic control devices
- Crash type
- Primary contributing cause
- Injury details

Each row represents one traffic crash incident.

## Dataset Size
- Format: CSV
- Large-scale public dataset (over 1 million records)
- Not stored directly in this repository due to file size limitations

## Features Used in This Project
Selected variables include:
- POSTED_SPEED_LIMIT
- WEATHER_CONDITION
- LIGHTING_CONDITION
- ROADWAY_SURFACE_COND
- FIRST_CRASH_TYPE
- PRIM_CONTRIBUTORY_CAUSE
- LANE_CNT
- CRASH_HOUR
- CRASH_DAY_OF_WEEK
- CRASH_MONTH
- INJURIES_FATAL
- INJURIES_INCAPACITATING

## Target Variable
A binary classification target is created:

- Severe = 1 → fatal injury or incapacitating injury present
- Severe = 0 → otherwise

## Project Purpose
This dataset is used to build a machine learning model for predicting traffic crash severity.
