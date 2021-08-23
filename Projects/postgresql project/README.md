# INTRODUCTION

- A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

- They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

# Database Design and  Schema
- JSON songs data and logs data is converted to songs,users,time,artists dimensions table
- Fact table called songs_table is created by getting unique id from logs joined with name description details from songs
- all tables unique primary key is assigned to preserve data integrity and data replication
- Sparkify needs queries on songs together with users which can be easily accessed by fact table for faster reads optimized designed based on star schema
- Dimension tables are designed for easier join rare queries that need to be performed

# Files.Scripts,Jupyter-notebook
- Data folder contains multiple songs,log json data files in the respective sub-folders
- create_tables.py file creates songs,users etc tables and drops tables if already exists. This is used to create tables initially or reset tables
- sql_queries.py file contains schema of each table and values that need to be inserted
- etl.py inserts data from songs,log json files obtained in directories into tables according to sql_queries design
- etl.ipynb contains interactive view of etl.python script how the data is extracted from directories transformed json to structure and load into tables
- test.ipynb is used to test the data loaded into tables

# Instructions to run 
- run create_tables.py to create tables and etl to load data  into tables and test.ipynb to check the data loaded interactively