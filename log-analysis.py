#!/usr/bin/env python3

import psycopg2


def main():
    print('LOG ANALYSIS PROJECT\n-----------------');

    # Connection to database
    conn = psycopg2.connect("dbname=news")

    # Cursor for database connection
    cur = conn.cursor()

    # Question 1 - What are the most popular three articles of all time?
    most_popular_articles_sql = """
    SELECT x.title, count(*) AS num FROM ( 
                  SELECT a.title FROM articles a 
                  JOIN authors b ON(a.author = b.id) 
                  JOIN log c ON(c.path = '/article/' || a.slug ) 
                  WHERE c.status = '200 OK' 
    ) x GROUP BY x.title ORDER BY num DESC LIMIT 3
    """
    cur.execute(most_popular_articles_sql)
    print("Popular Articles:" + "\n")
    
    counter =1;
    for (title, num) in cur.fetchall():
        print("{}. {} - {} Views".format(counter, title, num) )
        counter = counter + 1
    print( ("." * 50) + "\n")



    # Question 2 - Who are the most popular article authors of all time?
    popular_authors_sql = """
            SELECT authors.name, count(log.status) AS num
            FROM authors, articles, log
            WHERE   authors.id = articles.author
              
            AND log.path = '/article/' || articles.slug
            GROUP BY authors.name
            ORDER BY num DESC;
    """
    cur.execute(popular_authors_sql)
    print("Popular Authors:\n")
    counter =1;
    for (author, num) in cur.fetchall():
        print("{}. {} - {} Views".format(counter, author, num))
        counter = counter + 1
    print("-" * 70)




if __name__ == "__main__":
 main()