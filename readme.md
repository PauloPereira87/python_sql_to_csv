# Python - SQL to CSV

A simple script to save data from MS SQL Server to CSV files, using a simple configuration file:

myconfig.py :

```
server = "Server_Name_or_IP"
database = "Database_Name"
query = ("SELECT [ID]"
    ",[NAME]"
    "FROM [AdventureWorks].[Test_Schema].[Test_Table]")

user = "username"
pwd = "password"
```

## Configuration

This script needs the "pyodbc" dependency installed:

> pip install odbc

or

> py -m pipenv install