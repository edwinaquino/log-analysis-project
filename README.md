# Logs Analysis Project
### Project Goal Questions
1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

Example:

    "Princess Shellfish Marries Prince Handsome" — 1201 views
    "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
    "Political Scandal Ends In Political Scandal" — 553 views

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

Example:

    Ursula La Multa — 2304 views
    Rudolf von Treppenwitz — 1985 views
    Markoff Chaney — 1723 views
    Anonymous Contributor — 1023 views

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer back to this lesson if you want to review the idea of HTTP status codes.)

Example:

    July 29, 2016 — 2.5% errors


## Requirements
* VirtualBox 5.1
* Vagrant 1.9.1 
* Python 2.7.13
* psycopg2
* Postgresql 9.5.8

## How to Install

To successfully run this script, you must install VirtualBox in your Windows, Mac or Linux. [Download VirtualBox](https://www.virtualbox.org/wiki/Downloads)

Secondly, you will need to install Vagrant to share the folder to your virtual machine. [Download Vagrant](https://www.vagrantup.com/downloads.html)

Next, [download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) . You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

to start vagrant, inside the vagrant directory which you donloaded from the zip file and use this command: `vagrant up`

The download will start. It is a big file, be patient. Once the installation of your virtual machine has completed, you can connect to your new virtual machine using SSH with the following command: `vagrant ssh`

After you have successfully connected to the virtual machine, installed the database included in the zip file, the file name is newsdata.sql
NOTE: psql already comes pre-installed in the virtual machine

`psql -d news -f newsdata.sql`

Here's what this command does:

`psql` — the PostgreSQL command line program
`-d news` — connect to the database named news which has been set up for you
`-f newsdata.sql` — run the SQL statements in the file newsdata.sql


next, clone this git dispository to dowload this python script:
`git clone `

change direcotry to log-analysis-project
`cd log-analysis-project`

run the python script
`python log-analysis.py`



















* load the data onto the database
```sql
psql -d news -f newsdata.sql
```
* connect to the database
```sql
psql -d news
```
* create views
* python3 LogsAnalysis.py

### Create Views
```sql
CREATE VIEW author_info AS
SELECT authors.name, articles.title, articles.slug
FROM articles, authors
WHERE articles.author = authors.id
ORDER BY authors.name;
```

```sql
CREATE VIEW path_view AS
SELECT path, COUNT(*) AS view
FROM log
GROUP BY path
ORDER BY path;
```

```sql
CREATE VIEW article_view AS
SELECT author_info.name, author_info.title, path_view.view
FROM author_info, path_view
WHERE path_view.path = CONCAT('/article/', author_info.slug)
ORDER BY author_info.name;
```

```sql
CREATE VIEW total_view AS
SELECT date(time), COUNT(*) AS views
FROM log 
GROUP BY date(time)
ORDER BY date(time);
```

```sql
CREATE VIEW error_view AS
SELECT date(time), COUNT(*) AS errors
FROM log WHERE status = '404 NOT FOUND' 
GROUP BY date(time) 
ORDER BY date(time);
```

```sql
CREATE VIEW error_rate AS
SELECT total_view.date, (100.0*error_view.errors/total_view.views) AS percentage
FROM total_view, error_view
WHERE total_view.date = error_view.date
ORDER BY total_view.date;