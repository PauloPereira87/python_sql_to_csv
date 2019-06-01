import pyodbc
import csv
import getpass

from myconfig import *

filename = input('Filename: ')

if (len(filename) < 1): 
    filename = "output"

credentials = f"uid={user};pwd={pwd}"

connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};" + f"Server={server};" + f"Database={database};" + credentials)

cursor = connection.cursor()

cursor.execute(
    query
)

with open("output\\" + filename + ".csv","w", newline='') as outfile:
    writer = csv.writer(outfile, delimiter =';', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(col[0] for col in cursor.description)
    for row in cursor:
        writer.writerow(row)

cursor.close()
connection.close()