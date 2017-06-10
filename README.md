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