#!/usr/bin/env python3

import psycopg2


def main():
    print('LOG ANALYSIS PROJECT\n');

    # Connection to database
    conn = psycopg2.connect("dbname=news")

    # Cursor for database connection
    cur = conn.cursor()

    # Question 1 - What are the most popular three articles of all time?
    most_popular_articles_sql = """
    SELECT x.title, count(*) AS count FROM ( 
                  SELECT a.title FROM articles a 
                  JOIN authors b ON(a.author = b.id) 
                  JOIN log c ON(c.path = '/article/' || a.slug ) 
                  WHERE c.status = '200 OK' 
    ) x GROUP BY x.title ORDER BY count DESC LIMIT 3
    """
    cur.execute(most_popular_articles_sql)
    print("The Most Popular Articles:" + "\n")
    
    counter =1;
    for (title, view) in cur.fetchall():
        print("{} - {} views".format(counter, title, view) )
        counter = counter + 1
    print( ("." * 50) + "\n\n")



if __name__ == "__main__":
 main()