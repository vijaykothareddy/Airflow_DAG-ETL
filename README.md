# NYCTaxi_Trip-Fare_Analytics
Data model design and analysis for NYC Taxi trip data

# Introduction & Goals
The Project is design of a data model to perform data analysis and Visualization from semi-structured data.
Other data factors that has been taken in to account are,
**scale with data size**, 
**performance** and 
**develop predictive analytic models**


# Contents

- [The Data Set](#the-data-set)
- [Used Tools](#used-tools)
  - [Storage](#storage)
- [Pipelines](#pipelines)
  - Data Analysis
      - [Python](Code/NYC_Taxi_Trip_DataAnalysis.ipynb)
      - [SQL](Code/EDA.sql)
      - [Performance](Images/)
  - [Visualizations](Images/)
- [Follow Me On](#follow-me-on)
- [Appendix](#appendix)


# The Data Set
### Explain the data set

The dataset is about NYC taxi operations for year 2013, each row corresponds to a single taxi trip.

I selected a week worth of data to support the data model and analytics project.

Below is the table of some of the non self-explanatory column names,

| Attribute        | Description   |        
| ------------- |:-------------:| 
| Medallion     | A permit to operate yellow-taxi |
| Hack License      | license to drive a vehicle     |
| Store_and_fwd_flag | flag that indicates if it has stored in device before sending to server      |


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

- AWS Services

AWS Glue, AWS Athena, AWS S3

- Programming

Python, SQL


# Pipelines
Data Model displayed below helps to quickly run interactive queries to gain insights on the data that has been staged on Amazon S3.

Crawler's are created  using AWS Glue console to crawl the CSV data and store metadata in catalogue database.

Athena is serverless interactive SQL interface which can easily integrates with Glue and  schema details are immediately available to run queries against you data.


![](https://github.com/vijaykothareddy/NYCTaxi_Trip-Fare_Analytics/blob/main/Images/Data_Model_b.png)



# Follow Me On
Add the link to your LinkedIn Profile


