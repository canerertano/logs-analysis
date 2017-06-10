# Logs Analysis Project
This is Udacity FSND Logs Project. The python code runs sql queries via **psycong2** library to find out insights below from database which contains a web site's logs also authors and articles info.
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

### Instructions
In order to run the program follow the commands below. Before running these commands make sure you have the installed required software **python3**, **vagrant** and **postgresql**. Also you should run the **newsdata.sql** given by Udacity.

* Clone the repository to your vagrant location.
* Run the command once below to create views which contains queries to answer questions;
```sh
$ psql -d news -f create_views.sql
```

* Run this command to see result;
```sh
$ python3 logs_analysis.py
```

## Author
@cnrkfks