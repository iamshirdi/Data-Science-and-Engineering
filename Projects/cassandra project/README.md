# Project Details
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.

They'd like a data engineer to create an Apache Cassandra database which can create queries on song play data to answer the questions, and wish to bring you on the project. Your role is to create a database for this analysis. You'll be able to test your database by running queries given to you by the analytics team from Sparkify to create the results.

# Files
- event_data contains source data of event logs
- project_1b* .ipynb is our source file which contains etl transformations 
- gets data from csv files in different files of  event_data . loads into table based on queries for faster read optimization, low latency, writes since its big data and needed for analysis
- cassandra is our prefered choice since  it provides avialblity not conisistency and durability