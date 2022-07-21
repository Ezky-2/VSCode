### requests to run
mysql.connctor.python or any other sql
sseclient

### how to run
First change your bot token in values.py
create your sql and your table
change them in values.py
run Run.py
Enjoy

### sql and table
CREATE DATABASE #db_name#;

USE #db_name#;

CREATE TABLE #table_name# (
    ID VARCHAR(255) PRIMARY KEY ,
    Name VARCHAR(255) NOT NULL ,
    Amtiaz INT DEFAULT 0,
    Rank VARCHAR(255) DEFAULT 'Normal',
    Tedad_davat INT DEFAULT 0,
    Tedad_seke INT DEFAULT 50
);

CREATE TABLE #table_name# (
    Name VARCHAR(255) PRIMARY KEY
);
