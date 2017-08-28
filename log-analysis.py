#!/usr/bin/env python3

import psycopg2


def main():
    print('Log Analysis Script started...');

    # Connection to database
    conn = psycopg2.connect("dbname=news")

    # Cursor for database connection
    cur = conn.cursor()

    # Question 1 - What are the most popular three articles of all time?




if __name__ == "__main__":
 main()