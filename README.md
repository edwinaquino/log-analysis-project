# Logs Analysis Project

The purpose of this app is to analyze data from a PostgreSQL database and to answer three questions

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

## Installation

To successfully run this script, you must install VirtualBox in your Windows, Mac or Linux. [Download VirtualBox](https://www.virtualbox.org/wiki/Downloads)

Secondly, you will need to install Vagrant to share the folder to your virtual machine. [Download Vagrant](https://www.vagrantup.com/downloads.html)

Next, You will need to download the following two files

[fsnd-virtual-machine.zip](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)

[newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) .

You will need to unzip the newsdata.zip file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

to start vagrant, inside the vagrant directory which you downloaded from the fsnd-virtual-machine.zip file, change directory to the vagrant directory and use this command: `vagrant up`

The download will start. It is a big file, be patient. Once the installation of your virtual machine has completed, you can connect to your new virtual machine using SSH with the following command: `vagrant ssh`

After you have successfully connected to the virtual machine, installed the database included in the zip file, the file name is newsdata.sql
NOTE: PostgreSQL already comes pre-installed in the virtual machine

`psql -d news -f newsdata.sql`

Here's what this command does:

`psql` — the PostgreSQL command line program
`-d news` — connect to the database named news which has been set up for you
`-f newsdata.sql` — run the SQL statements in the file newsdata.sql


next, clone this git dispository to dowload this python script:
`git clone https://github.com/edwinaquino/log-analysis-project.git`

change directory to log-analysis-project
`cd log-analysis-project`

run the python script
`python log-analysis.py`

## EXAMPLE OUTPUT:

`LOG ANALYSIS PROJECT
-----------------
Most Popular Articles:

1. Candidate is jerk, alleges rival - 338647 Views
2. Bears love berries, alleges bear - 253801 Views
3. Bad things gone, say good people - 170098 Views
..................................................

Most Popular Authors:

1. Ursula La Multa - 507594 Views
2. Rudolf von Treppenwitz - 423457 Views
3. Anonymous Contributor - 170098 Views
4. Markoff Chaney - 84557 Views
..................................................

Days with more than 1% errors:

2016-07-17 - 2.3% errors
..................................................`
