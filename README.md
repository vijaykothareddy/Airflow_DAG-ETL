# Airflow_DAG-ETL
Setup workflow to capture the response and upload to S3 as json file.  Covnert JSON to CSV with transformation.

# Introduction & Goals
To write a DAG ( Dynamic Acyclic Graph ) to orchestate the workflow of below tasks on Airflow.


# Contents

- [The Data Set](#the-data-set)
- [Used Tools](#used-tools)
  - [Storage](#storage)
- [Pipelines](#pipelines)
  - Data Analysis
      - [Python](Code/NYC_Taxi_Trip_DataAnalysis.ipynb)
      - [Self-Check](Images/)
- [Follow Me On](#follow-me-on)
- [Appendix](#appendix)


# The Data Set
### Explain the data set

The JSON response from S3 Website enpoints.


### What do you like about it?

Interesting data set with time and date columns that helps to draw various insights, calculated columns and time based analytics.

Latitude and Longitude co-ordinates for pick up and drop-off locations.


### What is problematic?

Mapping the Latitude and Longitude columns to location names.

There is some missing data which requires either to ignore or impute based on the ML model exploration.

I used an external data related to NYC location names and id's to join with trip data for location name transformation.


# Used Tools
- Client

Jupyter NoteBook, VS Code

- Wokflow Tool

Apache Airflow

- Programming

Python


# Pipelines
Data Model displayed below helps to quickly run interactive queries to gain insights on the data that has been staged on Amazon S3.

Crawler's are created  using AWS Glue console to crawl the CSV data and store metadata in catalogue database.

Athena is serverless interactive SQL interface which can easily integrates with Glue and  schema details are immediately available to run queries against you data.


![](https://github.com/vijaykothareddy/NYCTaxi_Trip-Fare_Analytics/blob/main/Images/Data_Model_b.png)



# Follow Me On
Add the link to your LinkedIn Profile


