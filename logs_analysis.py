#!/usr/bin/env python3

import psycopg2

db_name = "news"
error = False

db_error_message = "An error occurred while performing a database operation"
question_1 = "\n1. What are the most popular three articles of all time?"
question_2 = "\n2. Who are the most popular article authors of all time?"
question_3 = "\n3. On which days did more than 1% of requests lead to errors?"

# This method connects to database, executes the given query as parameter
# and returns the query result


def execute_query(query):
    try:
        db = psycopg2.connect(dbname=db_name)
        cur = db.cursor()
        cur.execute(query)
        result = cur.fetchall()
        return result
        db.close()
    except Exception as e:
        print(db_error_message)
        global error
        error = True


# This method calls execute_query method with a select query on
# most_popular_articles view in the db as parameter
# and prints the top 3 popular articles


def most_popular_articles():
    if not error:
        result = execute_query("select * from most_popular_articles limit 3;")
        if result is not None:
            print(question_1)
            for v in result:
                print(
                    " {0} - {1} views".format(v[0], "{:,}".format(int(v[1]))))


# This method calls execute_query method with a select query on
# most_popular_authors view in the db as parameter
# and prints the most popular article authors


def most_popular_authors():
    if not error:
        result = execute_query("select * from most_popular_authors;")
        if result is not None:
            print(question_2)
            for v in result:
                print(
                    " {0} - {1} views".format(v[0], "{:,}".format(int(v[1]))))


# This method calls execute_query method with a select query on
# days_with_most_errors view in the db as parameter
# and prints days did more than 1% of requests lead to errors


def days_with_most_errors():
    if not error:
        result = execute_query(
            "select * from days_with_most_errors where rate > 1;")
        if result is not None:
            print(question_3)
            for v in result:
                print(" {0} - {1}% errors".format(v[0].strftime(
                    '%b, %d %Y'), "{:,}".format(float(v[1]))))


def main():
    most_popular_articles()
    most_popular_authors()
    days_with_most_errors()

main()
